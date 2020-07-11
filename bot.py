# coding: latin-1
import random
import tweepy
import time

#insert the API of twitter developer account 
CONSUMER_KEY =  ''
CONSUMER_SECRET = ''
ACCES_KEY = ''
ACESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACESS_SECRET)

api = tweepy.API(auth)

#receive the name of txt file
FILE = 'last_seen_id.txt'

#functions to read and write the id file
def read_last_seen_id(file):
    f_read = open(file, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def write_last_seen_id(last_seen_id, file):
    f_write = open(file, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


##function to reply tweets
def reply_to_tweets():
    print("respondendo tweets...")

    ##primeiro tweet é 1282000418936172545
    last_seen_id = read_last_seen_id(FILE)

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode = 'extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        write_last_seen_id(last_seen_id, FILE)
        
        #generate a random list
        randomList = ['NUM VAI DAAA', 'BICIPIS', ' CANHÃO CABEDIPINTO', 'EDILSON JOGADÔ', 'PÃÃÃO', 'JOGADOZINHO PÉ DI GRILO', 'CABELO DI BONECA', 'O MARAVILHA TA CERTO', 'SEIS NAO JOGA NADA', 'ZÉ RUELA DISGRAÇADO', 'EU NUM JOGO MAIS', 'TOMANOCU VELOSO', 'RAÍ VEIO DA EM MIM EU DEI NA COSTELA DO RAÍ', 'O NEYMAR', 'TITE CE QUÉ VIRA PASTOR', 'GOLEIRO MÃO DE PAU']
        gen = random.choice(randomList)

        if '@botdoneto1' in mention.full_text.lower():
            api.update_status('@'+mention.user.screen_name + str(genRandomPhrase), mention.id)

#keeps working 
while True:
    reply_to_tweets()
    time.sleep(15)