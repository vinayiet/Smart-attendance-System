# faiss_index.py

import faiss
import numpy as np
import os

class FaissIndexManager:
    def __init__(self, index_file="faiss_index.bin", embedding_dimension=128):
        self.index_file = index_file
        self.embedding_dimension = embedding_dimension

        # Initialize FAISS index
        self.index = faiss.IndexFlatL2(self.embedding_dimension)  # L2 = Euclidean Distance

        # Load existing index if it exists
        self.load_index()

    def load_index(self):
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
            print("FAISS index loaded successfully.")
        else:
            print("No existing FAISS index found, starting fresh.")

    def save_index(self):
        faiss.write_index(self.index, self.index_file)
        print("FAISS index saved successfully.")

    def add_embedding(self, embedding):
        embedding = np.array(embedding).astype("float32").reshape(1, -1)
        self.index.add(embedding)
        self.save_index()  # Save after adding

    def search_embedding(self, embedding, k=1):
        embedding = np.array(embedding).astype("float32").reshape(1, -1)
        distances, indices = self.index.search(embedding, k)
        return distances, indices
