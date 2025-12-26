def build_context(documents):
    """
    Converts retrieved Elasticsearch documents into
    a formatted context string for the LLM.
    """
    context_blocks = []

    for i, doc in enumerate(documents, start=1):
        block = f"""
Document {i}
Title: {doc['title']}
Category: {doc['category']}
Content: {doc['content']}
"""
        context_blocks.append(block.strip())

    return "\n\n".join(context_blocks)
