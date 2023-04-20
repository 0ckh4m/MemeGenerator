import random
import os
import requests
from flask import Flask, render_template, abort, request

#! DONE: Import your Ingestor and MemeEngine classes
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor, QuoteModel


image_url = 'https://images.ctfassets.net/2y9b3o528xhq/5sXS0Rr3MEr66P5elfYX7P/3728cc2d85c0979cb29d5cb291369038/mentor.jpg'
r = requests.get(image_url) # OK
extension = image_url.split('.')[-1]
body = 'Aaaa bbbbb ccccc ddddd'
author = 'Interesting Author'

tmp = f'./tmp/test-{random.randint(0, 1000000)}.{extension}' # OK 
with open(tmp, 'wb') as img: # OK
    img.write(r.content)

meme = MemeEngine('./tmp/test')
path = meme.make_meme(tmp, body, author)