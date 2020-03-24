  
# web_app/services/basilica_service.py

import basilica
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("BASILICA_API_KEY")

def basilica_api_client():
    connection = basilica.Connection(API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>
    return connection

if __name__ == "__main__":
    print("---------")
    connection = basilica.Connection(API_KEY)
    print(type(connection)) #> <class 'basilica.Connection'>

    print("---------")
    sentence = "Hello again"
    sent_embeddings = connection.embed_sentence(sentence)
    print('Length of 1 embedding:', len(sent_embeddings))
    #print(list(sent_embeddings))

    print("---------")
    sentences = ["Hello world!", "How are you?"]
    print(sentences)

    embeddings = connection.embed_sentences(sentences)
    print("EMBEDDINGS...")
    print(type(embeddings))
    embed_list = list(embeddings)
    print('Number of embeddings:', len(embed_list))
    for i in range(len(embed_list)):
        print(f'\tEmbedding {i} length: {len(embed_list[i])}, 1st 3:', 
              embed_list[i][:3])
    #print(list(embeddings)) # [[0.8556405305862427, ...], ...]
