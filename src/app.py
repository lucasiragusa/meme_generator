import random
import os
import tempfile
from flask import Flask, render_template, abort, request
import sys
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from MemeEngine.meme_engine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')

def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv', 
                   ]

    # Use the Ingestor class to parse all files in the quote_files variable
    quotes = []
    for quote_file in quote_files:
        parsed_quotes = Ingestor.parse(quote_file)
        print(f"Parsed {len(parsed_quotes)} quotes from {quote_file}")
        if parsed_quotes is not None:
            quotes.extend(parsed_quotes)

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                imgs.append(os.path.join(root, file))

    print(f"Found {len(imgs)} image files in {images_path}")
    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Select a random image and quote
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

    # 1. Use requests to save the image from the image_url form param to a temp local file.
    image_url = request.form['image_url']
    response = requests.get(image_url)
    img_file = tempfile.NamedTemporaryFile(delete=False)
    img_file.write(response.content)
    img_file.close()

    # 2. Use the meme object to generate a meme using this temp file and the body and author form parameters.
    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(img_file.name, body, author)

    # 3. Remove the temporary saved image.
    os.remove(img_file.name)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
