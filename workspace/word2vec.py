from sentence_transformers import SentenceTransformer
import numpy as np
def find_sim(a):
    model=SentenceTransformer('all-MiniLM-L6-v2')
    inp=[a]
    embeddings1=model.encode(inp)
    embeddings3=model.encode(["what should i eat today","give me protein rich food items","how many grams of protein in","what should be my bmi","what are some healthy food","how many calories in","vegan food options","non vegan food options","unhealthy food"],convert_to_numpy=True)
    dot=np.dot(embeddings1,embeddings3.T)
    norm1=np.linalg.norm(embeddings1)
    norm2=np.linalg.norm(embeddings3,axis=1)
    sim=dot/(norm1*norm2)
    return max(sim[0])