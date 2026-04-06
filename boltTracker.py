import cv2
import numpy as np
import time

class BoltTracker:
    def __init__(self):
        self.LOWER_METALLIC = np.array([0, 0, 100])
        self.UPPER_METALLIC = np.array([180, 50, 255])
        self.MIN_AREA = 2000
        self.SCREEN_CENTER = 320 

    def process_frame(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.LOWER_METALLIC, self.UPPER_METALLIC)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        best_target = None
        min_dist = float('inf')

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > self.MIN_AREA:
                x, y, w, h = cv2.boundingRect(cnt)
                
                # Orientation Agnostic Ratio
                ratio = max(w, h) / min(w, h)
                
                if ratio > 1.2:
                    cx, cy = int(x + w/2), int(y + h/2)
                    dist = abs(self.SCREEN_CENTER - cx)
                    
                    if dist < min_dist:
                        min_dist = dist
                        best_target = {'box': (x, y, w, h), 'center': (cx, cy)}
        
        return best_target

def main():
    cap = cv2.VideoCapture('test_video.mp4')
    tracker = BoltTracker()
    prev_time = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        # Calculate FPS
        new_time = time.time()
        fps = int(1 / (new_time - prev_time))
        prev_time = new_time

        # Logic
        target = tracker.process_frame(frame)

        # Visualization
        if target:
            x, y, w, h = target['box']
            cx, cy = target['center']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"LOCKED {cx},{cy}", (x, y-10), 2, 0.5, (0,255,0), 1)
        
        cv2.putText(frame, f"FPS: {fps}", (10, 30), 2, 1, (255, 255, 255), 2)
        cv2.imshow('Perception System', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
