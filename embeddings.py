from sentence_transformers import SentenceTransformer

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(texts):
    """
    Convert list of text into embeddings
    """
    return model.encode(texts)


# Test (optional)
if __name__ == "__main__":
    sample = ["Machine learning is powerful"]
    emb = get_embedding(sample)
    print("Embedding shape:", emb.shape)