# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import libraries
import nltk, sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
#
#
#
#
#
tweets_df = pd.read_csv('Lab 2/Data/oct_delta.csv') # read in twitter data

tweets_df['char_count'] = tweets_df['text'].apply(len) # create new column variable

tweets_df['char_count'].plot.hist(bins = 20)
plt.show()
#
#
#
#
cv = CountVectorizer() # begin instance of count vectorizer
tf = cv.fit_transform(tweets_df['text']) 
tf_feature_names = cv.get_feature_names_out()

tf_df = pd.DataFrame(tf.toarray(), columns = tf_feature_names) # create df

tf_df.sum().sort_values(ascending = False).head(20).plot.bar() # create a bar plot
plt.show()
#
#
#
#
tfidf = TfidfVectorizer() # create an instance of class
tfidf_matrix = tfidf.fit_transform(tweets_df['text'])
tfidf_feature_names = tfidf.get_feature_names_out()

tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), # convert to df
                        columns=tfidf_feature_names) 

tfidf_df.sum().sort_values(ascending=False).head(20).plot.bar() # create bar plot
plt.show()
#
#
#
#
tf_df.sum().sort_values(ascending=False).head(20) # see most common 20 words
#
#
#
tf_df.sum().sort_values(ascending=False).head(20).plot.bar() # create a bar plot
plt.show()
#
#
#
#
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2)) # create an instance of class
bigram_matrix = bigram_vectorizer.fit_transform(tweets_df['text'])
#
#
#
#
# create a function to create a plot of most common words
def plot_most_common_words(count_data, count_vectorizer, top_n=20):
  words = count_vectorizer.get_feature_names_out()
  total_counts = count_data.sum(axis=0).tolist()[0]
  count_dict = (zip(words, total_counts))
  count_dict = sorted(count_dict, key=lambda x:x[1], reverse=True)[0:top_n]
  words, counts = zip(*count_dict)
  plt.figure(figsize=(10, 5))
  plt.bar(words, counts)
  plt.xticks(rotation=45)
  plt.show()

plot_most_common_words(tf, cv)
#
#
#
#
#
nltk.download('gutenberg') # download gutenberg package
from nltk.corpus import gutenberg # import gutenberg
# compile austen texts with list comprehension
austen_texts = gutenberg.raw(fileids=[f for f in gutenberg.fileids() if 'austen' in f])
#
#
#
#
nltk.download('stopwords') # download stopwords package
stop_words = set(stopwords.words('english')) # select english stopwords
austen_words = nltk.word_tokenize(austen_texts) # tokenize austen texts
# filter words with list comprehension
filtered_words = [word for word in austen_words if word.lower() not in stop_words]
#
#
#
#
cv = CountVectorizer() # initiate class instance
tf = cv.fit_transform(filtered_words) # count words
tf_feature_names != cv.get_feature_names_out() 

tfidf = TfidfVectorizer() # initiate class instance
tfidf_matrix = tfidf.fit_transform(filtered_words) # create tfidf matrix
tfidf_feature_names = tfidf.get_feature_names_out()
#
#
#
#
tf_df.sum().sort_values(ascending=False).head(20) # view the top 20 words
plot_most_common_words(tf, cv) # create a plot of most common words
plot_most_common_words(tfidf_matrix, tfidf)
#
#
#
#
