# Smart-Attendance-System-version-2.0-Using-Face-Recognition

About The Project:

This is a GUI application that is built using the PyQT5 Module in Python. It is capable of performing the following tasks:

* It takes the Attendance of the Students by Qrcode Scanning method and it Generates the Qrcode of every Student.
* It automatically stores the attendance values in MySQL DataBase
* Every student's Images of their face are stored as labelled data. Students have to show their faces to the scanner and the system notes down their attendance
* This Application is capable of detecting the face i.e., it can detect if the attendance is being marked in real-time 

## Deployment

To Run the program

```bash
  Python loginpage.py
```
To create the Database
```MySQL
  create database college;
```
To create the table
```MySQL
  create table classroom(sid int,name varchar(20),Department char(5),year int,attendance char(10));
```
Set the MySQL User Account 
```MySQL
  mysql> CREATE USER ‘root’@’localhost’ IDENTIFIED BY ‘root’;
```
Install the QT Designer Software to drag and drop the GUI widgets and design the application
![App Screenshot](http://1.bp.blogspot.com/-PWsZkWMcXJc/UCa78WJeU_I/AAAAAAAAACo/-0a5QLzuAiE/s1600/hw.py.jpg)

Link : https://doc.qt.io/qt-6/qtdesigner-manual.html
## Installation

Install my-project with git

```bash
  apt-get install git+git clone https://github.com/pr4dyumn4/SmartAttendanceSystemversion-2.0UsingFace-Recognition
  cd SmartAttendenceSystem
```
To install the requirements

```
    pip install -r requirements.txt
```
## Screenshots
LOGIN PAGE:
This is the Admin Login page for authentication. Username and password

![App Screenshot](Screenshot/Screenshot1.png)

HOME PAGE:
This is the main page of the application, Manage Student, Dashboard, Export to CSV, It can also scan the face while scanning the video will be stored in the video File Admin can check so that no fake attendance is marked.

![App Screenshot](Screenshot/Screenshot2.png)

MANAGEMENT PAGE:
IN here student data can be added, updated, deleted, and Generate a single Qrcode.

![App Screenshot](Screenshot/Screenshot4.png)
![App Screenshot](Screenshot/Screenshot5.png)
![App Screenshot](Screenshot/Screenshot6.png)
![App Screenshot](Screenshot/Screenshot7.png)
![App Screenshot](Screenshot/Screenshot8.png)

Dashboard PAGE:
Here you can view the attendance and strength of the classroom through a pie chart you can view the attendance

![App Screenshot](Screenshot/Screenshot3.png) 
![App Screenshot](Screenshot/Screenshot10.png) 

SCANNING WINDOW:

![App Screenshot](Screenshot/Screenshot9.png)

## 🚀 About Project
This is a GUI application made to manage students' Attendance using a face Scan.
## Used By
