def validate_documents(documents):
    """
    Ensures retrieved documents are usable.
    """
    return documents and len(documents) > 0


def fallback_message():
    """
    Returns safe fallback response.
    """
    return "I could not find enough information to answer your question."
