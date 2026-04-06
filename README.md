# Autonomous Bolt Perception System
Computer Vision pipeline designed for identifying and tracking industrial fasteners in real-time.

#Technical
*Language: Python 3
*Library: OpenCV (cv2)
*Logic: HSV Color Thresholding + Contour Analysis

#Aspects
*Orientation Agnostic: Using min/max aspect ratio logic to detect bolts vertically and horizontally.
*Target Prioritization: Center-proximity weighting to maintain a stable lock on primary target.
*Optimization: Using Object-Oriented Programming (OOP).
*Telemetry Real-Time: On-screen FPS and coordinate tracking.

#Methods
*Color Filtering: Converts BGR frames to HSV, isolate metallic reflection.
*Geometry: Filtering noise by pixel area and calculates the object ratios to distinguish bolts from glares.
*Lock: Calculate the centroid (Cx, Cy) and draws a targeting crosshair.
