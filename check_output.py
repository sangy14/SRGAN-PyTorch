
import cv2

def check_image():
    img = cv2.imread('sr_output.png')
    if img is None:
        print("Error: Could not read sr_output.png")
        return
    print(f"Output image dimensions: {img.shape}")
    if img.shape == (400, 400, 3):
        print("SUCCESS: Image upscaled 4x correctly.")
    else:
        print("FAILURE: Image dimensions incorrect.")

if __name__ == "__main__":
    check_image()
