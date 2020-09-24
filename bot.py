# coding: latin-1
import random
import tweepy
import time

#APIs da conta developer do Twitter
CONSUMER_KEY =  ''
CONSUMER_SECRET = ''
ACCES_KEY = ''
ACESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACESS_SECRET)

api = tweepy.API(auth)

# arquivo para armazenar último id do Tweet recebido
FILE = 'last_seen_id.txt'

# funções para ler e escrever no arquivo de IDs
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


# função para responder tweets
def reply_to_tweets():
    print("respondendo tweets...")

    last_seen_id = read_last_seen_id(FILE)

    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode = 'extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        write_last_seen_id(last_seen_id, FILE)
        
        # lista com palavras aleatórias
        randomList = ['Hello, World!', 'Hello, i am a bot build using Python :)']
        gen = random.choice(randomList)

        if '@username' in mention.full_text.lower():
            api.update_status('@'+mention.user.screen_name + str(genRandomPhrase), mention.id)

# fica rodando 
while True:
    reply_to_tweets()
    time.sleep(15)
