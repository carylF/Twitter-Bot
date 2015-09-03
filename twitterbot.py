import tweepy

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

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("Im a real bot now! @RDH4CK4TH0N")
