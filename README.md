# discord-feed

This will basically be a reddit to discord repost bot. First, a subreddit will be created. There would be pinned post with feed categories from which user could choose from. Then a bot will be added to this sub. User will first send a discord webhook link for a certain feed category, defined in pinned post.

Bot will read those links, test them and add them to database. Then user will repost submission to our sub. Bot will read this submission, and find feed category from post title / tag. Then, the bot will send this post to defined webhooks.

Sub will have anti-flood bot that would prevent spam. It would also have admin post approval at first, and then we could instead use advanced keyword filters.
