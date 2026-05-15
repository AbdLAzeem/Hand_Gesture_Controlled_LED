🛠️ Hardware Setup
Requirements
1 × Arduino Uno

5 × LEDs

5 × 220Ω resistors

1 × Breadboard & Jumper wires

1 × USB Cable (PC to Arduino)

1 × Webcam (Built-in or External)

Connection Steps
Connect each LED’s anode (+) to its designated Arduino digital output pin through a 220Ω resistor.

Connect all LED cathodes (-) to a common ground rail, then route it to the Arduino's GND pin.

Plug the Arduino Uno into your computer's USB port.

💡 Logic: The number of LEDs turned ON corresponds directly to the number of detected raised fingers.

💻 Software Setup
Prerequisites
Python 3.8+

Arduino IDE (for uploading the controller sketch)

Installation
Clone the repository:

Bash
git clone [https://github.com/yourusername/Hand_Gesture_Controlled_LED.git](https://github.com/yourusername/Hand_Gesture_Controlled_LED.git)
cd Hand_Gesture_Controlled_LED
Install Python dependencies:

Bash
pip install opencv-python cvzone mediapipe pyserial
Flash the Arduino:

Open your Arduino IDE.

Load the provided firmware file (e.g., arduino_controller.ino) located in the repository.

Select your board type and correct COM port, then click Upload.

📈 Usage
Connect the pre-wired Arduino Uno to your PC.

Run the main execution script:

Bash
python main.py
Position your hand clearly within the webcam's field of view.

Raise your fingers (0–5) to modulate the LED array in real time.

Press the 'K' key on your keyboard to exit the application.
