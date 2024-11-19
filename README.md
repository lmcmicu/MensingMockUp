# Installation

# Flat file installation

1. Go to https://github.com/lmcmicu/MensingMockUp/releases in your browser, download the file: `mensing_web_exhibit_example-<date>.zip` associated with the most recent release to a folder on your computer, and unzip the file. Note that you do not need to download `static.zip`.
2. Open the file `index.html` in your favourite browser.
3. That's all.

# Server Installation

See this page for instructions on setting up Python for MacOS: https://docs.python.org/3/using/mac.html

To install and run the server:

1. `git clone https://github.com/lmcmicu/MensingMockUp`
1. `python3 -m venv .venv`
2. `. .venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. Download the file `static.zip` from the [latest release page](https://github.com/lmcmicu/MensingMockUp/releases).
4. `unzip static.zip` in the root folder of the repository.
4. `FLASK_DEBUG=1 ./server.py`
5. Navigate to this page in your favourite browser: http://127.0.0.1:5000/
