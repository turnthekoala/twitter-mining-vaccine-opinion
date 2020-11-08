#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "18196659-DBEYBxdsCHrBL0eUwVZnUx27onK5wJHZBONmsqThM"
access_token_secret = "TnoLLNka4YJue8c7khFYscg4Ari28Xs3YX7UBcb5CXT9d"
consumer_key = "qWR2fyEjOgTeKiUJjN0PmwQlX"
consumer_secret = "0JFag4zj5qunoZHNRHyXUKubs5LhGjWXrWz3K6fP6oApI4dzGI"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	#Changed to look for the words vaccine, vaccination
    stream.filter(track=['vaccine', 'vaccination', 'vaccin'])