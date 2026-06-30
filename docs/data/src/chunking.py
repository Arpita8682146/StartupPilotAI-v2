def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i+chunk_size]

        chunks.append(chunk)

    return chunks


sample = """
Startup India promotes innovation and entrepreneurship.

Funding opportunities are available through government schemes.

Legal compliance is important for startup registration.
"""

result = chunk_text(sample)

for idx, chunk in enumerate(result):

    print(f"\nChunk {idx+1}\n")

    print(chunk)