# redditScraper - reddit data for controversy mapping!

This is redditScraper, a script which pulls data from a subreddit and saves it in .xlsx-files. This is useful for conducting controversy mapping based on the Master's programme in Techno-Anthropology's Mapping Controversies course and material herein (found at https://jacomyma.github.io/mapping-controversies/). By default, it scrapes submission titles from the subreddit botsRights, to help map the discourse on this subreddit. 

## Setup
The scraper uses Python 3.10.9, so if you do not have that, you need to install it. To get it running you have to:
* Create an application in your reddit settings.
* Create a file called "login.txt" with the data from your application in the form of "client_id, client_secret, user_agent, username, password". This will be loaded into login.py.
* Install the following Python modules on your computer: praw, pathlib, openpyxl, xlsxwriter. Write "pip install XYZ", where XYZ is the name of the module.

In bot.py, you can change the subreddit you want, as well as the amount of posts.

## Running the scraper
To run the scraper, you do the following:
1. Navigate into the directory of the scraper on your computer in your IDE of choice (I use Visual Studio Code).
2. You run the post_bot.py script, which generates an Excel file to get the top 1000 posts on a subreddit (which you can change in this script as well).
3. You run the comment_bot.py script, which uses the Excel file for posts to scrape all comments related to the posts, saving this in a new Excel file.
    1. NOTE: This will take a LONG time, ~15 minutes to fetch ~13,000 posts. Be patient here!
