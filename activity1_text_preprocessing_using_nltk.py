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

##############################################################################

### Task 2: Remove hyperlinks
### hint: use regex to remove hyperlinks

# tweet =  # change this to remove hyperlinks

##############################################################################

### Task 3: Tokenisation

### Task 3.0. What is tokenisation?
#
#
#


### Task 3.1. Tokenise the tweet using the TweetTokenizer class

# instantiate tokenizer class
tweettokenizer = TweetTokenizer(preserve_case=False,
                           strip_handles=True,
                           reduce_len=True)

# tweet =  # change this to use the TweetTokenizer class

##############################################################################

### Task 4: Stopwords

### Task 4.0. What is a stopword?
# answer here
# 
# 


### Task 4.1. Remove stopwords

# download the stopwords from NLTK
download('stopwords')

#Import the english stop words list from NLTK
stopwords_english = stopwords.words('english') 
print(f"""
stopwords:
{stopwords_english}""")

# tweet =  # change this to remove stopwords


##############################################################################

### Extra Task 1: After lowercase and removing hyperlink, tokenise the tweet using the NLTK word_tokenize method

## download the punkt tokenizer from NLTK
download('punkt_tab')

# tweet =  # change this to convert to lowercase
# tweet =  # change this to remove hyperlinks
# tweet =  # change this to choose the word_tokenize tokeniser


### What is the difference between the TweetTokenizer class and the word_tokenize method?
# answer here
# 
# 

##############################################################################

### Extra Task 2: Research tokenisation
### hint: this may help: https://neptune.ai/blog/tokenization-in-nlp

### What are the different methods of tokenisation?
# answer here
#
#

### Choose a different language and research how text preprocessing is done for that language.
### hint: choose a language with a different alphabet or script from English.
# answer here
#
#

##############################################################################

### Extra Task 3: Experiment with stemming and lemmatisation to understand the difference

### What is stemming?
# answer here
#
#

### What are the different approaches to stemming?
# answer here
#
#

from nltk.stem import PorterStemmer
stemmer = PorterStemmer() 
stemmer.stem("was")


### What is lemmatisation?
# answer here
#
#

### What is part of speech tagging and why is it important for lemmatisation?
# answer here
#
#

### What are the different approaches to lemmatisation in Python?
# answer here
#
#

download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("was", pos="v")

##############################################################################
 #end of file