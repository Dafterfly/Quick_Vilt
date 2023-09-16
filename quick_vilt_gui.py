import tkinter as tk
from tkinter import filedialog

from transformers import ViltProcessor, ViltForQuestionAnswering
import requests
from PIL import Image, ImageTk
from io import BytesIO
import os

def browse_image():
    predicted_answer.set("")
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    entry_image.delete(0, tk.END)
    entry_image.insert(0, image_path)
    if not preview_var.get() and thumbnail_label:
        thumbnail_label.pack_forget()
    elif preview_var.get():
        display_thumbnail(image_path)

def preview_checkbox_changed():
    if not preview_var.get() and thumbnail_label:
        thumbnail_label.pack_forget()
    elif preview_var.get():
        display_thumbnail(image_path)

def display_thumbnail(image_path):
    global thumbnail_label

    if image_path:
        image = Image.open(image_path)
        image.thumbnail((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        if thumbnail_label:
            thumbnail_label.destroy()

        thumbnail_label = tk.Label(root, image=photo)
        thumbnail_label.image = photo
        thumbnail_label.pack(pady=10)

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

def run_prediction(event=None):
    
    
    predicted_answer.set("")
    image = load_image(entry_image.get()).convert("RGB")
    question = entry_question.get()
    print (f"Question: {question}")
    processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
    model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    encoding = processor(image, question, return_tensors="pt")

    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    answer = model.config.id2label[idx]
    predicted_answer.set(answer)
    print (f"Predicted answer: {answer}")

thumbnail_label = None

root = tk.Tk()
root.title("Vilt VQA GUI")

tk.Label(root, text="Image Path:").pack(pady=5)
entry_image = tk.Entry(root, width=50)
entry_image.pack(pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

browse_button.bind('<Return>', browse_image)

preview_var = tk.BooleanVar()
tk.Checkbutton(root, text="Preview Image", command=preview_checkbox_changed, variable=preview_var).pack(pady=5)

tk.Label(root, text="Question:").pack(pady=5)
entry_question = tk.Entry(root, width=50)
entry_question.pack(pady=5)

run_button = tk.Button(root, text="Run Prediction", command=run_prediction)
run_button.pack(pady=10)
run_button.bind('<Return>', run_prediction)

predicted_answer = tk.StringVar()

tk.Label(root, text="Predicted answer:").pack(pady=5)
predicted_answer_widget = tk.Entry(root, state='readonly', width=30,  textvariable=predicted_answer)

predicted_answer_widget.pack(pady=10)

# Set some initial text
predicted_answer_widget.insert(0, predicted_answer)

root.mainloop()
