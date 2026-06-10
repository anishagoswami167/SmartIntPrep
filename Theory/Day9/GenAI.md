Excellent. These topics are exactly the kind of questions asked for GenAI Engineer, Conversational AI Engineer, and RAG Developer interviews.

---

# Topic 1: RAG Evaluation

## Q1. How do you evaluate a RAG system?

A RAG system has **two components**:

```text
1. Retrieval Quality
2. Generation Quality
```

So evaluation should measure both.

Common metrics:

```text
Context Recall
Faithfulness
Answer Relevance
Context Precision
Latency
Cost
```

---

## Q2. What is Context Recall?

Measures:

```text
Did the retriever fetch the information needed to answer the question?
```

Example:

Question:

```text
What is Deloitte's leave policy?
```

Correct chunk exists in document.

If retriever successfully retrieves it:

```text
High Context Recall
```

If chunk never appears in retrieved results:

```text
Low Context Recall
```

---

## Q3. What is Faithfulness?

Measures:

```text
Is the answer supported by retrieved context?
```

Example:

Retrieved Context:

```text
Employees get 20 annual leave days.
```

Generated Answer:

```text
Employees get 25 leave days.
```

❌ Hallucination

Faithfulness is low.

---

## Q4. What is Answer Relevance?

Measures:

```text
Does the answer actually address the user's question?
```

Question:

```text
What is the refund policy?
```

Answer:

```text
The company was founded in 2010.
```

Not relevant.

Low Answer Relevance.

---

## Q5. Why is Accuracy Alone Insufficient?

Because:

```text
Correct answer can be generated for the wrong reason.
```

Example:

LLM memorized answer from training data.

Retriever failed completely.

Accuracy:

```text
100%
```

Retrieval quality:

```text
0%
```

Production RAG is still broken.

---

# Topic 2: Multi-Document RAG

## Why Single-Chunk RAG Fails?

Most business questions require:

```text
Multiple documents
Multiple sources
Multiple hops
```

Example:

```text
Compare Q3 revenue across all regions.
```

Information exists in:

```text
US Report
Europe Report
Asia Report
```

No single chunk contains answer.

---

## How Would You Answer Questions Across Multiple Documents?

### Step 1

Retrieve from multiple documents.

Example:

```text
Top 20-50 chunks
```

instead of:

```text
Top 3
```

---

### Step 2

Rerank

Keep only:

```text
Most relevant chunks
```

---

### Step 3

Synthesize answer

LLM combines information.

---

## Query Decomposition

Break question into subquestions.

Example:

```text
Compare sales across India, US and UK.
```

Convert into:

```text
Sales India?
Sales US?
Sales UK?
```

Retrieve separately.

Merge results.

---

## Document-Level Retrieval

Two-stage retrieval:

```text
Question
↓
Find relevant documents
↓
Find relevant chunks inside documents
```

This often improves retrieval quality.

---

## Context Compression

Instead of sending:

```text
20 full chunks
```

Extract only:

```text
Relevant sentences
```

Benefits:

```text
Lower token usage
Higher precision
Lower cost
```

---

# Topic 3: Hybrid Search Deep Dive

## Dense Retrieval

Uses:

```text
Embeddings
```

Captures:

```text
Semantic similarity
```

Example:

```text
Car
Automobile
Vehicle
```

can match even if exact words differ.

---

## Sparse Retrieval

Uses:

```text
Keywords
BM25
TF-IDF
```

Good for:

```text
Error codes
Product IDs
Names
```

---

## BM25

Keyword ranking algorithm.

Scores documents based on:

```text
Term frequency
Inverse document frequency
```

Very common in search engines.

---

## Reciprocal Rank Fusion (RRF)

Combines:

```text
Dense Ranking
+
Sparse Ranking
```

Formula idea:

```text
Higher ranked documents get higher score.
```

Final ranking uses both retrieval methods.

---

## When Would You Use Hybrid Search?

Use when:

```text
Exact keyword matching matters
AND
Semantic meaning matters
```

Examples:

```text
Enterprise Search
Customer Support
Knowledge Bases
Healthcare
Legal Systems
```

---

# Topic 4: Production RAG

## Interview Question

### Your RAG returns top-5 chunks. The answer is in chunk #12. What would you do?

---

## Step 1: Hybrid Search

Combine:

```text
Vector Search
+
BM25
```

to improve recall.

---

## Step 2: Retrieve Wide

Instead of:

```text
Top 5
```

retrieve:

```text
Top 50
```

candidates.

---

## Step 3: Rerank

Use:

```text
Cohere Rerank
BGE-Reranker
Cross Encoders
```

Rerank top 50.

Keep best 5.

---

## Step 4: Query Rewriting

Rewrite:

```text
User Query
```

into a better search query.

Techniques:

```text
HyDE
Query Expansion
```

---

## Step 5: Context Compression

Compress retrieved chunks.

Keep:

```text
Answer-bearing sentences only
```

---

## Step 6: Multi-Query Retrieval

Generate:

```text
3-5 versions
```

of the same question.

Retrieve for each.

Merge results.

---

# Interview Answer (Short Version)

> I would improve recall using hybrid search and wider retrieval, then use a reranker such as BGE-Reranker or Cohere Rerank to bring chunk #12 into the top results. I would also use query rewriting, multi-query retrieval, and contextual compression before passing context to the LLM.

---

# Topic 5: LangChain

## What is LangChain?

Framework used to build:

```text
LLM Applications
RAG Systems
Agents
Workflows
```

Provides:

```text
Prompt Management
Chains
Agents
Memory
Tools
Retrievers
```

---

## Chains vs Agents

### Chains

Fixed workflow.

Example:

```text
Question
↓
Retriever
↓
LLM
↓
Answer
```

Predictable.

---

### Agents

Dynamic workflow.

Example:

```text
Question
↓
Reason
↓
Choose Tool
↓
Execute
↓
Observe
↓
Answer
```

Agent decides what to do.

---

## Retriever

Responsible for:

```text
Fetching relevant documents
```

Example:

```python
retriever.invoke(query)
```

Returns:

```text
Relevant chunks
```

---

## Memory

Stores conversation history.

Examples:

```text
Buffer Memory
Summary Memory
Vector Memory
```

Used for:

```text
Chatbots
Virtual Assistants
```

---

## Tools

External capabilities available to agents.

Examples:

```text
Calculator
Weather API
SQL Database
Search Tool
```

Agent can invoke tools when needed.

---

## LCEL (LangChain Expression Language)

New LangChain syntax for building pipelines.

Example concept:

```text
Prompt
|
Retriever
|
LLM
|
Parser
```

Benefits:

```text
Cleaner
Composable
Production-friendly
```

---

# Day 9 Interview Questions

Try answering these tomorrow:

1. Difference between Context Recall and Faithfulness?
2. Why does Single-Chunk RAG fail?
3. Dense vs Sparse Retrieval?
4. Why Hybrid Search?
5. What is Reranking?
6. Chains vs Agents?
7. When would you use LangGraph instead of a Chain?
8. How would you design a production-ready RAG system for Deloitte's internal knowledge base?

These are highly aligned with your background in multilingual chatbots, RAG systems, LangChain, and conversational AI.
