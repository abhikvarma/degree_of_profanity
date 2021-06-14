# degree_of_profanity

## to run
execute `profanity_checker.py`

by default it looks for a `tweets.json` in the same director\
if you want to run it on your own json file,\
modify the `tweets_path` var

if you want to change the list of racial slurs to include\
modify the `slurs` list


## format of json file
the json file has to be a dictionary with keys as the user name and\
as values as the corresponding tweet\
an example:
```
{
    'user1': "i hate slur1 people",
    'user2': "today was a good day",
    'user3': "why did god create slur1s, slur2s and slur3s ugh",
    'user4': "slur3s dont belong is slur4s' streets",
    'user5': "the presidents new policy is bad news for the slur4s",
}
```