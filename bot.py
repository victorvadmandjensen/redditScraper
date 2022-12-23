import praw

# Open file with login info, split into list
f = str(open("login.txt", "r").read())
splitFile = f.split(", ")

# Define Reddit instance
reddit = praw.Reddit(
    client_id = splitFile[0],
    client_secret = splitFile[1],
    user_agent=splitFile[2],
    username=splitFile[3],
    password = splitFile[4]
)

# Define subreddit to scrape
subreddit = "botsRights"

for submission in reddit.subreddit(subreddit).hot(limit=10):
    print(submission.title)