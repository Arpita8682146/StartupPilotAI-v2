import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IQ93VwA5hev_G8GPfm3UTj8n8xVwBIR6RWmL-yMib1tg")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)