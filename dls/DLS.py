import praw
import config
#from pycricbuzz import Cricbuzz

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DLSBOT")
    return r


def run_bot(r):
    #c = Cricbuzz()
    subreddit = r.subreddit('cricket')
    submission = subreddit.submissions()
    for post in submission:
        if "Match Thread" in post.title:
            print(post.title)
            print(post.selftext)






r = bot_login()
run_bot(r)
