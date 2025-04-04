from nltk import download                  # download reference datasets from NLTK
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.tokenize import TweetTokenizer, word_tokenize   # module and  for tokenizing strings
import re                                  # library for regular expression operations
from string import punctuation             # for punctuation

##############################################################################

### Select one positive tweet from the Twitter dataset

# downloads sample twitter dataset. uncomment the line below if running on a local machine.
# nltk.download('twitter_samples')

# select the set of positive tweets
all_positive_tweets = twitter_samples.strings('positive_tweets.json')

# select one positive tweet
raw_tweet = all_positive_tweets[2277]
print(f"""
raw:
{raw_tweet}""")

##############################################################################

### Task 1: Convert the tweet to lowercase
### hint: .lower() method

# tweet =  # change this to convert to lowercase

tweet = raw_tweet.lower()
print(f"""
lowercase:
{tweet}""")

##############################################################################

### Task 2: Remove hyperlinks
### hint: use regex to remove hyperlinks

# tweet =  # change this to remove hyperlinks

tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
print(f"""
remove hyperlinks:
{tweet}""")

##############################################################################

### Task 3: Tokenisation

### Task 3.0. What is tokenisation?
# See slides


### Task 3.1. Tokenise the tweet using the TweetTokenizer class

# instantiate tokenizer class
tweettokenizer = TweetTokenizer(preserve_case=False,
                           strip_handles=True,
                           reduce_len=True)

# tweet =  # change this to use the TweetTokenizer class

tweet = tweettokenizer.tokenize(tweet)
print(f"""
TweetTokenizer:
{tweet}""")

##############################################################################

### Task 4: Stopwords

### Task 4.0. What is a stopword?
# See slides


### Task 4.1. Remove stopwords

# download the stopwords from NLTK
download('stopwords')

#Import the english stop words list from NLTK
stopwords_english = stopwords.words('english') 
print(f"""
stopwords:
{stopwords_english}""")

# tweet =  # change this to remove stopwords

tweet = [word for word in tweet if word not in stopwords_english] # change this to remove stopwords
print(f"""
remove stopwords:
{tweet}""")


##############################################################################

### Extra Task 1: After lowercase and removing hyperlink, tokenise the tweet using the NLTK word_tokenize method

## download the punkt tokenizer from NLTK
download('punkt_tab')

# tweet =  # change this to convert to lowercase
# tweet =  # change this to remove hyperlinks
# tweet =  # change this to choose the word_tokenize tokeniser
tweet = raw_tweet.lower()
tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
tweet_word_tokenize = word_tokenize(tweet)
print(f"""
word_tokenize:
{tweet_word_tokenize}""")

### What is the difference between the TweetTokenizer class and the word_tokenize method?
# TweetTokenizer uses a different algorithm to word_tokenize.
# For example, TweetTokenizer will split on hashtags and mentions, while word_tokenize will not.

##############################################################################

### Extra Task 2: Research tokenisation
### hint: this may help: https://neptune.ai/blog/tokenization-in-nlp

### What are the different methods of tokenisation?
# See https://neptune.ai/blog/tokenization-in-nlp

### Choose a different language and research how text preprocessing is done for that language.
### hint: choose a language with a different alphabet or script from English.
# Article for Chinese characters:
# https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00560/116047/Sub-Character-Tokenization-for-Chinese-Pretrained

##############################################################################

### Extra Task 3: Experiment with stemming and lemmatisation to understand the difference

### What is stemming?
# See slides

### What are the different approaches to stemming?
# See https://www.ibm.com/think/topics/stemming

from nltk.stem import PorterStemmer
stemmer = PorterStemmer() 
stemmer.stem("was")


### What is lemmatisation?
# See slides

### What is part of speech tagging and why is it important for lemmatisation?
# https://www.youtube.com/watch?v=WQYt3DRLpuQ
# https://codefinity.com/courses/v2/c68c1f2e-2c90-4d5d-8db9-1e97ca89d15e/026d736a-1860-4e3e-a915-b926ca2d9ed8/b9469e7f-9eb7-40ce-8941-2fb946782907

### What are the different approaches to lemmatisation in Python?
# https://www.machinelearningplus.com/nlp/lemmatization-examples-python/

download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("was", pos="v")

##############################################################################
 #end of file