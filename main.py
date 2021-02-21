import os
import praw

class Crossposter:
    def get_instance(self):
        return praw.Reddit(client_id=os.environ['CLIENT_ID'],
                           client_secret=os.environ['CLIENT_SECRET'], password=os.environ['PWD'],
                           user_agent="testscript", username=os.environ['USER_NAME'])
    def main(self):
        print("hello")