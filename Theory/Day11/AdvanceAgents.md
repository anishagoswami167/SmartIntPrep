Perfect. This topic is becoming extremely important because companies are moving from:

```text id="3mfx4j"
Simple RAG
       ↓
Agentic AI
       ↓
Multi-Agent Systems
```

---

# Topic 3: Advanced Agent Design

---

# What is an AI Agent?

An AI Agent is an LLM that can:

```text id="4lq6q5"
Reason
Decide
Take Actions
Use Tools
Observe Results
```

Traditional LLM:

```text id="njm0iz"
Question
   ↓
Answer
```

Agent:

```text id="2bdg4u"
Question
   ↓
Reason
   ↓
Use Tool
   ↓
Observe
   ↓
Answer
```

---

Example:

User:

```text id="13xyv1"
What's the weather in Bangalore?
```

LLM alone:

```text id="hj6l2u"
May hallucinate
```

Agent:

```text id="jrz5jl"
Call Weather API
↓
Get Real Data
↓
Answer
```

---

# Planner Agent

Think:

```text id="sxqgnd"
Planner = Project Manager
```

Job:

```text id="2vm39x"
Break task into steps
```

---

Example:

User:

```text id="m6dc8u"
Plan a 3-day Goa trip.
```

Planner creates:

```text id="pxu6wz"
Step 1: Find flights
Step 2: Find hotels
Step 3: Create itinerary
Step 4: Estimate budget
```

Planner usually does NOT execute.

It only plans.

---

Architecture:

```text id="pfslm0"
User Query
     ↓
Planner Agent
     ↓
Task List
```

---

# Executor Agent

Think:

```text id="lsm9vd"
Worker
```

Job:

```text id="36fj1y"
Execute tasks created by Planner
```

---

Example:

Planner:

```text id="2dw7ns"
Find flights
```

Executor:

```text id="l79g8g"
Calls Flight API
```

Planner:

```text id="yj43q8"
Find hotel
```

Executor:

```text id="jlwmf0"
Calls Hotel Search API
```

---

Architecture:

```text id="j3sg9u"
Planner
   ↓
Executor
   ↓
Tool Calls
```

---

# Critic Agent

Think:

```text id="gikx4x"
Quality Checker
```

Job:

```text id="tgvkm7"
Review output
Find mistakes
Suggest improvements
```

---

Example:

Generated answer:

```text id="sjj2bh"
Goa trip costs ₹500
```

Critic:

```text id="0c4juv"
Too low.
Missing hotel costs.
```

---

Architecture:

```text id="cnxg0h"
Executor
   ↓
Output
   ↓
Critic
```

---

# Reflection Agent

Very hot interview topic.

Think:

```text id="s5g4ev"
Self-improvement agent
```

---

Instead of checking another agent's work:

```text id="w8nfg0"
It checks its own work.
```

---

Example:

Agent generates:

```text id="0wkho4"
Answer A
```

Then asks itself:

```text id="06w15r"
Is this answer complete?
Did I miss anything?
```

Then improves answer.

---

Flow:

```text id="s75xj6"
Generate
 ↓
Reflect
 ↓
Improve
 ↓
Final Answer
```

---

# Agent Loops

Traditional Workflow:

```text id="7a3wm4"
A → B → C
```

One direction.

---

Agent Workflow:

```text id="e2hrxm"
Planner
  ↓
Executor
  ↓
Critic
  ↓
Back to Executor
```

Loop.

---

Example:

```text id="1c36y7"
Generate Report
 ↓
Critic says incomplete
 ↓
Generate Again
 ↓
Critic reviews
 ↓
Approved
```

---

This is why LangGraph became popular.

It supports:

```text id="knlqjw"
Cycles
Loops
State
Retries
```

---

# Failure Recovery

Real systems fail.

Examples:

```text id="0l4u6p"
API Timeout
Tool Failure
Database Error
Bad Retrieval
```

---

Agent should recover.

---

Example:

Weather API fails.

Agent:

```text id="q9wvz4"
Retry
```

Still fails.

Agent:

```text id="f4l41v"
Use backup API
```

Still fails.

Agent:

```text id="kgjs4g"
Tell user service unavailable
```

---

This is Failure Recovery.

---

# Multi-Agent Systems

Instead of one huge agent:

```text id="4n3zj8"
One Agent Does Everything
```

Use specialists.

---

Example:

Travel Planning System

Planner Agent

```text id="4b8es3"
Creates tasks
```

Flight Agent

```text id="09wx6y"
Finds flights
```

Hotel Agent

```text id="v9wqqf"
Finds hotels
```

Budget Agent

```text id="dh4g8e"
Calculates cost
```

Critic Agent

```text id="9sm6kj"
Reviews final itinerary
```

---

Architecture:

```text id="t7k9g3"
              Planner
                 ↓
   ┌─────────────┼─────────────┐
   ↓             ↓             ↓

Flight      Hotel       Budget
Agent       Agent       Agent

   └─────────────┼─────────────┘
                 ↓

             Critic
                 ↓

             Response
```

---

# Why Multi-Agent?

Benefits:

```text id="qgngaq"
Specialization
Better Accuracy
Scalability
Parallel Execution
Easier Maintenance
```

---

# LangGraph Mapping

Very common interview question.

```text id="g6ukht"
Node = Agent

Edge = Transition

State = Shared Memory

Conditional Edge = Routing Logic

Cycle = Agent Loop
```

---

# Quick Revision Notes

## Agent Types

```text id="j8hjhq"
Planner Agent
→ Creates plan

Executor Agent
→ Executes tasks

Critic Agent
→ Reviews output

Reflection Agent
→ Self-evaluates output
```

---

## Advanced Concepts

```text id="4lsj63"
Agent Loop
→ Repeat until success

Failure Recovery
→ Retry/Fallback

Multi-Agent System
→ Specialized agents working together
```

---

## Memory Trick

```text id="y1o66r"
Planner   = Think

Executor  = Do

Critic    = Review

Reflection = Improve Yourself
```

---
