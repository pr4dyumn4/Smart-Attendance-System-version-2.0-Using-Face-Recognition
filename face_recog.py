import face_recognition
import cv2
from cv2 import VideoWriter_fourcc
import numpy as np
import os
from Attendence import Mark
import traceback
from PyQt5.QtWidgets import QMessageBox
import datetime as dt
import datefolder

class FaceRecognizer:
    def __init__(self) -> None:
        self.video_capture = cv2.VideoCapture(0)
        self.today = dt.datetime.now()
        a =  self.today.strftime('%d%m%Y')+' - '+self.today.strftime('%H %M')
        datefolder.create_folder()
        self.a = "./captures/"+a
        self.cap = cv2.VideoWriter(self.a+"/webcam.avi", VideoWriter_fourcc(*'MP42'), 25.0, (640,480))
        self.known_face_encodings = []
        self.known_face_names = []
        self.process_this_frame = True
        self.bunty = []
        # Directory containing sample pictures
        self.samples_dir = './photos'
        # Initialize attendance marker
        self.mark = Mark()
        # Load known face encodings and names
        self.load_samples()
        # Directory containing sample pictures
        self.samples_dir = './photos'
    def open_markAttnded(self):
        self.mark = Mark()
        self.mark.markattendence()
    def enterData(self,z):
        if z in self.known_face_names :
            with open('attendence.txt', 'a') as fob:
                self.bunty.append(z)
                fob.write(z+'\n')
        print('Reading...')  
    def checkData(self,data):    
        data = str(data)
        if data in self.bunty:
            print('Already Present')
        else:
            print('\n'+str(len(self.bunty)+1)+'\n'+data)
            self.enterData(data)
    def load_samples(self):
        # Loop through all image files in the directory
        for file_name in os.listdir(self.samples_dir):
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                # Load image file
                image_path = os.path.join(self.samples_dir, file_name)
                image = face_recognition.load_image_file(image_path)
                face_locations = face_recognition.face_locations(image)
                if len(face_locations) == 0:
                    print(f"No faces detected in {file_name}. Skipping...")
                    continue
                # Encode face in the image and add it to known_face_encodings
                face_encoding = face_recognition.face_encodings(image)[0]
                self.known_face_encodings.append(face_encoding)
                # Add name of the person in the image to known_face_names
                name = file_name.split('.')[0]  # Remove file extension
                self.known_face_names.append(name)
    def camera_off(self):
        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
    def showDialog(self):
      msgBox = QMessageBox()
      msgBox.setIcon(QMessageBox.Information)
      msgBox.setText("Scanned Successfully")
      msgBox.setWindowTitle("QMessageBox Example")
      msgBox.setStandardButtons(QMessageBox.Ok )
      msgBox.buttonClicked.connect(self.msgButtonClick)
      returnValue = msgBox.exec()
      if returnValue == QMessageBox.Ok:
         print('OK clicked')
    def msgButtonClick(self,i):
      print("Button clicked is:",i.text())
    def main(self):
            with open('attendence.txt', 'w') as fob:
                fob.write('')
            try:
                process_this_frame = True 
                while True:
                    # Grab a single frame of video
                    ret, frame = self.video_capture.read()
                    b = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    cv2.putText(frame, b,(10, 25), cv2.FONT_HERSHEY_DUPLEX,0.8,(0, 0, 255),1,cv2.LINE_AA)
                    # Only process every other frame of video to save time
                    if process_this_frame:
                        # Resize frame of video to 1/4 size for faster face recognition processing
                        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                        rgb_small_frame = small_frame[:, :, ::-1]
                        # Find all the faces and face encodings in the current frame of video
                        face_locations = face_recognition.face_locations(rgb_small_frame)
                        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                        face_names = []
                        for face_encoding in face_encodings:
                            # See if the face is a match for the known face(s)
                            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                            name = "Unknown"
                            # # If a match was found in self.known_face_encodings, just use the first one.
                            # if True in matches:
                            #     first_match_index = matches.index(True)
                            #     name = known_face_names[first_match_index]
                            # Or instead, use the known face with the smallest distance to the new face
                            matched_indices = [index for index, match in enumerate(matches) if match]
                            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                                matched_labels = [self.known_face_names[index] for index in matched_indices]
                                best_match_label = self.known_face_names[best_match_index]
                                matching_percentage = (1 - face_distances[best_match_index]) * 100
                            face_names.append(name)
                    process_this_frame = not process_this_frame
                    # Display the results
                    for (top, right, bottom, left), name in zip(face_locations, face_names):
                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4
                        # Draw a box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                        # Draw a label with a name below the face
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, f"{name} ({matching_percentage:.2f}%)", (left, top - 10), font, 0.9, (0, 255, 0), 2)
                        # Display the resulting image
                        if matching_percentage >= 65:
                            self.checkData(name)
                            cv2.imwrite(self.a+f"/{name}.png",frame)
                    self.cap.write(frame)
                    cv2.imshow('Video', frame)
                        # Hit 'q' on the keyboard to quit!
                    if cv2.waitKey(1) & 0xFF == ord('q') :
                        break
            except Exception as e:
                traceback.print_exc()
            finally:
                self.open_markAttnded()
                self.camera_off()
                self.showDialog()
if __name__ == '__main__':
    cap = FaceRecognizer()
    cap.load_samples()
    cap.main()