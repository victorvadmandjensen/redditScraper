import praw 

# Open file with login info, split into list
f = str(open("login.txt", "r").read())
split_file = f.split(", ")

# Define Reddit instance
reddit = praw.Reddit(
    client_id = split_file[0],
    client_secret = split_file[1],
    user_agent=split_file[2],
    username=split_file[3],
    password = split_file[4]
)

def get_reddit():
    return reddit