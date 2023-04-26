# MemeGenerator

MemeGenerator is a web-based and a command line application that allows users to create custom memes using a simple and intuitive interface.

## Table of Contents

- [Installation](https://chat.openai.com/c/c529f97c-1b58-486b-b146-b5dc112c4c36#installation)
- [Usage](https://chat.openai.com/c/c529f97c-1b58-486b-b146-b5dc112c4c36#usage)

## Installation

To set up and install the MemeGenerator project on your local machine, follow these steps:

1. Clone the repository

```bash
git clone https://github.com/0ckh4m/MemeGenerator.git
```

2. Navigate to the project directory

```bash
cd MemeGenerator
```

3. Install the required dependencies

```bash
pip install -r requirements.txt
```

4. Start Flask server

```bash
flask run --host 0.0.0.0 --port 3000
```

5. Installing Xpdf tool - necessary for the PDFIngestor module

```bash
sudo apt-get install -y xpdf
```

## Usage

After setting up the project, you can access the MemeGenerator application at `[http://localhost:3000](http://localhost:3000)` or through the command line. 

Using the web app:

To create a custom meme, follow these steps:

1. Upload your an image.
2. Add your desired quote and author using the provided input fields.

You can also generate a meme selecting the Random option. It will select a random image, text, and author.

Using the command line:

If you run [meme.py](http://meme.py) without any arguments it will generate a meme using a random image and a random text. You can specify the following options:

—body : the quote text

—author : the autor of the quote

—path : path to the image file that will be used in the meme

The application can process CSV, DOCX, PDF , and TEXT files to extract quotes and authors. To use this functionality you can place your files in the _data/DogQuotes folder. You can also use your own images when generating random memes. For this you must place your images in the folder _data/photos/dog.
