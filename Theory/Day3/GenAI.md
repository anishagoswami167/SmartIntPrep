
# Topic 1: Why Transformers Replaced RNNs?

### Traditional NLP Models

Before Transformers, people used:

```text
RNN
LSTM
GRU
```

Sentence:

```text
I love learning AI
```

RNN processes words one by one:

```text
I
↓
love
↓
learning
↓
AI
```

### Problem 1: Slow

Cannot process all words together.

Must wait for previous word.

---

### Problem 2: Long-Term Memory

Sentence:

```text
The movie that I watched yesterday was amazing.
```

When reading:

```text
amazing
```

the model may forget:

```text
movie
```

This is called:

```text
Long-range dependency problem
```

---

### Transformer Solution

Process all words simultaneously.

```text
I
love
learning
AI
```

All words can attend to each other.

Faster training.

Better understanding.

---

# Interview Answer

### Why Transformers replaced RNNs?

```text
RNNs process words sequentially, making training slow and causing difficulty in capturing long-range dependencies.

Transformers use self-attention, allowing parallel processing of all tokens and better handling of long-context information.
```

---

# Topic 2: What is Self-Attention?

This is asked constantly in GenAI interviews.

Sentence:

```text
The cat sat on the mat because it was tired.
```

Question:

```text
Who was tired?
```

```text
it
```

refers to:

```text
cat
```

not:

```text
mat
```

Self-attention helps the model identify this relationship.

---

### Layman Explanation

Imagine you're reading a sentence.

For each word:

```text
Look at every other word.
Decide which words are important.
Give more attention to important words.
```

That's self-attention.

---

# Topic 3: What is an Embedding?

Interview favorite.

---

### Problem

Computers don't understand text.

```text
cat
dog
car
```

Need numbers.

---

### Old Method

One-hot encoding:

```text
cat = [1,0,0]
dog = [0,1,0]
car = [0,0,1]
```

Problem:

```text
cat and dog appear completely unrelated
```

---

### Embedding

Convert words into dense vectors.

Example:

```text
cat = [0.2, 0.8, 0.5]
dog = [0.3, 0.7, 0.6]
car = [0.9, 0.1, 0.2]
```

Now:

```text
cat and dog are close
```

because they are semantically similar.

---

# Interview Answer

### What is an embedding?

```text
An embedding is a dense numerical vector representation of text that captures semantic meaning.

Similar words have similar vector representations.
```

---

# Topic 4: Vector Database

Very important for RAG interviews.

Examples:

* Pinecone
* Weaviate
* Chroma
* Milvus

---

### Why Normal Database Doesn't Work?

User asks:

```text
How can I reset my password?
```

Stored document:

```text
Steps to change account credentials
```

Keyword search may fail.

---

### Vector Search

Convert both into embeddings.

Find closest vectors.

Retrieve relevant documents based on meaning.

Not exact words.

---

# Interview Answer

### What is a Vector Database?

```text
A vector database stores embeddings and enables similarity search to retrieve semantically relevant information.
```

---

# Topic 5: RAG (Very Important)

You already worked with RAG, so know this thoroughly.

---

### Problem

LLMs:

```text
Can hallucinate
Knowledge cutoff
No access to private documents
```

---

### Solution

RAG

```text
Retrieve
↓
Augment
↓
Generate
```

---

### Flow

User Question

```text
What is my leave balance?
```

↓

Convert query into embedding

↓

Search vector database

↓

Retrieve relevant documents

↓

Pass documents + question to LLM

↓

Generate answer

---

### Benefits

```text
Reduces hallucination
Uses latest data
Uses enterprise knowledge
```

---

# Interview Question

### How does RAG reduce hallucination?

Answer:

```text
RAG retrieves relevant external information and provides it as context to the LLM before generation. Since the model answers using retrieved facts rather than relying solely on its internal knowledge, hallucinations are reduced.
```

---

# Today's Revision Checklist

## Transformers

✅ Why Transformers replaced RNNs

## Self-Attention

✅ Definition

✅ Example

## Embeddings

✅ What and why

## Vector DB

✅ Purpose

✅ Similarity Search

## RAG

✅ Architecture

✅ Hallucination Reduction

---

# Quick Interview Questions

Answer these in your own words:

1. What is Self-Attention?
2. What is an Embedding?
3. Why do we need a Vector Database?
4. What are the 3 steps in RAG?
5. Why are Transformers better than RNNs?

Try answering them without looking above. If you can answer all 5 confidently, you've completed Day 3 GenAI revision successfully. 🚀
