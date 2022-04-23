from textblob import TextBlob

text = 'Today is a beautiful day. Tomorrow looks like bad weather.'

blob = TextBlob(text)

# get list of sentences
print(blob.sentences)

# get list of words
print(blob.words)

# tags
print(blob.tags)

# noun phrases
print(blob.noun_phrases)

# sentiments
# -1 polarity == bad emotions, 0 == neutral, 1 == good
# subjectivity: 0 == objective, 1 == subjective
print(blob.sentiment) # blob.sentiment.polarity also works

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
pri
