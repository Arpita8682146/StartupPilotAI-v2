import os
import google.generativeai as genai
from retriever import retrieve_context_with_citations

# Placeholder API key for fallback
DEFAULT_KEY = "AQ.Ab8RN6IQ93VwA5hev_G8GPfm3UTj8n8xVwBIR6RWmL-yMib1tg"

def configure_gemini(api_key=None):
    """
    Configures the Gemini API client using the provided key, env variable, or default key.
    """
    key_to_use = api_key or os.environ.get("GEMINI_API_KEY") or DEFAULT_KEY
    genai.configure(api_key=key_to_use)
    return key_to_use

def ask_gemini(prompt, api_key=None, model_name="gemini-2.5-flash"):
    """
    Generates content using Gemini.
    """
    configure_gemini(api_key)
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    return response.text

def generate_answer(prompt):
    """
    Backward compatibility wrapper.
    """
    return ask_gemini(prompt)

def build_prompt_with_history(question, context, history):
    """
    Formats the context, chat history, and new query into a structured LLM prompt.
    Args:
        question: The user's prompt
        context: Concatenated text blocks retrieved from ChromaDB
        history: List of tuples representing past turns: [('user', 'msg'), ('assistant', 'msg')]
    """
    history_str = ""
    if history:
        for role, msg in history[-5:]: # Keep last 5 turns to prevent prompt bloat
            label = "User" if role == "user" else "Assistant"
            history_str += f"{label}: {msg}\n"
            
    prompt = f"""You are StartupPilotAI, an expert startup advisor and AI co-founder. 
Your goal is to guide entrepreneurs by answering their questions using the retrieved document context below.

Rules:
1. Ground your answers in the provided context as much as possible.
2. If the context does not contain the answer, you can use your general startup expertise, but explicitly state that this information was not found in the uploaded documents.
3. Keep your tone professional, encouraging, and highly actionable.
4. Structure your response using markdown headings, bullet points, or bold text for readability.

Retrieved Context:
{context or "No context retrieved. Answer using general startup advisory knowledge."}

Conversation History:
{history_str or "No history yet."}

User's Question: {question}

Actionable Response:
"""
    return prompt

def ask_rag(question, history=None, api_key=None, n_results=4):
    """
    Runs the complete RAG loop.
    Returns:
        tuple: (answer_text, list_of_citations)
    """
    if history is None:
        history = []
        
    # Retrieve context and sources
    context, citations = retrieve_context_with_citations(question, n_results=n_results)
    
    # Build prompt
    prompt = build_prompt_with_history(question, context, history)
    
    # Call Gemini API
    try:
        answer = ask_gemini(prompt, api_key=api_key)
        return answer, citations
    except Exception as e:
        error_msg = f"Error generating answer: {str(e)}\n\n*Please verify your Gemini API key in the sidebar.*"
        return error_msg, []
