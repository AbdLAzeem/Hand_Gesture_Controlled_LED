# Hand_Gesture_Controlled_LED
Python | OpenCV | MediaPipe | Arduino Uno
Overview

This project implements a real-time hand gesture recognition system that detects the number of fingers raised using a webcam and controls LEDs connected to an Arduino Uno accordingly.

Using OpenCV and CVZone (MediaPipe Hand Tracking), the system tracks a single hand, determines finger states, and sends control signals to an external hardware controller. The project demonstrates an effective integration of computer vision, human–computer interaction, and embedded systems.

Features

Real-time hand tracking using a standard webcam

Accurate detection of raised fingers (0–5)

Live video feedback with finger count overlay

LED control via Arduino based on detected gestures

System Architecture
Webcam
   ↓
OpenCV + MediaPipe (Hand Tracking)
   ↓
Finger State Detection
   ↓
Python Controller Module
   ↓
Arduino Uno
   ↓
LEDs

Hardware Requirements

Arduino Uno - 5 × LEDs - 5 × 220Ω resistors - Breadboard - Jumper wires - USB cable (Arduino ↔ PC) - Webcam (built-in or external) 

Connection Steps:

Connect each LED’s anode (+) to its corresponding Arduino pin via a 220Ω resistor

Connect all cathodes (–) to GND

Connect Arduino to PC via USB

The number of LEDs turned ON corresponds to the number of detected raised fingers.
<img width="625" height="676" alt="Schematic_Diagram" src="https://github.com/user-attachments/assets/70240248-84d8-4327-ba12-2dc84e97ea15" />


Software Requirements

Python 3.8+ - Arduino IDE 

Required Python libraries: opencv-python - cvzone - mediapipe - pyserial

Usage

Connect the Arduino Uno to your computer

Ensure LEDs are wired correctly

Run the Python script:

python main.py


Hold your hand in front of the webcam

Raise fingers (0–5)

LEDs will light up according to finger count

Press K to exit the application


