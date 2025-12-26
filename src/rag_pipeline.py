from retriever import retrieve_documents
from context_builder import build_context
from generator import generate_response
from utils import validate_documents, fallback_message


def run_rag_pipeline(query, top_k=3):
    """
    Full RAG pipeline:
    1. Retrieve documents
    2. Build context
    3. Generate answer
    """
    try:
        documents = retrieve_documents(query, top_k=top_k)

        if not validate_documents(documents):
            return fallback_message()

        context = build_context(documents)
        answer = generate_response(context, query)

        return answer

    except Exception as e:
        return f"Pipeline error: {str(e)}"


# Example usage
if __name__ == "__main__":
    question = "What is Network Security?"
    print(run_rag_pipeline(question))
    # print(run_rag_pipeline("Explain API authentication"))
    # print(run_rag_pipeline("What are insider threats?"))
    # print(run_rag_pipeline("Explain OAuth"))

