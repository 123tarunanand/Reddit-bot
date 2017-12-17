import praw
import config
import pandas as pd
#from pycricbuzz import Cricbuzz

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DLSBOT")
    return r


def run_bot(r):
    DLSTABLE = pd.read_csv('DLSTABLE.csv')
    #c = Cricbuzz()
    #subreddit = r.subreddit('cricket')
    #submission = subreddit.submissions()
    #for post in submission:
        #if "Match Thread" in post.title:
            #print(post.title)
            #print(post.selftext
    inital_over = 50
    team1_score = 230
    team2_initial_target = 300
    team2_initial_overs = 40
    for i in range(len(DLSTABLE)):
        if DLSTABLE['O'][i] == team2_initial_overs:
            break
    team2_initialres = float(str(round(DLSTABLE['W0'][i],2)))
    team1_resources = float(str(round(1/((team2_initial_target-1)/(team1_score*team2_initialres)),2)))
    current_over








r = bot_login()
run_bot(r)
