from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorMemory:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.texts = []

    def add(self, text: str):
        embedding = self.model.encode([text])[0]
        self.index.add(np.array([embedding]))
        self.texts.append(text)

    def search(self, query: str, top_k=3):
        embedding = self.model.encode([query])[0]
        D, I = self.index.search(np.array([embedding]), top_k)

        results = []
        for i in I[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results