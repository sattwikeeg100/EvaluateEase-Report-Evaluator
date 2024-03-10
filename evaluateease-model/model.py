import numpy as np
import streamlit as st
from keybert import KeyBERT
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity

kw_model = KeyBERT()

@st.cache_data
def calculate_similarity(array1, array2, model_name="clips/mfaq"):
    model = SentenceTransformer(model_name)

    # Encode the arrays into fixed-dimensional vectors
    array1_embeddings = model.encode(array1)
    array2_embeddings = model.encode(array2)

    # Calculate cosine similarity between the encoded vectors
    similarity_matrix = util.cos_sim(array1_embeddings,array2_embeddings)

    return similarity_matrix

def evaluation_score(doc2):
    doc1= """Ferrari, an iconic name in the realm of automotive excellence, represents a fusion of power, precision, and passion. Founded by Enzo Ferrari in 1939, the marque has established itself as a symbol of luxury, speed, and Italian flair. Renowned for its sleek designs and exhilarating performance, each Ferrari model embodies a heritage of racing heritage and engineering prowess. From the legendary Ferrari 250 GTO to the cutting-edge LaFerrari hybrid supercar, the brand continuously pushes the boundaries of automotive innovation. With a focus on craftsmanship and attention to detail, Ferrari cars are not merely vehicles but expressions of automotive artistry. Beyond the racetrack, Ferrari’s influence extends into lifestyle and culture, captivating enthusiasts worldwide with its allure of exclusivity and prestige. Embracing advanced technologies while staying true to its heritage, Ferrari remains at the forefront of automotive excellence, inspiring admiration and fascination among aficionados and admirers alike. Whether roaring down the Autobahn or gracing the streets of Monte Carlo, a Ferrari is not just a car—it's a symbol of speed, sophistication, and the relentless pursuit of perfection."""
    
    kw1=kw_model.extract_keywords(doc1, keyphrase_ngram_range=(3,3),stop_words='english', use_maxsum=True, nr_candidates=20, top_n=15)
    keywords1=[]
    for keywordset in kw1:
        keywords1.append(keywordset[0])
        
    kw2=kw_model.extract_keywords(doc2, keyphrase_ngram_range=(3,3),stop_words='english', use_maxsum=True, nr_candidates=20, top_n=15)
    keywords2=[]
    for keywordset in kw2:
        keywords2.append(keywordset[0])
        
    similarity_matrix = calculate_similarity(keywords1, keywords2)
    s_score= similarity_matrix.mean()
        
    return s_score



