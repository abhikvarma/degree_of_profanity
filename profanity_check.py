import json

'''
contents of "tweets.json":
{
    'user1': "i hate slur1 people",
    'user2': "today was a good day",
    'user3': "why did god create slur1s, slur2s and slur3s ugh",
    'user4': "slur3s dont belong is slur4s' streets",
    'user5': "the presidents new policy is bad news for the slur4s",
}
'''

'''
list of 5 given racial slurs
'''
slurs = ['slur1','slur2','slur3','slur4','slur5']


'''
accpets: list of slurs
adds plural and possessive forms of the slurs to the list
returns: modified list
assuming only the basic words are mentioned in the list
'''
def modify_slurs(slurs):
    updated = []
    for i in slurs:
        updated+=[i,i+"s",i+"'s"]
    return updated


'''
accepts: tweet, list of slurs
returns: the ratio of racial slurs to total no of words
assuming that degree of profanity will be given by this ratio
'''
def rate(string, slurs):
    cnt = 0
    for i in slurs:
        cnt+=string.count(i)
    return (cnt/len(string))

'''
accepts: json file containing the tweets, list of slurs
prints: tweets along with their degree of profanity (rounded off to 2 decimal places)
assuming that all the arguements are passed in the correct form
'''
def checker(tweets_path, slurs):
    tweets = json.load(open(tweets_path))
    slurs = modify_slurs(slurs)
    for tweet in tweets.items():
        print(tweet[1] + '\n-' + tweet[0])
        print(f"degree of profanity: {round(rate(tweet[1],slurs),2):.2f}\n")


tweets_path = "tweets.json"
checker(tweets_path,slurs)