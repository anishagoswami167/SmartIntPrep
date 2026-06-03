Perfect. Since you've already finished Day 2 coding, let's use the next 45 minutes to build **interview-ready GenAI answers**, not just definitions.

---

# Topic 1: LLM (Large Language Model)

## Q1. What is an LLM?

**Simple Answer:**

An LLM (Large Language Model) is an AI model trained on massive amounts of text data to understand and generate human-like language. It predicts the next most likely token (word/subword) based on the context it has seen.

**Interview Answer:**

> A Large Language Model is a deep learning model, typically based on the Transformer architecture, trained on large-scale text datasets. It learns language patterns, grammar, reasoning abilities, and world knowledge, enabling it to perform tasks such as question answering, summarization, translation, code generation, and conversational AI.

---

## Q2. How is it Different from Traditional ML?

| Traditional ML                               | LLM                            |
| -------------------------------------------- | ------------------------------ |
| Uses structured data                         | Uses large text datasets       |
| Task-specific                                | General-purpose                |
| Requires feature engineering                 | Learns features automatically  |
| Separate model per task                      | Same model performs many tasks |
| Examples: Logistic Regression, Random Forest | GPT, Claude, Gemini, Llama     |

### Interview Answer

> Traditional ML models are trained for specific tasks using structured features, whereas LLMs learn language representations from massive unstructured text and can perform multiple tasks through prompting without retraining.

---

## Q3. Examples of LLMs

Use entity references for exploration:

* GPT-4
* Claude
* Gemini
* Llama
* Mistral

---

## Q4. What is a Token?

A token is the smallest unit processed by an LLM.

Example:

```text
I love coding
```

may become:

```text
["I", "love", "coding"]
```

or sometimes subwords:

```text
["cod", "ing"]
```

### Why Tokens Matter?

* Context window is measured in tokens.
* API pricing is usually token-based.
* Input + Output = Total Tokens.

### Interview Answer

> A token is the basic unit of text processed by an LLM. Tokens may represent words, parts of words, punctuation, or special symbols. LLMs operate on tokens rather than entire sentences.

---

# Topic 2: Prompt Engineering

## What is Prompt Engineering?

Prompt Engineering is the practice of designing instructions that help an LLM generate better and more accurate outputs.

---

## Zero-Shot Prompting

No examples given.

Input:

```text
Translate English to French:
Hello
```

Output:

```text
Bonjour
```

The model relies only on its pre-trained knowledge.

---

## One-Shot Prompting

One example is provided.

Input:

```text
English: Hello
French: Bonjour

English: Thank you
French:
```

Output:

```text
Merci
```

The model learns the expected format from one example.

---

## Few-Shot Prompting

Multiple examples provided.

Input:

```text
English: Hello
French: Bonjour

English: Thank you
French: Merci

English: Good Morning
French:
```

Output:

```text
Bonjour
```

---

## Interview Question

### Why does Few-Shot Prompting improve results?

**Answer:**

> Few-shot prompting gives the model examples of the desired format and behavior, helping it understand the task more accurately and produce more consistent outputs.

---

# Topic 3: Temperature

Temperature controls randomness in LLM responses.

---

## Temperature = 0

```text
Deterministic
```

Same input → nearly same output every time.

Example:

```text
2 + 2 = ?
```

Output:

```text
4
```

---

## Temperature = 1

```text
More Creative
```

Multiple possible responses.

Example:

```text
Write a story about a dragon.
```

Every run may produce a different story.

---

## Interview Question

### Why Keep Temperature Low in Customer Support Bots?

**Answer:**

> Customer support systems require accurate, consistent, and predictable responses. A low temperature reduces randomness and helps ensure users receive reliable information instead of creative variations.

### Real Example

Customer asks:

```text
How can I reset my password?
```

Temperature 0:

```text
Click Forgot Password and follow the instructions.
```

Temperature 1:

```text
There are several ways you might try...
```

Support bots should avoid unnecessary creativity.

---

# Topic 4: Hallucination

## What is Hallucination?

Hallucination occurs when an LLM generates information that sounds correct but is actually false, fabricated, or unsupported.

Example:

User asks:

```text
Who won the FIFA World Cup in 2050?
```

Model may invent an answer.

---

## Why Does Hallucination Happen?

LLMs do not truly "know" facts.

They predict the most likely next token based on patterns learned during training.

Reasons:

1. Missing knowledge
2. Ambiguous prompts
3. Outdated training data
4. No access to external sources

---

## How Does RAG Reduce Hallucination?

RAG = Retrieval-Augmented Generation.

### Without RAG

```text
User Question
       ↓
      LLM
       ↓
    Answer
```

The model relies only on its training data.

---

### With RAG

```text
User Question
       ↓
Retriever
       ↓
Relevant Documents
       ↓
LLM
       ↓
Answer
```

The model uses retrieved documents as evidence before generating a response.

---

### Interview Answer

> RAG reduces hallucination by retrieving relevant external information and providing it as context to the LLM. Instead of relying solely on training data, the model generates responses grounded in retrieved documents, improving factual accuracy.

---

# Quick 5-Minute Self-Test

Try answering these without looking:

1. Why are tokens important in LLMs?
2. Difference between Zero-Shot and Few-Shot prompting?
3. Why is temperature set low for banking/customer support bots?
4. What causes hallucinations?
5. How does RAG reduce hallucination?

If you can answer all five confidently, you've completed today's GenAI revision successfully. Tomorrow we can move to **Transformers, Embeddings, Vector Databases, RAG Architecture, and LangChain fundamentals**, which are heavily asked in GenAI interviews. 🚀
