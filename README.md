# Quick_Vilt
A little CLI for using the [Vision-and-Language Transformer (ViLT) model by 
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
To use the script call the script can pass these 2 arguments:
1. ```--image``` or ```i``` can either be an image url from the web or a path stored locally
2. ```--question``` or ```q``` is the question you'd like to ask
3. Examples

   Using this image from the COCO dataset as an example
   ![5868604848_680662062a_z (Phone)](https://github.com/Dafterfly/Quick_Vilt_Cli/assets/17124333/bf724b2f-a150-4972-ab0e-28e5489b01e1)


Direct url: https://farm4.staticflickr.com/3076/5868604848_680662062a_z.jpg

COCO dataset link: https://cocodataset.org/#explore?id=18633

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
