from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image
from io import BytesIO

import argparse
import os

# adapted from https://huggingface.co/dandelin/vilt-b32-finetuned-vqa

def load_image(image):
    if os.path.exists(image):
        with open(image, "rb") as file:
            raw_image_data = file.read()
            return Image.open(BytesIO(raw_image_data))
    else:
        try:
            response = requests.get(image, stream=True)
            return Image.open(response.raw)
        except Exception as e:
            raise ValueError(f"Unable to load image: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', '-i', type=str, help='The image to look at.', required=True)
    parser.add_argument('--question', '-q', type=str, help='The question to answer.', required=True)
    
    args = parser.parse_args()
    
    # prepare image + question
    image = load_image(args.image).convert("RGB")
    question = args.question

    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    # prepare inputs
    encoding = processor(image, question, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    print("Predicted answer:", model.config.id2label[idx])
