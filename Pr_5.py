import nltk
import re
import contractions
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
# Download required resources
nltk.download('punkt')
# Sample text
text ="I'm learning NLP!!! It's fun, isn't it?"
# 1. Expanding contractions
expanded_text = contractions.fix(text)
print("Expanded Text:"
, expanded_text)
# 2. Removing special characters (keep only alphabets & spaces)
clean_text = re.sub(r'[^a-zA-Z\s]'
''
,
, expanded_text)
print("Cleaned Text:"
, clean_text)
# 3. Case conversion (to lowercase)
lower_text = clean_text.lower()
print("Lowercase Text:"
, lower_text)
# 4. Tokenization
tokens = word_tokenize(lower_text)
print("Tokens:"
, tokens)
# Generate N-grams
# Unigrams
unigrams = list(ngrams(tokens, 1))
print("Unigrams:"
, unigrams)
# Bigrams
bigrams = list(ngrams(tokens, 2))
print("Bigrams:"
, bigrams)
# Trigrams
trigrams = list(ngrams(tokens, 3))
print("Trigrams:"
, trigrams)