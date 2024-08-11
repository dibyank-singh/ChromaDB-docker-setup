import chromadb
from chromadb.config import Settings

chroma_client = chromadb.HttpClient(
    host="chroma",
    port=8000,
    settings=Settings(allow_reset=True, anonymized_telemetry=False)
)

# SECTION - Test with simple text Document.


documents = [
    "The Great Wall of China, one of the world's most impressive architectural feats, stretches over 13,000 miles.",
    "The Amazon Rainforest, often referred to as the 'lungs of the Earth', is home to an estimated 390 billion individual trees.",
    "The theory of evolution by natural selection was first formulated by Charles Darwin in his 1859 book, 'On the Origin of Species'.",
    "The Pyramids of Giza, built during Egypt's Fourth Dynasty, are among the Seven Wonders of the Ancient World.",
    "The discovery of penicillin by Alexander Fleming in 1928 marked the beginning of modern antibiotics.",
    "The concept of relativity, revolutionizing our understanding of space and time, was introduced by Albert Einstein in the early 20th century.",
    "The human genome consists of approximately 3 billion DNA base pairs and contains about 20,000-25,000 genes.",
    "The theory of general relativity describes the gravitational force as a curvature in the fabric of space-time.",
    "The Internet, a global network of interconnected computers, has transformed communication, commerce, and information sharing.",
    "The discovery of DNA's double helix structure by James Watson and Francis Crick in 1953 paved the way for modern genetics.",
    "The Hubble Space Telescope, launched in 1990, has provided some of the most detailed images of distant galaxies and celestial phenomena.",
    "The Large Hadron Collider, located at CERN, is the world's largest and most powerful particle accelerator.",
    "The concept of plate tectonics explains the movement of Earth's lithospheric plates and the formation of mountains, earthquakes, and volcanoes.",
    "The theory of quantum mechanics deals with phenomena on atomic and subatomic scales, challenging classical physics concepts.",
    "The Great Barrier Reef, the world's largest coral reef system, is located off the coast of Queensland, Australia."
]

metadatas = [
    {'source': "Architecture"}, {'source': "Nature"}, {'source': "Science"},
    {'source': "History"}, {'source': "Medicine"}, {'source': "Physics"},
    {'source': "Genetics"}, {'source': "Physics"}, {'source': "Technology"},
    {'source': "Genetics"}, {'source': "Astronomy"}, {'source': "Physics"},
    {'source': "Geology"}, {'source': "Physics"}, {'source': "Nature"}
]
ids = [str(i) for i in range(1, 16)]

def get_or_create_collection(client, name):
    while True:
        try:
            return client.get_or_create_collection(name=name)
        except Exception as e:
            print(f"Error retrieving or creating collection: {e}")

document_collection = get_or_create_collection(chroma_client, "sample_collection")

# Add documents to the collection
document_collection.add(documents=documents, metadatas=metadatas, ids=ids)

def query_collection(collection, query_text, n_results):
    try:
        results = collection.query(query_texts=query_text, n_results=n_results)
        return results["documents"][0]
    except Exception as e:
        print(f"Error querying the collection: {e}")
        return []

query_text = "Tell me about scientific discoveries"
result_documents = query_collection(document_collection, query_text, n_results=3)

for doc in result_documents:
    print(doc)



# Uncomment and used it- for connecting with file directly.


# import chromadb
# from chromadb.config import Settings

# chroma_client = chromadb.HttpClient(
#     host="chroma",
#     port=8000,
#     settings=Settings(allow_reset=True, anonymized_telemetry=False)
# )

# def read_txt_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.readlines()
    
    
#  # SECTION - Connect with file here::

# file_path = 'path/to/your/details.txt'
# file_content = read_txt_file(file_path)

# documents = [line.strip() for line in file_content if line.strip()]

# metadatas = [{'source': "CustomFile"} for _ in documents]
# ids = [str(i) for i in range(1, len(documents) + 1)]

# def get_or_create_collection(client, name):
#     while True:
#         try:
#             return client.get_or_create_collection(name=name)
#         except Exception as e:
#             print(f"Error retrieving or creating collection: {e}")

# document_collection = get_or_create_collection(chroma_client, "sample_collection")

# document_collection.add(documents=documents, metadatas=metadatas, ids=ids)

# def query_collection(collection, query_text, n_results):
#     try:
#         results = collection.query(query_texts=query_text, n_results=n_results)
#         return results["documents"][0]
#     except Exception as e:
#         print(f"Error querying the collection: {e}")
#         return []

# query_text = "Tell me about the contents of the file"
# result_documents = query_collection(document_collection, query_text, n_results=3)

# for doc in result_documents:
#     print(doc)
