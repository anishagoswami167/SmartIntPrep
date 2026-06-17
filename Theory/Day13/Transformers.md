Perfect. Let's dedicate today entirely to **Transformers** and cover 5 major topics in depth.

# Transformer Deep Dive - Day 1

## Topic 1: Why Transformers Were Invented

### Before Transformers

### RNN

```text
I → love → learning → AI
```

Processes one word at a time.

Problem:

```text
Sequential processing
```

Cannot process words in parallel.

---

### Long-Term Dependency Problem

Example:

```text
The movie that I watched last week with my friends was fantastic.
```

When predicting:

```text
fantastic
```

the model should remember:

```text
movie
```

But RNN struggles with long distances.

---

### LSTM

Introduced memory cells.

Better than RNN.

Still:

```text
Sequential
Slow
Hard to parallelize
```

---

### Transformer Idea

Instead of:

```text
Word1 → Word2 → Word3 → Word4
```

Use:

```text
Every word looks at every other word
```

at the same time.

This is called:

```text
Self-Attention
```

---

# Topic 2: Self-Attention Intuition

Sentence:

```text
The cat sat on the mat
```

When processing:

```text
cat
```

Model asks:

```text
Which words help me understand cat?
```

Maybe:

```text
The
cat
sat
```

Important.

Maybe:

```text
mat
```

Less important.

---

### Another Example

```text
The animal didn't cross the road because it was tired.
```

Question:

```text
Who is tired?
```

Transformer learns:

```text
it → animal
```

using attention.

This is why Transformers understand context much better than old NLP models.

---

# Topic 3: Query, Key, Value (QKV)

This is the heart of every interview.

Every word creates:

## Query (Q)

```text
What am I looking for?
```

## Key (K)

```text
What information do I contain?
```

## Value (V)

```text
What information should I give?
```

---

### Real-Life Analogy

Imagine LinkedIn.

You are looking for:

```text
GenAI Engineer jobs
```

Your search:

```text
Query
```

Job titles:

```text
Keys
```

Job descriptions:

```text
Values
```

You compare:

```text
Query vs Key
```

Best matching jobs return:

```text
Value
```

---

### Interview Answer

If asked:

> What are Query, Key and Value?

Answer:

```text
Each token is projected into Query, Key and Value vectors.
Queries determine what information a token seeks,
Keys represent what information tokens contain,
and Values contain the actual information passed to the next layer.
Attention is computed by comparing Queries and Keys and then weighting Values.
```

---

# Topic 4: Attention Score Calculation

Let's do actual math.

Suppose:

```text
Query = [1,0]
```

and

```text
Key1 = [1,0]
Key2 = [0,1]
```

Attention score:

```text
Q · K
```

Dot Product.

---

### Score 1

```text
[1,0] · [1,0]

=
1×1 + 0×0

=
1
```

---

### Score 2

```text
[1,0] · [0,1]

=
1×0 + 0×1

=
0
```

---

Result:

```text
Key1 = 1
Key2 = 0
```

Meaning:

```text
Key1 is more relevant
```

---

### Why Softmax?

Raw scores:

```text
[1,0]
```

Convert to probabilities:

```text
Softmax([1,0])

≈ [0.73, 0.27]
```

Now model says:

```text
73% attention to token 1
27% attention to token 2
```

---

# Topic 5: Multi-Head Attention

Single attention may focus on only one relationship.

Example:

```text
The bank approved the loan.
```

One attention head may learn:

```text
bank ↔ loan
```

Another head may learn:

```text
approved ↔ loan
```

Another head may learn:

```text
subject ↔ verb relationship
```

---

Instead of:

```text
1 attention mechanism
```

Transformer uses:

```text
Multiple attention heads
```

Typically:

```text
8
12
16
32
```

depending on model size.

---

### Why Multi-Head?

Different heads learn different relationships:

Head 1:

```text
Grammar
```

Head 2:

```text
Meaning
```

Head 3:

```text
Coreference
(it → animal)
```

Head 4:

```text
Subject-object relations
```

---

# Complete Flow So Far

```text
Input Sentence
        ↓
Tokenization
        ↓
Embeddings
        ↓
Q, K, V Creation
        ↓
Attention Scores
        ↓
Softmax
        ↓
Weighted Values
        ↓
Multi-Head Attention
```

---

# Interview Questions

### Q1

Why are Transformers better than RNNs?

### Q2

What is Self-Attention?

### Q3

What are Query, Key and Value?

### Q4

Why is Softmax used in Attention?

### Q5

Why do we need Multi-Head Attention?

---

Tomorrow's Transformer topics should be:

6. Positional Encoding
7. Feed Forward Network (FFN)
8. Encoder Architecture
9. Decoder Architecture
10. GPT vs BERT vs T5 (very important interview topic)

These 10 topics together cover about 80% of Transformer interview questions.
