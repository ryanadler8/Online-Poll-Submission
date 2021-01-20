# Online Poll Submission
How to use a Python script to enter in entries to an online poll.
Created this script for some friends to help them win an online contest for a school project. 
## Setup - Libraries
  - **Selenium** (https://selenium-python.readthedocs.io/)
  - **Chromedriver_autoinstaller** (https://chromedriver.chromium.org/getting-started)
  - **Time** (https://docs.python.org/3/library/time.html)
  - **Pandas** (https://pandas.pydata.org/)
  - **Random** (https://docs.python.org/3/library/random.html)

## Obstacles
  + **Time** - selenium may run faster than your webbrowser.
  + **Google reCAPTCHA** - Google has limitations on automating the web and clicking submit.
  + **Finding the element** - you may have to try a few different ways to locate the element. In my script I used find_element_by_id.
                          Use this link for other ways to locate the element. (https://selenium-python.readthedocs.io/locating-elements.html)
  + **Submission intervals** - Don't want to enter in to many submissions to quickly. 
  
## Explanation of Code
Import libraries

![image](https://user-images.githubusercontent.com/55520621/105122391-1ea1f900-5aa4-11eb-80b6-33d49d74ca88.png)

Here we are calling in our excel file and telling python what sheet we would like to read from. Sheet1 is just the default, but it can be called whatever you choose.

![image](https://user-images.githubusercontent.com/55520621/105122731-c3bcd180-5aa4-11eb-8bff-c31f2f9b5f77.png)

Next, we are creating a for loop to iterate through the rows in our excel doc. I started off using index, rows in the beginning just to keep track of what row I was iterating through in my excel doc. I kept index in my for loop for testing purposes when using the print function, but it is not needed. This could be helpful. After that we are calling in the chrome driver and than using the driver to get our desired webaddress. I used time.sleep inorder to let chrome load before moving to the next step. You will see this used alot throughout my script. 

![image](https://user-images.githubusercontent.com/55520621/105123275-c0761580-5aa5-11eb-97cf-631726024d5a.png)

This next screenshot is where we start to automate the webpage. In my code where it says ID_NAME_1 and ID_NAME_2 this is where we need to inspect the webpage to get the ID value. To do so, we will right click on the text box and click inspect, this should be at the bottom. Once that is selected a window will appear on the right with HTML code. I found it better to right click again on the text box to make sure we are looking at the correct ID. If you run into challenges with this please use this link for more info, https://selenium-python.readthedocs.io/.  After the ID is figured out I again used time.sleep to let chrome catch up. Then I used the send_keys to get the information from my excel doc. The column name is where you will be iterating down the excel sheet. I did that twice, the first column contained a list of names and the second column had a list of emails. 

![image](https://user-images.githubusercontent.com/55520621/105124079-5a8a8d80-5aa7-11eb-978c-9181f4a6ff01.png)

To make sure that the entries all weren't going to one team I created a list that contained the same team three times and the least likely team to win once. I did this to make sure the team I wanted to win was selected most of the time, but not every time. 

![image](https://user-images.githubusercontent.com/55520621/105124919-2adc8500-5aa9-11eb-91f3-9baa5c261f57.png)

After selecting the team I wanted to win. I did something similar with the rest of the teams. At the end of each selection I would remove the team that was picked from the list to make sure that it wasn't being duplicated. I did this multiple times for all the selections. 

![image](https://user-images.githubusercontent.com/55520621/105125360-2fee0400-5aaa-11eb-8f7f-623b6f9f288d.png)

Lastly, I selected the select button, printed out the name, email and the sections for each "person" and added in some time.sleeps for the script to run again in the for loop. I had trouble with Google reCAPTCHA when having the script run to quickly.

![image](https://user-images.githubusercontent.com/55520621/105125561-abe84c00-5aaa-11eb-8c5f-fb439c4980d4.png)
