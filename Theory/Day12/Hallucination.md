This is one of the most important interview topics because **hallucination is the biggest challenge in enterprise GenAI systems**.

Since you've worked on chatbots, RAG, AWS Bedrock, and customer support use cases, interviewers often ask:

> "How would you prevent the model from making up information?"

---

# 1. Why Do Hallucinations Happen?

## Simple Definition

A hallucination occurs when:

```text
The model generates information
that sounds correct
but is actually wrong or unsupported.
```

---

## Example

User:

```text
What is my bank account balance?
```

LLM:

```text
Your balance is ₹45,000.
```

Problem:

```text
The model has no access to your account.
It invented the answer.
```

---

## Why Does This Happen?

Because LLMs are:

```text
Next-word predictors
```

They do NOT inherently know:

```text
True
False
Current
User-specific
```

They only predict:

```text
What text is likely next.
```

---

## Common Causes

### 1. Missing Knowledge

User asks:

```text
What happened yesterday?
```

Training data may be old.

Model guesses.

---

### 2. Missing Context

User asks:

```text
What is my account balance?
```

No account data provided.

Model invents.

---

### 3. Ambiguous Questions

User:

```text
What is the policy?
```

Which policy?

Model may assume incorrectly.

---

# 2. Retrieval-Based Grounding

This is the #1 enterprise solution.

Instead of relying only on model memory:

```text
User Question
      ↓
Retrieve Documents
      ↓
Provide Context
      ↓
LLM Generates Answer
```

---

## Example

Without RAG

```text
User:
What is our company's refund policy?

LLM:
Maybe 30 days...
```

Hallucination risk.

---

## With RAG

Retrieve:

```text
Refund policy document
```

Pass to model:

```text
Context:
Refunds are allowed within 14 days.
```

Answer:

```text
Refunds are allowed within 14 days.
```

Much safer.

---

## Interview Answer

```text
Grounding reduces hallucination by forcing the model to answer using retrieved enterprise documents instead of relying solely on its pre-trained knowledge.
```

---

# 3. Guardrails

Guardrails are rules that control behavior.

Think:

```text
Input Protection
Output Protection
```

---

## Example

User:

```text
Tell me another customer's account number.
```

Guardrail:

```text
Blocked
```

---

## Example

Model generates:

```text
Customer SSN: 123-45-6789
```

Guardrail:

```text
PII Detection
↓
Redact
```

---

### AWS Bedrock

You've already worked with:

* Guardrails
* PII masking
* Sensitive data filtering

This is a perfect real-world example.

---

# 4. Verification Chains

Idea:

```text
Generate Answer
↓
Verify Answer
↓
Return Only If Valid
```

---

## Example

Agent 1:

```text
Generates answer
```

Agent 2:

```text
Checks evidence
```

---

Visual:

```text
Question
    ↓
Answer Agent
    ↓
Verifier Agent
    ↓
Final Response
```

---

## Example

Answer:

```text
Refund policy = 30 days
```

Verifier checks document:

```text
Document says 14 days
```

Result:

```text
Answer rejected
```

---

# 5. Self-Checking Agents

A more advanced version.

The model reviews its own response.

---

Prompt:

```text
Generate answer.

Then verify:
1. Is answer supported by context?
2. Any unsupported claims?
3. Any missing evidence?
```

---

Example

First response:

```text
Refunds are allowed for 30 days.
```

Self-check:

```text
Evidence not found.
```

Correction:

```text
Refunds are allowed for 14 days.
```

---

## Used In

* Self-RAG
* CRAG
* Reflection Agents

---

# 6. Confidence Scoring

Instead of blindly answering:

```text
Answer + Confidence
```

---

Example

```text
Answer:
Refunds allowed within 14 days.

Confidence:
95%
```

---

Another:

```text
Answer:
I am unable to find enough information.

Confidence:
25%
```

---

If confidence is low:

```text
Escalate
Ask clarification
Search again
Route to human
```

---

# Banking Chatbot Example

User:

```text
Can I increase my credit card limit?
```

Bad chatbot:

```text
Yes, your limit is increased.
```

Hallucination.

---

Better architecture:

```text
User
 ↓
Intent Detection
 ↓
API Call
 ↓
Bank Data
 ↓
LLM
 ↓
Response
```

The LLM never invents the limit.

It only summarizes actual API results.

---

# Interview Question

## How would you reduce hallucinations in a banking chatbot?

### Strong Answer

```text
I would use retrieval-based grounding and API-driven responses rather than relying on the model's memory.

For policy-related questions, I would implement a RAG system that retrieves information from approved banking documents.

For account-specific information such as balances or transactions, I would use tool calling or backend APIs instead of allowing the LLM to generate answers.

I would also add guardrails for PII protection, confidence scoring to identify uncertain responses, and verification layers to ensure generated answers are supported by retrieved evidence before being shown to the customer.
```

---

# Hallucination Reduction Cheat Sheet

```text
Why Hallucinations Happen:
- Missing knowledge
- Missing context
- Ambiguous questions
- LLM predicts text, not truth

Reduction Techniques:

1. RAG / Grounding
   → Retrieve real documents

2. Tool Calling
   → Use APIs for real-time data

3. Guardrails
   → PII protection
   → Toxicity filtering

4. Verification Chains
   → Answer agent + verifier agent

5. Self-Checking Agents
   → Model reviews itself

6. Confidence Scoring
   → Detect uncertainty

Banking Best Practice:
Policies → RAG
Account Data → API Calls
PII → Guardrails
Low Confidence → Human Escalation
```

### Quick Check

A customer asks:

```text
"What was my last transaction?"
```

Would you use:

**A. RAG**
**B. Tool Calling / API**
**C. Fine-Tuning**

And why? This is a very common interview question.
