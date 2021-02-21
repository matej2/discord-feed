import os
import praw
import re


class Crossposter:

    @staticmethod
    def get_instance():
        return praw.Reddit(client_id=os.environ['CLIENT_ID'],
                           client_secret=os.environ['CLIENT_SECRET'], password=os.environ['PWD'],
                           user_agent="Mention bot", username=os.environ['USER_NAME'])

    @staticmethod
    def get_discord_subs():
        subs = os.environ['SUB']
        re.sub('\\s+', '', subs)
        return subs.split(",")

    @staticmethod
    def get_mentions(reddit):
        return reddit.inbox.mentions(limit=25)

    @staticmethod
    def get_feed(reddit):
        return reddit.subreddit("DiscordFeed").new()

    def set_flair(self, submission):
        choices = submission.flair.choices()
        template_id = next(x for x in choices if x["flair_text_editable"])["flair_template_id"]
        submission.flair.select(template_id, 'processed')


    def main(self):
        r = self.get_instance()
        feed = self.get_feed(r)
        for submission in feed:
            print(f'Processing post: ', submission.title)
            self.set_flair(submission)

        print(self.get_discord_subs())
