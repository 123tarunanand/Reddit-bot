import praw
import config

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DLSBOT")
    return r


def run_bot(r):
    subreddit = r.subreddit('cricket')
    for submission in subreddit.submissions:
        if "Match Thread" in submission.title:
		
    return i

r = bot_login()
print("There are ",run_bot(r)," instances of dragon")
