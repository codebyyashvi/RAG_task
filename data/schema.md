# Dataset Schema Documentation

## Overview
This document describes the schema used for the synthetic dataset created for the Elasticsearch and Retrieval-Augmented Generation (RAG) pipeline task. Each record in the dataset represents a single document suitable for semantic search and retrieval.

## Schema Fields

### doc_id
- Type: String
- Description: A unique identifier for each document.
- Example: "DOC_042"

### title
- Type: String
- Description: A short, descriptive title summarizing the document content.
- Purpose: Used for keyword-based and semantic search.

### category
- Type: String
- Description: High-level classification of the document domain.
- Example values: Elasticsearch, RAG, Security, AI Concepts, Cloud, DevOps.

### content
- Type: String
- Description: The main textual body of the document containing meaningful information.
- Purpose: Primary field for semantic search, vector embeddings, and RAG context generation.

### tags
- Type: Array of Strings
- Description: Keywords associated with the document.
- Purpose: Improves filtering, relevance boosting, and metadata-based queries.

### created_at
- Type: String (ISO date format)
- Description: The date when the document was created.
- Example: "2025-01-01"

## Notes
- Each JSON object corresponds to one document in Elasticsearch.
- The schema is designed to be compatible with Elasticsearch 7.x indexing and vector-based retrieval.
