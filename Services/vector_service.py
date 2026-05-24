import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="documents"
)


# Store embeddings

def store_embeddings(chunks, embeddings):
    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[str(i) for i in range(len(chunks))]
    )


# Search embeddings

def search_embeddings(query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=3
    )

    return results