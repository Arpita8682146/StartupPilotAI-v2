import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IQ93VwA5hev_G8GPfm3UTj8n8xVwBIR6RWmL-yMib1tg")

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

print("USING MODEL:", model.model_name)

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def generate_answer(prompt):
    return ask_gemini(prompt)
