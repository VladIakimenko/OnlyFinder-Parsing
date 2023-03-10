# Technical task:

Collect data from [onlyfinder.com](https://onlyfinder.com/new-free/profiles)
around 1000 accounts and return a .json file with the following content:

    'name': account name  
    'count': likes amount  
    'link': link to account at onlyfans.com
    
# System requirements
Chromium browser must be installed to operate the Undetected ChromeDriver package.
Please install it as per your system requirements:

LINUX:
	sudo pacman -S chromium (This line works for Manjaro dist. Use your own package manager)

WINDOWS:
	Please visit [Chromium official website](https://www.chromium.org/getting-involved/download-chromium)

# Application Composition
### main.py
The entry point to the application. This is the main module that parses the raw html
received from parser.py and specifies where and what data to collect.
### parser.py
An independent module that may be used for similar tasks separately. It is based on
Undetected ChromeDriver library intended to pass through websites' robots-protection
protocols.
During initialization, it opens the browser, and then the .parse method reads
the page html (link given as argument) by continuously scrolling it down to the bottom for a given number of seconds (timer parameter).
Then method returns page's raw html as str object.
Parsed page is saved to local machine at *data/parsed_page.html*.  
*data/start_from.lnk* is a file where the contents of the browser's address bar is
recorded at the end of each session.
### config.py
These are the app's constants such as url for parsing and paths to data files.
### requirements.txt
All necessary packages are listed in requirements.txt.

# Operation Manual
- Engage the venv  
Create a virtual environment as per instructions for your system. Packages required to run the app are listed in requirements.txt.  
NOTE: Chromium browser needs to be installed separetely (instructions given at System requirements)

Once activated:

    pip install -r requirements.txt

- Run **main.py** in venv
- Wait untill the browser opens  
*This may take a while due to peculiarities of Undetected ChromeDriver package.*
- Set the time limit for a session  
*The browser will scroll the page down and read the data for the number of seconds
specified in the dialogue. Then the app parses and saves the result in a .json file.
Every new session continues from the place where the previous session stopped. The
app maintains that no repeated data is recorded to result.json.*
- Read the report
- Restart the session or quit

# Product
**result.json** is saved to the root directory of the project ready for further use.
