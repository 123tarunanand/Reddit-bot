import praw
import config
from pycricbuzz import Cricbuzz

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DLSBOT")
    return r


def run_bot(r):
    c = Cricbuzz()
    subreddit = r.subreddit('cricket')
    submission = subreddit.submissions()
    for post in submission:
        if "Match Thread" in post.title:
            print(post.title)
            print(post.selftext)
    #for submission in subreddit.submissions():
    #    title = submission.title
    #    #title = title.split()
        #if(len(title)>2):
            #if title[0] =="Match" and title[1]=="Thread:":
            #    title = submission.title
                #print(title)
                #mindex=-1
                #for match in c.matches():
                #    if match['srs']
                #    desc = match['mchdesc'].split()
                #    if desc[0].lower() in title.lower() or desc[2].lower() in title.lower():
                #        mindex = match['id']
                #        break
                #if mindex ==-1:
                #    print("No link found")
                #    break
                #print(c.livescore(mindex))





r = bot_login()
run_bot(r)
