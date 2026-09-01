This is one of the most frequently asked GenAI interview topics today.

A lot of candidates say:

```text
RAG and Fine-Tuning are the same thing
```

which is incorrect.

---

# 1. Prompt Engineering vs Fine-Tuning

## Prompt Engineering

You do NOT change model weights.

You only change instructions.

Example:

```text
You are a helpful banking assistant.
Answer in bullet points.
```

Model remains:

```text
GPT-4
Claude
Llama
```

unchanged.

---

### Advantages

```text
Cheap
Fast
No training required
Easy to update
```

---

### Disadvantages

```text
Limited customization
May not fully learn company-specific behavior
```

---

## Fine-Tuning

You train the model on your own examples.

Example:

```text
Input:
Customer wants refund

Output:
Follow company refund policy...
```

Thousands of such examples are used.

The model weights are updated.

---

### Advantages

```text
Learns specific behavior
Consistent outputs
Domain adaptation
```

---

### Disadvantages

```text
Expensive
Training required
Harder to maintain
```

---

## Interview Answer

### Prompt Engineering vs Fine-Tuning

```text
Prompt engineering modifies the instructions given to the model, while fine-tuning updates the model weights using training data.

Prompt engineering is faster and cheaper, whereas fine-tuning is useful when consistent domain-specific behavior is required.
```

---

# 2. SFT (Supervised Fine-Tuning)

This is usually the first stage of fine-tuning.

---

## Idea

Train using:

```text
Input → Correct Output
```

Example:

```text
Question:
What is AWS?

Answer:
AWS is Amazon's cloud platform...
```

---

Dataset:

```text
(Input, Output)
(Input, Output)
(Input, Output)
```

---

Model learns:

```text
When user says X
Generate Y
```

---

### Visual

```text
Base Model
      ↓
Training Examples
      ↓
SFT
      ↓
Instruction Following Model
```

---

# 3. Instruction Tuning

A special type of SFT.

Instead of learning facts, model learns:

```text
How to follow instructions
```

---

Example

```text
Summarize this text.

Translate to French.

Write Python code.
```

Thousands of instructions.

---

Result:

```text
Model becomes better at following commands.
```

---

### Example

Without instruction tuning:

```text
Question:
Summarize this paragraph.
```

May perform poorly.

With instruction tuning:

```text
Model understands task format.
```

---

# 4. RLHF

RLHF =

```text
Reinforcement Learning from Human Feedback
```

Used by ChatGPT and
