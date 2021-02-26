# discord-feed

> Discord bot that you could use trought reddit


Bot would have multiple subreddits grouped into feeds (categories). Each time bot would be called, it would choose random post from those feeds. It would also use filters when searching trough posts.

User that wants to get those posts would subscribe to feeds. This will be done using webhooks. User would send a message to bot linking a certain webhook with feed. For example:

    User: !update feed-pics <webhook-url>
    Bot: Webhook for feed-pics is successfully saved

Bot will read those messages and store webhooks in database. Next time the bot is ran, it will send posts to those webhooks. 

Since this bot is meant to be content provider and not repost bot, it will be ran only a couple times per day, choosing the best posts from `/hot` page. On average, approx. 2-3 posts will be sent per day.
