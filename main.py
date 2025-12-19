from __future__ import annotations
import os
import sys

# Configure environment variables to use project folder for temporary/cache data
# This prevents files from occupying space on the C: partition
current_dir = os.path.dirname(os.path.abspath(__file__))

# Redirect Python pycache to a local folder
os.environ['PYTHONPYCACHEPREFIX'] = os.path.join(current_dir, '.pycache')

# Redirect Mediapipe and other libraries that might use user-specific temp paths
os.environ['MP_RESOURCE_PATH'] = current_dir
os.environ['MEDIAPIPE_RESOURCE_PATH'] = current_dir

# Ensure local venv is prioritized if not already activated
venv_path = os.path.join(current_dir, 'venv', 'Scripts')
if venv_path not in os.environ['PATH']:
    os.environ['PATH'] = venv_path + os.pathsep + os.environ['PATH']

import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

def main():
    print("Initializing Hand Tracking LED Control...")
    
    # Initialize Camera
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Error: Could not open camera.")
        input("Press Enter to exit...")
        sys.exit(1)
        
    # Initialize Hand Detector
    try:
        detector = HandDetector(detectionCon=0.8, maxHands=1)
    except Exception as e:
        print(f"Error initializing Hand Detector: {e}")
        video.release()
        input("Press Enter to exit...")
        sys.exit(1)
        
    # Initialize Arduino
    board = cnt.connect_arduino('COM11')
    leds = cnt.setup_leds(board)
    if not leds:
        print("Warning: Running without Arduino LED control.")

    window_name = "Hand Tracking LED Control"
    print(f"Application started. Press 'k' in the '{window_name}' window to quit.")

    try:
        while True:
            ret, frame = video.read()
            if not ret:
                print("Error: Could not read frame from camera.")
                break
                
            frame = cv2.flip(frame, 1)
            
            try:
                # findHands returns hands and img (frame with landmarks)
                hands, img = detector.findHands(frame, draw=True)
            except Exception as e:
                print(f"Hand detection error: {e}")
                hands = []

            if hands:
                hand = hands[0]
                try:
                    fingerUp = detector.fingersUp(hand)
                    fingersUpCount = sum(fingerUp)  
                    
                    # Update LEDs
                    cnt.update_leds(leds, fingersUpCount)  
                    
                    # Display count on screen
                    cv2.putText(
                        frame, 
                        f'Finger count: {fingersUpCount}', 
                        (20, 460), 
                        cv2.FONT_HERSHEY_COMPLEX, 
                        1, 
                        (0, 255, 0), 
                        2, 
                        cv2.LINE_AA
                    )
                except Exception as e:
                    print(f"Error processing hand data: {e}")

            cv2.imshow(window_name, frame)
            
            k = cv2.waitKey(1)
            # Exit on 'k' or if window is closed
            if k == ord("k") or cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                break
                
    except KeyboardInterrupt:
        print("\nStopping application...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        video.release()
        cv2.destroyAllWindows()
        print("Cleanup complete. Goodbye!")

if __name__ == "__main__":
    main()
