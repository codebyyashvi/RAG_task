from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "You are a technical assistant. "
    "Answer the user's question strictly using the provided context. "
    "If the context does not contain the answer, say so clearly."
)

def generate_response(context, query, model="llama-3.1-70b-versatile"):
    """
    Sends context + user query to Groq LLM
    and returns generated response.
    """
    prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
    except Exception:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
    return response.choices[0].message.content.strip()
