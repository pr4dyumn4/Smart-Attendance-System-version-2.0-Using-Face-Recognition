import cv2
import os
def capture_image():
    camera = cv2.VideoCapture(0)  # Open the default camera (0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Failed to open camera")
        return

    while True:
        ret, frame = camera.read()

        if ret:
            cv2.imshow("Camera", frame)

            # Wait for the user to press a key
            key = cv2.waitKey(1)

            # Capture image when 'c' key is pressed
            if key == ord('c'):
                os.makedirs('tmp',exist_ok=True)
                cv2.imwrite("tmp/temp.jpg", frame)
                print("Image captured!")
                

            # End the program when 'q' key is pressed
            if key == ord('q'):
                break
        else:
            print("Failed to capture image")

    # Release the camera
    camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_image()
