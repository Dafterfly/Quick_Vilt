# Quick_Vilt
A CLI and GUI for using the [Vision-and-Language Transformer (ViLT) model by 
dandelin](https://huggingface.co/dandelin/vilt-b32-finetuned-vqa) for visual question answering (answering questions based on an image)

## Installation
1. Clone this repo
  ```shell
  git clone https://github.com/Dafterfly/Quick_Vilt_Cli.git
```
2. Navigate into the repo
  ```shell
  cd Quick_Vilt_Cli
  ```
3. Install requirements
  ```shell
  pip install -r requirements.txt
  ```
You are now ready to use the script

## Usage

Using this image from the COCO dataset as an example
   ![5868604848_680662062a_z (Phone)](https://github.com/Dafterfly/Quick_Vilt_Cli/assets/17124333/bf724b2f-a150-4972-ab0e-28e5489b01e1)


Direct url: https://farm4.staticflickr.com/3076/5868604848_680662062a_z.jpg

COCO dataset link: https://cocodataset.org/#explore?id=18633

Note: the first time that you run either the CLI or GUI, the ViLT model will automatically be downloaded onto you computer. This download is 449 MB.

### CLI

To use the command line interface script call the script and pass these 2 arguments:
1. ```--image``` or ```i``` can either be an image url from the web or a path stored locally
2. ```--question``` or ```q``` is the question you'd like to ask
3. Examples

   

 * Image from url
```shell
python quick_vilt.py -i https://farm4.staticflickr.com/3076/5868604848_680662062a_z.jpg -q "how many dogs are there?"
```
Output
```shell
  Predicted answer: 2
```
  * Image from local storage
```shell
python quick_vilt.py -i 5868604848_680662062a_z.jpg -q "how many dogs are there?"
```
Output
```shell
Predicted answer: 2
```

### GUI
Alternatively, you can use the graphical user interface by calling
```shell
python quick_vilt_gui.py
```

You can browse for the image on the internet or local file storage using the file dialog that appears when you click 'Browse' or you can type it directly into the box.

You can tick or untick the 'Preview image' box to show or hide the selected image

You can click 'Run Prediction' to answer the question

![image](https://github.com/Dafterfly/Quick_Vilt/assets/17124333/165e5446-d712-4e91-8d34-8348c6d9afbf)


