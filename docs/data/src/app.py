from rag_pipeline import ask

print("Program Started")

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = ask(question)

    print("\nAnswer:\n")

    print(answer)