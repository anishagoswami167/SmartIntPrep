
# 1. Transformer Architecture

### Q. Why were Transformers introduced? Why not RNNs/LSTMs?

### Answer

RNNs and LSTMs process text sequentially:

```text
Word1 → Word2 → Word3 → Word4
```

Problems:

* Slow training (cannot fully parallelize)
* Difficulty remembering long-range dependencies
* Vanishing/Exploding gradients

Transformers solve this using:

```text
Self-Attention
```

which allows every token to directly look at every other token.

### Interview One-Liner

> Transformers replaced RNNs because they process tokens in parallel and capture long-range dependencies using self-attention.

---

# 2. Self-Attention

### Q. What is Self-Attention?

### Answer

Self-attention allows a token to determine which other tokens are important for understanding its meaning.

Example:

```text
The cat sat on the mat.
```

The word:

```text
cat
```

may pay more attention to:

```text
sat
mat
```

than to:

```text
the
```

### Interview One-Liner

> Self-attention calculates relationships between tokens and assigns importance scores to relevant tokens.

---

# 3. Multi-Head Attention

### Q. Why use Multi-Head Attention?

### Answer

Different attention heads learn different relationships.

Example:

Sentence:

```text
The bank approved the loan.
```

One head may learn:

```text
bank ↔ loan
```

Another may learn:

```text
subject ↔ verb relationships
```

Multiple heads allow the model to understand language from multiple perspectives simultaneously.

### Interview One-Liner

> Multi-head attention allows the model to learn multiple types of relationships in parallel.

---

# 4. Tokenization

### Q. What is Tokenization?

### Answer

Tokenization is the process of breaking text into smaller units called tokens.

Example:

```text
I love ChatGPT
```

becomes:

```text
["I", "love", "Chat", "GPT"]
```

depending on the tokenizer.

---

### Q. Why not use words directly?

### Answer

Vocabulary would become huge.

Instead, models use subwords.

Example:

```text
unbelievable
```

can become:

```text
un
believe
able
```

This helps handle unseen words.

---

# 5. BPE (Byte Pair Encoding)

### Q. What tokenization technique does GPT use?

### Answer

GPT models use:

```text
Byte Pair Encoding (BPE)
```

BPE repeatedly merges frequently occurring character pairs into tokens.

Example:

```text
l + ow → low
low + er → lower
```

### Interview One-Liner

> BPE creates subword tokens, reducing vocabulary size while handling unknown words effectively.

---

# 6. Embeddings

### Q. What are Embeddings?

### Answer

Embeddings are dense numerical vector representations of text.

Example:

```text
Dog → [0.12, 0.88, -0.45, ...]
Cat → [0.15, 0.85, -0.40, ...]
```

Similar meanings produce similar vectors.

---

### Q. Why are embeddings important?

### Answer

They allow semantic similarity search.

Example:

```text
Car
Automobile
Vehicle
```

will have similar vectors.

---

# 7. Positional Encoding

### Q. Why do Transformers need Positional Encoding?

### Answer

Transformers process tokens in parallel.

Without positional information:

```text
I love AI
```

and

```text
AI love I
```

would appear identical.

Positional encoding tells the model where each token occurs.

### Interview One-Liner

> Positional encoding injects word-order information into Transformers.

---

# 8. Encoder vs Decoder

### Q. Difference between Encoder and Decoder?

| Encoder           | Decoder          |
| ----------------- | ---------------- |
| Understands input | Generates output |
| Bidirectional     | Autoregressive   |
| BERT              | GPT              |

---

### Q. What type is GPT?

### Answer

```text
Decoder-Only Transformer
```

GPT predicts the next token repeatedly.

---

# 9. Context Window

### Q. What is Context Window?

### Answer

The maximum number of tokens the model can consider in one request.

Example:

```text
128K tokens
```

means the model can use up to 128,000 tokens of context.

### Problem

If information exceeds the context window:

```text
Older information gets dropped.
```

---

# 10. Temperature

### Q. What does Temperature control?

### Answer

Controls randomness of generation.

Low temperature:

```text
0.1
```

* Deterministic
* Consistent
* Preferred for customer support bots

High temperature:

```text
1.0
```

* Creative
* Diverse
* Better for content generation

### Interview One-Liner

> Temperature controls randomness in token selection.

---

# 11. Why LLMs Are Stateless

### Q. Are LLMs Stateful?

### Answer

No.

Each API call is independent.

Example:

Request 1:

```text
My name is Anisha
```

Request 2:

```text
What is my name?
```

The model will not know unless previous conversation is sent again.

### How We Handle Memory

* Conversation history
* Databases
* Redis
* Vector databases
* LangGraph memory

### Interview One-Liner

> LLMs are stateless; memory must be managed externally by the application.

---

# Most Asked Interview Questions From This Section

1. Why Transformers over RNNs?
2. What is Self-Attention?
3. What is Multi-Head Attention?
4. What is Tokenization?
5. What is BPE?
6. What are Embeddings?
7. Why Positional Encoding?
8. Encoder vs Decoder?
9. Why is GPT Decoder-only?
10. What is Context Window?
11. Why are LLMs Stateless?
12. What is Temperature?

Tomorrow we can continue with the next high-value topics:

* RAG Deep Dive
* Vector Databases
* Hybrid Search (BM25 + Dense Retrieval)
* Rerankers
* Multi-Document RAG
* GraphRAG
* Agentic AI & LangGraph
* Function Calling / Tool Calling
* Fine-tuning, LoRA, QLoRA

These are the topics currently appearing most often in GenAI Engineer interviews. 🚀
