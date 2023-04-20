import random
import os
import requests
from flask import Flask, render_template, abort, request

#! DONE: Import your Ingestor and MemeEngine classes
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                './_data/DogQuotes/DogQuotesDOCX.docx',
                './_data/DogQuotes/DogQuotesPDF.pdf',
                './_data/DogQuotes/DogQuotesCSV.csv']

    #* DONE: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    #* DONE: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
            imgs = [os.path.join(root, name) for name in files] # ? Is this right? 

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    #* DONE:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    extension = image_url.split('.')[-1]




    r = requests.get(image_url) # OK
    
    tmp = f'./tmp/{random.randint(0, 1000000)}.{extension}' # OK 
    with open(tmp, 'wb') as img: # OK
        img.write(r.content)
    # img = open(tmp, 'wb').write(r.content)
    # img.close()

    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    
    # 3. Remove the temporary saved image.
    try:
        path = meme.make_meme(tmp, body, author)
    except:
        raise Exception('could not generate meme')
    
    
    # TODO: use os module to remove the tmp file
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()