import tweepy, random


team_list = ['rd_tmp', 'te4mn00bs', 'team_jp_', 'RDH4CK4TH0N']

class TwitterAPI:
    def __init__(self):
        consumer_key = "fkjVnvY2TAXZSKVrgiQVvDSvY"
        consumer_secret = "QiXogDZ4Sgbia8eIlBArAYC9gKNGf9qrGxj7MjnA2gXSbZ9Mha"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "3538338736-4F5nyKBVtIbQsmOWuZlLISx3BIdjemb6Wodr7Tj"
        access_token_secret = "bx4HMbyl6qSlqUF395chLBf1Rbo860BS63AyS0aYX10kS"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

    def mention_tweet(self, message, account):
        tweet = message + ' @' + account
        self.api.update_status(status=tweet)

    def autoreply(self):
        mentions = self.api.mentions_timeline(count=1)
        for mention in mentions:
            print mention.text
            self.mention_tweet(mention.text,account)

            print mention.user.screen_name



if __name__ == "__main__":
    twitter = TwitterAPI()
    for value in team_list:
        twitter.mention_tweet("Do you even tweet @{0}", random.choice(team_list))
