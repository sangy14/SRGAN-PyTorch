
import cv2
import numpy as np

def create_image():
    # Create a 100x100 dummy image with some patterns
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.rectangle(img, (20, 20), (80, 80), (255, 0, 0), -1)
    cv2.circle(img, (50, 50), 30, (0, 255, 0), -1)
    cv2.putText(img, 'LR', (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imwrite('sample_lr.png', img)
    print("Created sample_lr.png")

if __name__ == "__main__":
    create_image()
