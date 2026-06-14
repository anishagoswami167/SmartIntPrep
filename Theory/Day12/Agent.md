Excellent topic. This is exactly where interviews are heading now, especially for GenAI Engineer, Conversational AI Engineer, and Agentic AI roles.

---

# Why Multiple Agents?

Suppose a user asks:

```text
Create a project handover document from these meeting transcripts,
generate FAQs,
and identify knowledge gaps.
```

One agent can do it.

But multiple specialized agents often perform better:

```text
Planner
↓
Summarizer
↓
FAQ Generator
↓
Knowledge Gap Analyzer
↓
Reviewer
```

This is called a **Multi-Agent System**.

---

# 1. Planner Agent

Think of it as:

```text
Project Manager Agent
```

It doesn't do the work.

It decides:

```text
What needs to be done?
In what order?
Which agent should do it?
```

---

### Example

User:

```text
Plan a trip to Japan.
```

Planner creates:

```text
1. Find flights
2. Find hotels
3. Create itinerary
4. Estimate budget
```

Then routes work.

---

### Visual

```text
User Request
      ↓
Planner Agent
      ↓
Task List
      ↓
Other Agents
```

---

# 2. Executor Agent

This is the worker.

It performs actual tasks.

Examples:

```text
Search documents
Call APIs
Generate summary
Create report
```

---

### Example

Planner:

```text
Summarize transcript.
```

Executor:

```text
Reads transcript
Generates summary
```

---

### Visual

```text
Planner
   ↓
Executor
   ↓
Result
```

---

# 3. Critic Agent

Think:

```text
Quality Checker
```

Its job:

```text
Find mistakes
Verify outputs
Identify missing information
```

---

### Example

Executor generates:

```text
Refund policy = 30 days
```

Critic checks source:

```text
Actual policy = 14 days
```

Flags error.

---

### Visual

```text
Executor
   ↓
Output
   ↓
Critic
   ↓
Approved / Rejected
```

---

# 4. Reflection Pattern

Reflection means:

```text
Agent evaluates itself
```

Instead of another critic agent.

---

### Example

Agent generates:

```text
Meeting Summary
```

Then asks itself:

```text
Did I miss action items?
Did I miss decisions?
Is this supported by transcript?
```

---

### Flow

```text
Generate
 ↓
Review
 ↓
Improve
 ↓
Return
```

---

### Interview Definition

```text
Reflection is a pattern where an agent evaluates and improves its own output before returning the final response.
```

---

# 5. Supervisor Agent

Very common in LangGraph.

Think:

```text
Manager of Agents
```

It doesn't perform tasks.

It coordinates agents.

---

### Example

Agents:

```text
Research Agent
Writing Agent
Review Agent
```

Supervisor decides:

```text
Who should work next?
```

---

### Visual

```text
Supervisor
   ↓
Research Agent
   ↓
Writing Agent
   ↓
Review Agent
```

---

# 6. Agent Orchestration

Orchestration means:

```text
Managing workflow between agents
```

---

### Example

Without orchestration

```text
Agent A
Agent B
Agent C
```

No coordination.

---

### With orchestration

```text
Agent A
   ↓
Agent B
   ↓
Agent C
```

Controlled workflow.

---

### LangGraph

This is exactly why LangGraph exists.

It provides:

```text
State Management
Routing
Agent Coordination
Loops
Human Approval
```

---

# Common Architecture

```text
User
 ↓
Planner
 ↓
Executor
 ↓
Critic
 ↓
Final Answer
```

---

# Interview Question

## Design a Multi-Agent Knowledge Transfer Assistant

This matches your project idea almost perfectly.

---

### Problem

When an employee leaves:

```text
Meeting Notes
Documents
Recordings
FAQs
Processes
```

Need knowledge transfer.

---

### Architecture

```text
                    User
                      ↓
              Supervisor Agent
                      ↓
        ----------------------------
        |            |            |
        ↓            ↓            ↓
 Document      Transcript     FAQ Agent
 Agent         Agent
        ↓            ↓
        ----------------
                ↓
        Knowledge Gap Agent
                ↓
          Critic Agent
                ↓
         Final KT Report
```

---

# Agent Responsibilities

## 1. Supervisor Agent

```text
Receives request
Coordinates workflow
Routes tasks
```

---

## 2. Document Agent

```text
Reads SOPs
Reads PDFs
Extracts key knowledge
```

---

## 3. Transcript Agent

```text
Processes meetings
Generates summaries
Extracts decisions
```

---

## 4. FAQ Agent

Creates:

```text
Frequently Asked Questions
```

Example:

```text
How is deployment performed?
How are incidents handled?
```

---

## 5. Knowledge Gap Agent

Finds:

```text
Missing documentation
Missing ownership
Missing processes
```

---

## 6. Critic Agent

Validates:

```text
Completeness
Consistency
Coverage
```

---

# Interview Answer

### Design a Multi-Agent Knowledge Transfer Assistant

```text
I would use a supervisor-agent architecture.

The supervisor agent would coordinate specialized agents such as a document analysis agent, transcript summarization agent, FAQ generation agent, and knowledge-gap detection agent.

The document and transcript agents would extract knowledge from available sources. The FAQ agent would generate common operational questions, while the knowledge-gap agent would identify missing documentation or processes.

Finally, a critic agent would validate completeness and consistency before generating the final knowledge transfer report.

LangGraph would be a good choice for implementing orchestration, state management, and routing between these agents.
```

---

# Cheat Sheet

```text
Planner Agent
→ Creates task plan

Executor Agent
→ Performs work

Critic Agent
→ Reviews output

Reflection Pattern
→ Self-review

Supervisor Agent
→ Coordinates agents

Agent Orchestration
→ Controls workflow between agents

Typical Flow:

User
 ↓
Planner/Supervisor
 ↓
Executors
 ↓
Critic
 ↓
Final Response
```

---

### Quick Check

Suppose you're building an AI Travel Planner.

Which agent would be responsible for each?

```text
Task 1:
Create itinerary

Task 2:
Check whether itinerary is realistic

Task 3:
Decide whether to call Flight Agent or Hotel Agent first
```

Which would be:

* Planner Agent?
* Executor Agent?
* Critic Agent?

Try answering before we move to Topic 5 (LLM Evaluation Frameworks).
