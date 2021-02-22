import os
import time

import praw
import re

from discord_webhook import DiscordWebhook,DiscordEmbed

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

    @staticmethod
    def set_flair(submission):
        choices = submission.flair.choices()
        template_id = next(x for x in choices if x["flair_text_editable"])["flair_template_id"]
        submission.flair.select(template_id, 'processed')

    @staticmethod
    def send_webhook(url, sub):
        webhook = DiscordWebhook(url=url)
        embed = DiscordEmbed(title=sub.title, description='r/DiscordFeed', color=242424)
        link = "www.reddit.com" + sub.permalink

        embed.set_author(name='r/DiscordFeed', url='https://www.reddit.com/r/DiscordFeed/')
        if sub.url is not None:
            embed.set_image(url=sub.url)
        embed.set_footer(text=f'Submitted to [r/DiscordFeed]({link}) by u/{sub.author}');
        webhook.add_embed(embed)

        return webhook.execute()


    def main(self):
        r = self.get_instance()
        feed = self.get_feed(r)
        discord_webhooks = self.get_discord_subs()

        for submission in feed:
            print(f'Processing post: ', submission.title)

            if not submission.is_self and submission.link_flair_text != 'processed':
                for wh in discord_webhooks:
                    self.send_webhook(wh, submission)
                self.set_flair(submission)

                time.sleep(1)

        print(self.get_discord_subs())
