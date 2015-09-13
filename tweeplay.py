import tweepy,json

# Authentication details. To  obtain these visit dev.twitter.com

consumer_key = 'h3mSe5fRU0wmXuJbcbQ8I5uUM'
consumer_secret = 'IhLlX9GSu1a4oQqDKPPOtRnwRMlT8e8Ndgq1tL14e0rBJx3lf6'
access_token = '125627409-tjCdFyi9VDGi7Doug0Adt2A5uxlyDSxO4Z8YQMUv'
access_token_secret = 'zjv0qipatsyeGnG5kGLcMzlQpfFBcP1ZvpFxQ4URpULBr'

f = open('Music_List.txt', 'w+')
list_dict={}

# This is the listener, resposible for receiving data

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
	global lumos
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        string =  '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        empty = ''
	newtab = '\t'
	need = decoded['text'].encode('ascii','ignore')
	need=need.replace('#tweeplay ','')
	need=need.replace(' #tweeplay','')
	if need in list_dict:
		list_dict[need]+=1
	else:
		list_dict[need]=1
	
	f.write(need+newtab+list_dict[need])
	lumos += 1
	return True
    def on_error(self, status):
        print status
	return True
def main():
        l = StdOutListener()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        # There are different kinds of streams: public stream, user stream, multi-user streams
        # In this example follow #programming tag
        # For more details refer to https://dev.twitter.com/docs/streaming-apis
        stream = tweepy.Stream(auth, l)
        stream.filter(track=['#tweeplay'])
if __name__ == '__main__':
    try:
	main()	
    except KeyboardInterrupt:
	for words in list_dict:
		print words + " : " + str(list_dict[words])
        print '\nGoodbye!\n'
	f.close()
