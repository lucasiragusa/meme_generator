# Meme Generator Introduction
The Meme Generator is a Python web application that generates memes by combining pictures with quotes. It contains a QuoteEngine module that generates quotes by reading them from various text files in different formats, and a MemeEngine module that generates images by resizing them.

# Installation
Clone the repository to your local machine using "git clone <repository-url>".
Install the required dependencies by running "pip install -r requirements.txt".

# Usage 1 - Flask app
- Navigate to the "src" directory.
- Run "python app.py" to start the local server.
- Open a web browser and navigate to the identified local host to access the home page.
- Click on the "Random" button to go to generate a random meme. 
- Click on the "Creator" button to use the meme generating page.  
- The generated meme will be displayed on the next page.

# Usage 2 - CLI
- Navigate to the "src" directory.
- Run the "meme.py" with three optional arguments (--body, --author, --path)  
- --body: The body of the quote to use in the meme. If this argument is not provided, a random quote will be used.
- --author: The author of the quote to use in the meme. If this argument is not provided, the author will be set to "Unknown".
- --path: The path to the image file to use as the background of the meme. If this argument is not provided, a random image will be used.

# Project Structure
- The MemeEngine directory contains the meme_engine.py module which is responsible for generating memes by resizing images.
- The QuoteEngine directory contains the quote_engine.py module which is responsible for generating quotes by reading them from various text files.
- The src directory contains the app.py module which is responsible for running the local server and handling HTTP requests, the meme.py module which is a CLI interface, and the templates directory which contains the HTML templates for the user interface.

# Project structure (tree)
.
├── MemeEngine
│   ├── __init__.py
│   ├── __pycache__
│   └── meme_engine.py
├── QuoteEngine
│   ├── CsvIngestor.py
│   ├── DocxIngestor.py
│   ├── Ingestor.py
│   ├── IngestorInterface.py
│   ├── PdfIngestor.py
│   ├── QuoteModel.py
│   ├── TxtIngestor.py
│   ├── __init__.py
│   └── __pycache__
├── README.md
├── __init__.py
├── meme
│   ├── bin
│   ├── include
│   ├── lib
│   └── pyvenv.cfg
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   ├── _data
│   ├── _tmp
│   ├── app.py
│   ├── fontsg
│   ├── meme.py
│   ├── static
│   ├── templates
│   └── tmp
└── static

# Dependencies

certifi==2022.12.7
charset-normalizer==3.0.1
click==8.1.3
Flask==2.2.3
idna==3.4
importlib-metadata==6.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
lxml==4.9.2
MarkupSafe==2.1.2
numpy==1.24.2
pandas==1.5.3
Pillow==9.4.0
python-dateutil==2.8.2
python-docx==0.8.11
pytz==2022.7.1
requests==2.28.2
six==1.16.0
urllib3==1.26.14
Werkzeug==2.2.3
zipp==3.14.0
