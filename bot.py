import praw
from openpyxl import Workbook
import login

# Get Reddit instance from login.py
reddit = login.get_reddit()

# Define subreddit to scrape
subreddit = "botsRights"

# Create empty list of data
data_list = []

for submission in reddit.subreddit(subreddit).hot(limit=10):
    data_list.append(submission.title)

print(data_list)

# Define workbook to write to and file
wb = Workbook()
destination = "python_data.xlsx"
ws1 = wb.create_sheet(title="test_data")

# Iterate over items in data_list and add the title to the Excel sheet
for data_item in range(1, len(data_list)):
    ws1.cell(column=1, row=data_item).value= data_list[data_item]

# Save the workbook
wb.save(filename=destination)