That's completely fine. For this week, keeping DSA to **2 quality questions/day** is enough. You've already covered:

✅ Sliding Window
✅ Stack
✅ Monotonic Stack
✅ Group Anagrams
✅ Top K Frequent Elements (Heap Concept)

That's solid progress.

---

# Day 8 GenAI (Intermediate) – RAG Deep Dive

## Topic 1: Chunking

### Q1. Why do we chunk documents?

**Answer:**

LLMs have a context window limit and embedding models work better on smaller pieces of text.

Instead of embedding a 100-page document, we split it into smaller chunks and embed each chunk separately.

**Flow:**

```text
Document
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
```

---

### Q2. What happens if chunks are too large?

Example:

```text
Chunk Size = 3000 words
```

Problems:

* Retrieval becomes less precise
* Irrelevant information gets retrieved
* Higher token cost
* More context noise

---

### Q3. What happens if chunks are too small?

Example:

```text
Chunk Size = 20 words
```

Problems:

* Loss of context
* Sentences get split
* Important information spread across chunks

Example:

```text
Chunk 1:
"The policy starts on"

Chunk 2:
"January 1st 2025"
```

Neither chunk makes sense alone.

---

### Q4. Fixed vs Semantic Chunking

#### Fixed Chunking

```text
Every 500 tokens
```

Pros:

* Fast
* Simple

Cons:

* Can split meaning

---

#### Semantic Chunking

Split at:

* Paragraphs
* Headings
* Sections

Pros:

* Preserves meaning
* Better retrieval

Cons:

* More expensive

---

# Topic 2: Embedding Models

### Q5. What is an embedding model?

An embedding model converts text into numerical vectors while preserving semantic meaning.

Example:

```text
"car"
```

becomes

```text
[0.23, 0.89, -0.12, ...]
```

---

### Q6. Why Embeddings?

Because computers cannot compare meaning directly.

Example:

```text
car
automobile
vehicle
```

Embedding vectors will be close together.

---

### Q7. Difference Between LLM and Embedding Model

| LLM                | Embedding Model            |
| ------------------ | -------------------------- |
| Generates text     | Generates vectors          |
| Used for answering | Used for retrieval         |
| GPT, Claude        | BGE, E5, OpenAI Embeddings |

---

### Interview Answer

> An embedding model converts text into dense vector representations that capture semantic meaning, while an LLM generates natural language responses.

---

### Q8. Why can't GPT be used directly for retrieval?

Because retrieval requires:

```text
Fast similarity search
```

GPT generates text but doesn't efficiently search millions of vectors.

Embeddings + Vector DB solve retrieval.

---

# Topic 3: Vector Databases

### Q9. Why Vector Databases?

Traditional databases search:

```text
Exact match
```

Vector DB searches:

```text
Semantic similarity
```

Example:

Query:

```text
How can I reset my password?
```

Document:

```text
Steps to change account credentials
```

Keyword search may fail.

Vector search succeeds.

---

### Q10. Popular Vector Databases

| Database | Notes                    |
| -------- | ------------------------ |
| ChromaDB | Local development        |
| FAISS    | Fast local vector search |
| Pinecone | Managed cloud service    |
| Weaviate | Enterprise-grade         |
| pgvector | PostgreSQL extension     |

---

### Interview Favorite

**FAISS vs Pinecone**

FAISS:

* Open-source
* Runs locally
* No hosted service

Pinecone:

* Managed cloud solution
* Scalable
* Production-friendly

---

# Topic 4: Similarity Search

### Q11. What is Cosine Similarity?

Measures angle between vectors.

Formula:

\cos(\theta)=\frac{A\cdot B}{||A||,||B||}

---

### Interview Answer

> Cosine similarity measures how similar two vectors are based on the angle between them. It is commonly used in vector search and retrieval systems.

---

### Example

```text
car
automobile
```

Similarity:

```text
0.95
```

Very close.

---

```text
car
pizza
```

Similarity:

```text
0.10
```

Not related.

---

# Topic 5: Hybrid Search

This is being asked more frequently now.

### Q12. Why does pure vector search fail?

Embeddings may miss:

* Error codes
* IDs
* Product names
* Exact keywords

Example:

```text
ERR-5678
```

Vector search often struggles.

---

### Q13. What is BM25?

A keyword-based retrieval algorithm.

It scores documents based on:

* Keyword frequency
* Document length
* Relevance

---

### Q14. Dense vs Sparse Retrieval

| Dense      | Sparse      |
| ---------- | ----------- |
| Embeddings | Keywords    |
| Semantic   | Exact match |
| Vector DB  | BM25        |

---

### Q15. What is Hybrid Search?

Combines:

```text
Dense Retrieval
+
Sparse Retrieval
```

Benefits:

* Better recall
* Better precision

---

# Topic 6: Rerankers

### Most Asked Production RAG Question

> What if the correct chunk is ranked 12th and Top-K is only 5?

---

### Wrong Answer

```text
Increase Top-K to 20
```

Problem:

* Larger context
* More token cost
* More noise

---

### Correct Answer

Use a reranker.

Flow:

```text
Retrieve Top 50
        ↓
Rerank
        ↓
Keep Top 5
        ↓
Send to LLM
```

---

### Popular Rerankers

* Cohere Rerank
* BGE-Reranker
* Cross Encoder models

---

### Interview Answer

> I would retrieve a larger candidate set and use a reranker to score chunks against the full query. This improves recall while keeping the final context window small.

---

# Day 8 Interview Question

Try answering this tomorrow:

> Design a production-ready RAG system for a company's internal knowledge base.

A strong answer should include:

```text
Documents
→ Chunking
→ Embeddings
→ Vector DB
→ Hybrid Search
→ Reranking
→ LLM
→ Guardrails
→ Monitoring
```

This is exactly the kind of GenAI system-design question being asked for GenAI Engineer and Conversational AI roles.
