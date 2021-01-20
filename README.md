# OnlinePollSubmission
How to use a Python script to enter in entries to an online poll.

Created this script for some friends to help them win an online contest for a school project. 

## Obstacles
  + **Time** - selenium may run faster than your webbrowser.
  + **Google reCAPTCHA** - Google has limitations on automating the web and clicking submit.
  + **Finding the element** - you may have to try a few different ways to locate the element. In my script I used find_element_by_id.
                          Use this link for other ways to locate the element. (https://selenium-python.readthedocs.io/locating-elements.html)
  + **Submission intervals** - Don't want to enter in to many submissions to quickly. 
  
## Setup - Packages
  - **Selenium (https://selenium-python.readthedocs.io/)
  - **Chromedriver_autoinstaller (https://chromedriver.chromium.org/getting-started)
  - **Time (https://docs.python.org/3/library/time.html)
  - **Pandas (https://pandas.pydata.org/)
  - **Random (https://docs.python.org/3/library/random.html)
