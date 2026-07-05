from retriever import retrieve_context
from prompt_builder import build_prompt
from gemini_client import generate_answer


def ask(question):

    context = retrieve_context(question)

    prompt = build_prompt(
        question,
        context
    )

    answer = generate_answer(prompt)

    return answer

