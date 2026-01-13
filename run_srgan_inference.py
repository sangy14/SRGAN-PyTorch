
import os
import cv2
import torch
from model import srresnet_x4
from imgproc import preprocess_one_image, tensor_to_image
from utils import load_pretrained_state_dict

def run_inference():
    # Configuration
    model_arch = "srresnet_x4"
    model_weights_path = "./results/pretrained_models/SRGAN_x4-ImageNet.pth.tar"
    input_image_path = "./sample_lr.png"
    output_image_path = "./sr_output.png"
    device = torch.device("cpu") # Default to CPU for safety on Mac unless MPS confirms faster/stable
    
    # Check if files exist
    if not os.path.exists(model_weights_path):
        print(f"Error: Weights not found at {model_weights_path}")
        return
    if not os.path.exists(input_image_path):
        print(f"Error: Input image not found at {input_image_path}")
        return

    print(f"Initializing {model_arch}...")
    model = srresnet_x4()
    
    print(f"Loading weights from {model_weights_path}...")
    model = load_pretrained_state_dict(model, False, model_weights_path)
    model.eval()
    model = model.to(device)

    print(f"Processing image {input_image_path}...")
    # Preprocess (Note: inference.py uses half=False by default)
    input_tensor = preprocess_one_image(input_image_path, False, False, device)

    print("Running inference...")
    with torch.no_grad():
        sr_tensor = model(input_tensor)

    print("Saving output...")
    # Postprocess
    sr_image_numpy = tensor_to_image(sr_tensor, False, False)
    sr_image_bgr = cv2.cvtColor(sr_image_numpy, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_image_path, sr_image_bgr)
    
    print(f"Super-resolved image saved to {output_image_path}")

if __name__ == "__main__":
    run_inference()
