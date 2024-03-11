
#import has been commented to avoid errors using python script

#import spacy 
#from textblob import TextBlob
#nlp = spacy.load('en_core_web_md')

#this is used to load the spacy model for our preprocessing and use of NLP

#import pandas as pd
amazon_reviews = pd.read_csv ('amazon_product_reviews.csv', dtype={1:str, 10:str})


#Spacy is used to load the language model. 
#The data for amazon products have been read in.
#The function intends to return the polarity score of the amazon reviews based on the types of words used.

#Intentions with NLP Capstone:
#1. CSV file to be read.
#Missing values to be dropped.
#Reviews are then tokenised.
#The polarity of reviews are to be found.
#The sentiment of these reviews is to then be found.
#The similarity of these two tokenised results are thereafter found.
#The results are to then be printed


#Here the reviews.text column is intended to be extracted alone as this is the most relevant from the dataset
amazon_reviews[['reviews.text']]

#The isnull functions detects any missing values in the data.
amazon_reviews.isnull().sum()

#dropna is then used to clean the data
amazon_reviews.dropna(subset=['reviews.text'])
selected_reviews = amazon_reviews.sample



#the function defines the text as preprocessed before checking for similarities
def preprocess(amazon_reviews):
    
    doc = nlp(amazon_reviews.lower())
    processed = [token.lemma_.lower()for token in doc if not token.is_stop and token.is_punct]

    return ''.join (processed)

# then apply the function to the reviews
amazon_reviews['processed.text'] = amazon_reviews[['reviews.text']].apply(preprocess)

#this function will extract from the reviews, which already preprocessed and cleaned, which have similarities
for sentence in amazon_reviews: 
    doc = nlp(sentence)
    tokens = [token.lemma_.lower()for token in doc if not token.is_stop and token.is_alpha]
    for token in tokens:
        blob = TextBlob(str(token))

        polarity = blob.sentiment.polarity 
        
        
if polarity > 0:
    sentiment = 'good'
elif polarity < 0:
    sentiment = 'bad'
else:
    sentiment = 'okay'

print(f"Review: {amazon_reviews}\nPolarity Score: {polarity_score}\nSentiment Score: {sentiment}")



#Based on these conditions the polarity score is then ranked based on the opinions of the review



#For the case of sentiment similarities, this takes the reviews and compares them with each other that way we find a score for the reviews.
review1 = nlp("Didnt know how much i'd use a kindle so went for the lower end. im happy with it, even if its a little dark")
review2 = nlp("the future of reading you just have this and it is like a whole library")

similarity = review1.similarity(review2)
print(f"show similarity: {similarity:.2f}")

review3 = nlp("I love the Kindle, it is a great product. It reduces eye strain so I enjoy reading on it. This is my second Kindle.")
review4 = nlp("Good, able to read under bright sunlight conditions too")

similarity = review3.similarity(review4)
print(f"show similarity: {similarity:.2f}")
