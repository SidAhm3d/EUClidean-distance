import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Content specification
documents = [
    "Cristiano Ronaldo is Considered as one of the best footballers ever.", 
    "In his career, lionel messi has won eight Ballon d'Or awards.", 
    "Sheffield F.C is the oldest professional football club in the world and it was founded in 1857. ",  
    "The three main leagues are Spanish La Liga, Italian Serie A, and the English Premier League. ",      
    "The El Clasico match between Real Madrid and Barcelona is one of the greatest football matches on the planet.",  
    "only 8 teams have won world cups since the 1930 FIFA  world cup.",   
    "A goalkeeper is someone who protects a team's goal. There are goalkeepers in sports like footbal.",
]

# Tokenization of documents
tokens = []
for doc in documents:
    # Split into individual words and remove punctuation
    words = nltk.word_tokenize(doc.lower())
    words = [word for word in words if word.isalnum()]
    tokens.append(words)

# Processing of document terms
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
terms = []
for doc_tokens in tokens:
    doc_terms = []
    for token in doc_tokens:
        # Remove stop words and perform stemming
        if token not in stop_words:
            term = stemmer.stem(token)
            doc_terms.append(term)
            # Add new term to global list if not already present
            if term not in terms:
                terms.append(term)

# Index building
index = {}
for i, doc_terms in enumerate(tokens):
    for term in doc_terms:
        # Add new term to index if not already present
        if term not in index:
            index[term] = []
        index[term].append(i)

# Get the query from the user.
query = input("Enter your query: ")

# Tokenize the query.
query_tokens = nltk.word_tokenize(query.lower())

# Remove stop words and perform stemming.
query_terms = []
for token in query_tokens:
    if token not in stop_words:
        term = stemmer.stem(token)
        query_terms.append(term)

# Calculate the Euclidean distance between the query and each document.
distances = []
for i in range(len(documents)):
    # Calculate the Euclidean distance between the two documents
    distance = 0
    for term in query_terms:
        if term in index:
            distance += (index[term].count(i) - query_terms.count(term))**2
        else:
            distance += query_terms.count(term)**2
    distances.append((distance, i))

# Sort the distances in ascending order.
distances.sort()

# Get the document with the lowest distance.
document = distances[0][1]

# Print the document.
print(documents[document])
