# Meme Generator

The Meme Generator is a Python web application that generates memes by combining pictures with quotes. It contains a QuoteEngine module that generates quotes by reading them from various text files in different formats, and a MemeEngine module that generates images by resizing them.

# Installation

Clone the repository to your local machine using "git clone <repository-url>".
Install the required dependencies by running "pip install -r requirements.txt".


# Usage

- Navigate to the "src" directory.
- Run "python app.py" to start the local server.
- Open a web browser and navigate to "http://localhost:5000/" to access the home page.
- Click on the "Generate Meme" button to go to the meme generation form.
- Select a meme image from the dropdown menu, enter the quote and author in the text fields, and click on the "Generate" button.
- The generated meme will be displayed on the next page.

# Project Structure

- The MemeEngine directory contains the meme_engine.py module which is responsible for generating memes by resizing images.
- The QuoteEngine directory contains the quote_engine.py module which is responsible for generating quotes by reading them from various text files.
- The src directory contains the app.py module which is responsible for running the local server and handling HTTP requests, the meme.py module which is responsible for the meme generation process, and the templates directory which contains the HTML templates for the user interface.
- The tree.txt file is a listing of the project directory structure.

# Project structure (tree)
.
├── MemeEngine
│   ├── __init__.py
│   ├── __pycache__
│   └── meme_engine.py
├── QuoteEngine
│   ├── __init__.py
│   └── quote_engine.py
├── src
│   ├── __init__.py
│   ├── _data
│   ├── app.py
│   ├── meme.py
│   └── templates
└── tree.txt

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
