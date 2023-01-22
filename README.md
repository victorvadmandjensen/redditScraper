# redditScraper - reddit data for controversy mapping!

This is redditScraper, a script which pulls data from a subreddit and saves it in .xlsx-files. This is useful for conducting controversy mapping based on the Mapping Controversies course and material herein (found at https://jacomyma.github.io/mapping-controversies/). By default, it scrapes submission titles from the subreddit botsRights, to help map the discourse on this subreddit. 

## Setup
The scraper uses Python 3.10.9, so if you do not have that, you need to install it. To get it running you have to:
* Create an application in your reddit settings.
* Create a file called "login.txt" with the data from your application in the form of "client_id, client_secret, user_agent, username, password". This will be loaded into login.py.
* Install the following Python modules on your computer: praw, pathlib, openpyxl, xlsxwriter.

In bot.py, you can change the subreddit you want, as well as the amount of posts.

## Running the scraper
To run the scraper, you just navigate into the directory of the scraper on your computer. Then you run the script, and it will generate the right .xlsx-file. The system has not been tested on macOS or Linux.
