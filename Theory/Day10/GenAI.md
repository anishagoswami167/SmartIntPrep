Perfect. This is the level where GenAI interviews become interesting. Let's start with **Topic 1: Agentic AI** because Agent vs RAG is one of the most asked questions now.

# Topic 1: Agentic AI

## 1. What is an AI Agent?

### Simple Definition

An AI Agent is an LLM that can:

1. Reason
2. Decide
3. Take Actions
4. Use Tools
5. Observe Results
6. Continue until task completion

Unlike a normal chatbot, an Agent does not just answer—it can perform tasks.

---

### Example

User:

```text
Book the cheapest flight from Bangalore to Delhi next Friday.
```

Agent:

```text
Step 1: Search flights
Step 2: Compare prices
Step 3: Select cheapest
Step 4: Ask user confirmation
Step 5: Book ticket
```

This is Agentic behavior.

---

## 2. Difference Between Workflow and Agent

### Workflow

Predefined path.

```text
User
 ↓
Step A
 ↓
Step B
 ↓
Step C
```

Example:

```text
Document
 ↓
Chunk
 ↓
Embed
 ↓
Store
```

Same path every time.

---

### Agent

Dynamic path.

```text
User Query
 ↓
Reason
 ↓
Choose Tool
 ↓
Observe Result
 ↓
Choose Next Step
 ↓
Final Answer
```

Path changes depending on query.

---

### Interview Answer

Workflow:

```text
Deterministic
Fixed sequence
```

Agent:

```text
Dynamic
LLM decides next action
```

---

## 3. What is ReAct?

ReAct =

```text
Reason + Act
```

Most popular Agent framework.

---

### Flow

```text
Thought
 ↓
Action
 ↓
Observation
 ↓
Thought
 ↓
Action
 ↓
Answer
```

---

### Example

Question:

```text
What is the weather in Bangalore?
```

Agent:

```text
Thought:
I need weather data.

Action:
Call Weather API

Observation:
28°C

Answer:
Current temperature is 28°C.
```

---

## 4. What is Tool Calling?

Tool Calling allows the LLM to use external tools.

Examples:

```text
Calculator
Weather API
Database
Search Engine
CRM System
```

---

### Example

User:

```text
What is 257 × 843?
```

Instead of guessing:

```text
Call Calculator Tool
```

Return exact result.

---

## 5. What is Function Calling?

Function Calling is a structured way of Tool Calling.

Example:

Tool:

```python
get_weather(city)
```

LLM generates:

```json
{
  "function":"get_weather",
  "arguments":{
      "city":"Bangalore"
  }
}
```

Application executes function and returns result.

---

### Interview Answer

```text
Function Calling is a specific implementation of Tool Calling.
```

---

## 6. What are Multi-Agent Systems?

Multiple specialized agents collaborate.

---

### Example

Travel Planner

Agent 1:

```text
Flight Agent
```

Agent 2:

```text
Hotel Agent
```

Agent 3:

```text
Budget Agent
```

Agent 4:

```text
Itinerary Agent
```

---

### Flow

```text
User
 ↓
Coordinator Agent
 ↓
Flight Agent
 ↓
Hotel Agent
 ↓
Budget Agent
 ↓
Final Plan
```

---

## 7. Agents vs RAG

### RAG

Purpose:

```text
Retrieve information
```

Flow:

```text
Question
 ↓
Retrieve Chunks
 ↓
LLM
 ↓
Answer
```

Good for:

```text
Knowledge Search
FAQs
Documentation
Policies
```

---

### Agent

Purpose:

```text
Take actions
```

Flow:

```text
Question
 ↓
Reason
 ↓
Tool Calls
 ↓
Actions
 ↓
Answer
```

Good for:

```text
Booking
API Calls
Automation
Decision Making
```

---

## Interview Question

### Why not use a simple RAG pipeline instead of an Agent?

### Answer

RAG can only retrieve information.

Example:

```text
What is the leave policy?
```

RAG works perfectly.

---

But:

```text
Apply leave for next Monday.
```

RAG cannot perform the action.

You need:

```text
Agent
 ↓
Call HR API
 ↓
Submit Leave Request
```

---

### Interview One-Liner

```text
Use RAG when you need knowledge retrieval.
Use Agents when you need reasoning and actions.
```

---

# Quick Revision

### AI Agent

```text
Reason + Decide + Act
```

### Workflow

```text
Fixed Path
```

### Agent

```text
Dynamic Path
```

### ReAct

```text
Reason → Act → Observe
```

### Tool Calling

```text
LLM uses external tools
```

### Function Calling

```text
Structured Tool Calling
```

### Multi-Agent

```text
Multiple specialized agents collaborate
```

### RAG

```text
Retrieve Information
```

### Agent

```text
Take Actions
```

---

### Mini Mock Interview

Answer this in your own words:

> A user asks:
>
> "What is my current bank balance and transfer ₹5000 to my savings account."
>
> Would you use:
>
> 1. RAG
> 2. Tool Calling
> 3. Agent
>
> Explain why.
