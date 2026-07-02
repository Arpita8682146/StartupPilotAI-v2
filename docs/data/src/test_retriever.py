from retriever import retrieve_context

question = "How can startups get funding?"

context = retrieve_context(question)

print(context)