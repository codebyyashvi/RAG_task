# RAG Task – Elasticsearch-Based Retrieval System

## Repository Overview
This repository contains a well-structured implementation of a document retrieval system using **Elasticsearch 7.x**. The project covers dataset generation, indexing, retrieval, optimization, and evaluation of retrieval efficiency.

The repository follows clear directory organization and uses version control with meaningful commits.

---

## Project Structure

```text
RAG_TASK/
│
├── data/
│   ├── data_generation.md
│   ├── data.json
│   ├── eval_queries.json
│   ├── experiment_results.json
│   └── schema.md
│
├── efficiency/
│   ├── efficiency.md
│   ├── evaluation.py
│   ├── experiments.py
│   └── plots.py
│
├── src/
│   ├── config.py
│   ├── context_builder.py
│   ├── create_index.py
│   ├── data_ingestion.py
│   ├── elasticsearch.yml
│   ├── generator.py
│   ├── optimization.md
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── search_queries.py
│   └── utils.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
---

# Project Setup Instructions

## Prerequisites

Ensure the following are installed on your system:

- **Python**: 3.10 or higher  
- **Java**: 11 or 17 (required for Elasticsearch 7.17.29)  
- **Elasticsearch**: 7.17.29  
- **Git**
```
---

## Step 1: Clone the Repository

```bash
git clone https://github.com/codebyyashvi/RAG_task.git
cd RAG_TASK
```
## Step 2: Create and Activate Virtual Environment (Recommended)

```bash
python -m venv venv
```
# Windows
```bash
venv\Scripts\activate
```
# Linux / macOS
```bash
source venv/bin/activate
```
## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
## Step 4: Configure Environment Variables

Create a .env file in the project root if it does not already exist.

```bash
GROQ_API_KEY=your_groq_api_key
ELASTICSEARCH_URL=http://localhost:9200
INDEX_NAME=tech_docs
```
## Step 5: Start Elasticsearch

Ensure Elasticsearch 7.17.x is running.

```bash
cd path_to_your_elasticsearch-7.17.29_directory
.\bin\elasticsearch.bat
```
# Verify:

```bash
curl http://localhost:9200
```
## Step 6: Create Elasticsearch Index

```bash
python src/create_index.py
```
## Step 7: Ingest Dataset

```bash
python src/data_ingestion.py
```
## Step 8: Run Retrieval Queries
```bash
python src/search_queries.py
```
## Step 9: Evaluate Retrieval Efficiency
Run experiments and generate plots for retrieval efficiency evaluation.

```bash
python efficiency/experiments.py
python efficiency/plots.py
```
## Evaluation Overview

The retrieval system is evaluated using the following metrics:

- **Retrieval Accuracy:** Precision, Recall, F1-score  
- **Latency:** End-to-end query response time  
- **Relevance:** Qualitative analysis of retrieved documents  
- **Answer Quality:** Assessment of generated responses  

Detailed evaluation results and analysis are available in:

- `efficiency/efficiency.md`  
- `data/experiment_results.json`

