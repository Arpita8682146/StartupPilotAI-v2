from sentence_transformers import SentenceTransformer

from vectorstore import store_embeddings
from vectorstore import search

model = SentenceTransformer(

    'all-MiniLM-L6-v2'

)

chunks = [

"Startup India supports innovation.",

"Government funding schemes are available.",

"Legal compliance is necessary."

]

embeddings = model.encode(

    chunks

)

store_embeddings(

    chunks,

    embeddings

)

query = model.encode(

"startup grants"

)

results = search(

query

)

print(

results

)