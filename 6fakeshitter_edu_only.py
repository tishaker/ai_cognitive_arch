import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

print("Loading Multimodal Neural Network...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

image_path = "sample.jpg"
if not os.path.exists(image_path):
    print(f"\n[Error: Please save an image as '{image_path}' in this folder first!]")
else:
    raw_image = Image.open(image_path).convert('RGB')
    while True:
        user_prompt = input("\nAsk about the picture (or type 'exit'): ")
        if user_prompt.lower() == 'exit': break

        inputs = processor(raw_image, user_prompt, return_tensors="pt")
        with torch.no_grad():
            out = model.generate(**inputs)
        
        reply = processor.decode(out, skip_special_tokens=True)
        print(f"AI Vision Response: {reply}")
