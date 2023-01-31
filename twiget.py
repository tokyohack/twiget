import sys
import time

import datetime
import tweepy
from archiveph import archiveph

consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        id_ = status.id
        sc_n = status.user.screen_name
        print('\n' + 'twiTime' + str(datetime.datetime.now()))
        if hasattr(status, 'retweeted_status'):
            try:
                tweet = status.retweeted_status.extended_tweet['full_text']
                print('RTFULL' * 4)
                print(tweet)
                print('RTFULL_https://twitter.com/' + str(sc_n) + '/status/' + str(id_))
            except:
                tweet = status.retweeted_status.text
                print('RTexcept' * 4)
                print(tweet)
                print('RTexcept_https://twitter.com/' + str(sc_n) + '/status/' + str(id_))
        else:
            try:
                tweet = status.extended_tweet['full_text']
                print('FULLL' * 4)
                print(tweet)
                print('FULLL_https://twitter.com/' + str(sc_n) + '/status/' + str(id_))
                AR = archiveph()
                AR.archivephNow('https://twitter.com/' + str(sc_n) + '/status/' + str(id_))
            except AttributeError:
                tweet = status.text
                print('EXCEPT' * 4)
                print(tweet)
                print('EXCEPT_https://twitter.com/' + str(sc_n) + '/status/' + str(id_))
                AR = archiveph()
                AR.archivephNow('https://twitter.com/' + str(sc_n) + '/status/' + str(id_))

    def on_error(self, status_code):
        if status_code == 420:
            time.sleep(5)
            return

    def on_exception(self, exception):
        print(exception)
        print('STOP')
        time.sleep(5)
        start_stream()
        return


def start_stream():
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(follow=['88846085'], is_async=True, stall_warnings=True)  # この例ではYahooNewsTopicsがツイートした時やリプライ貰った時をトリガーにアーカイブする。
    return 1


if __name__ == '__main__':
    print('LOOP_STR_' + str(datetime.datetime.now()))
    sys.exit(start_stream())
