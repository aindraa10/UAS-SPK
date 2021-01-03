import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

word_data = "hows ares your todays"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#Next find the roots of the word
for w in nltk_tokens:
       print("Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w)))

# import nltk
# from nltk.stem import WordNetLemmatizer
# wordnet_lemmatizer = WordNetLemmatizer()

# word_data = "hows ares your"
# nltk_tokens = nltk.word_tokenize(word_data)
# for w in nltk_tokens:
#        print ("Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w)))