Perfect! Since you've completed **Day 4 DSA**, let's do **Day 4 GenAI Revision (45–60 min)** focused on interview questions.

---

# 🤖 Topic 1: RAG (Retrieval Augmented Generation)

### What is RAG?

RAG is a technique where we:

```text id="a1"
User Query
      ↓
Retrieve relevant documents
      ↓
Send documents + query to LLM
      ↓
Generate answer
```

---

### Why do we need RAG?

Problem:

```text id="a2"
LLMs have limited knowledge.
They may not know:
• Company documents
• Latest policies
• Internal knowledge
```

Solution:

```text id="a3"
Fetch relevant information first.
Then generate answer.
```

---

### Interview Question

**How does RAG reduce hallucination?**

Answer:

```text id="a4"
Without RAG, the model relies only on its training data and may guess answers.

With RAG, relevant documents are retrieved and provided as context, so the model answers based on actual information instead of making assumptions.
```

---

### RAG Pipeline

```text id="a5"
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
LLM
```

Be able to explain each step.

---

# 🤖 Topic 2: Embeddings

### What are Embeddings?

Embeddings are numerical vector representations of text.

Example:

```text id="a6"
"cat"  → [0.23, 0.78, 0.11 ...]

"dog"  → [0.21, 0.75, 0.14 ...]
```

Since cat and dog are similar, their vectors will be close.

---

### Why Embeddings?

Used for:

```text id="a7"
Semantic Search
RAG
Recommendation Systems
Similarity Search
```

---

### Interview Question

**Why can't we use keywords instead of embeddings?**

Answer:

```text id="a8"
Keyword search matches exact words.

Embeddings understand meaning.

For example:
"car" and "automobile"

Keyword search may fail.
Embedding search can identify them as similar.
```

---

# 🤖 Topic 3: Vector Database

### What is a Vector Database?

Stores embeddings and helps find similar vectors quickly.

Examples:

* FAISS
* Chroma
* Pinecone
* Weaviate

---

### Interview Question

**Why not store embeddings in SQL?**

Answer:

```text id="a9"
Traditional databases are not optimized for similarity search.

Vector databases are designed to efficiently find nearest vectors among millions of embeddings.
```

---

# 🤖 Topic 4: Chunking

### What is Chunking?

Breaking large documents into smaller pieces.

Example:

```text id="a10"
100-page PDF
↓
Chunk 1
Chunk 2
Chunk 3
...
```

---

### Why Chunking?

Because LLMs cannot process huge documents efficiently.

Smaller chunks:

```text id="a11"
Better retrieval
Better accuracy
Less token usage
```

---

### Interview Question

**What happens if chunks are too large?**

Answer:

```text id="a12"
Retriever may return irrelevant information and increase token cost.
```

---

### What happens if chunks are too small?

```text id="a13"
Important context may be lost.
```

---

# 🤖 Topic 5: Context Window

### What is Context Window?

Maximum amount of text an LLM can process at one time.

Includes:

```text id="a14"
User prompt
Chat history
Retrieved documents
Model response
```

---

### Interview Question

**What happens when context window is exceeded?**

Answer:

```text id="a15"
Older information may be truncated or ignored depending on the implementation.
```

---

# 🤖 Topic 6: Fine-Tuning vs RAG

### Fine-Tuning

Changes model weights.

Used when:

```text id="a16"
Need new behavior
Need domain-specific style
Need task specialization
```

---

### RAG

Does not change model weights.

Used when:

```text id="a17"
Need latest information
Need company documents
Need dynamic knowledge
```

---

### Interview Question

**When would you choose RAG over Fine-Tuning?**

Answer:

```text id="a18"
When knowledge changes frequently.

For example:
Policies
Knowledge bases
Product documents

Updating documents is easier than retraining the model.
```

---

# 🎯 Must-Know Interview Questions

Prepare answers for:

1. What is an LLM?
2. What is a token?
3. What is temperature?
4. What is hallucination?
5. What is RAG?
6. How does RAG reduce hallucination?
7. What are embeddings?
8. What is a vector database?
9. What is chunking?
10. Fine-Tuning vs RAG?
11. What is context window?
12. What are prompt engineering techniques?

    * Zero Shot
    * One Shot
    * Few Shot

---

# 📝 Day 4 Deliverables

### DSA

✅ Buy & Sell Stock

✅ Maximum Consecutive Ones

✅ Fixed Sliding Window Concept

---

### GenAI

✅ RAG

✅ Embeddings

✅ Vector DB

✅ Chunking

✅ Context Window

✅ Fine-Tuning vs RAG

---

Tomorrow (Day 5) we'll move into:

* Python OOP basics
* Two Pointers revision
* More Sliding Window questions
* LangChain & Agents interview revision (important for GenAI Engineer roles). 🚀
