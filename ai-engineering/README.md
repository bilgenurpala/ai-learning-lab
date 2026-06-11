[![AI Engineering](../assets/hub_banner.png)](../README.md)

# AI Engineering & Agents

> This space tracks my Phase 4 journey, focusing on LLM integrations, Retrieval-Augmented Generation (RAG) structures, Vector Databases, Semantic Search, and autonomous Tool-Calling LLM Agents.

[![Stack](https://img.shields.io/badge/Stack-LangChain--Chroma-blue?logo=googlecolab&logoColor=white&style=flat-square)](../README.md)
[![Status](https://img.shields.io/badge/Status-Upcoming-lightgrey?style=flat-square)](../README.md)

---

## 📂 What's in this folder

| Directory | Type / Access Badge | Description | Status |
| :--- | :--- | :--- | :--- |
| `llm-apis/` | [![Folder](https://img.shields.io/badge/Folder-APIs-purple?logo=github&style=flat-square)](llm-apis/) | direct LLM interactions, completion models, and token utilization strategies. | ⏳ Upcoming |
| `rag/` | [![Folder](https://img.shields.io/badge/Folder-RAG-purple?logo=github&style=flat-square)](rag/) | Vector store pipelines, document chunking, indexing, and context augmentation. | ⏳ Upcoming |
| `agents/` | [![Folder](https://img.shields.io/badge/Folder-Agents-purple?logo=github&style=flat-square)](agents/) | ReAct loops, tool definitions, structured outputs, and LLM memories. | ⏳ Upcoming |

---

## 🧮 Theoretical & Mathematical Foundations

AI Engineering builds bridges between raw LLMs and contextual enterprise data using vector calculations and probabilistic parsing.

### 1. Retrieval-Augmented Generation (RAG) Mathematics
RAG addresses LLM hallucinations by retrieving relevant factual documents from an external corpus before generation.

1.  **Vector Embedding Space:**
    A query $q$ and target documents $d_i$ are mapped to dense vector spaces using an embedding encoder:
    $$\vec{q} = \text{embed}(q), \quad \vec{d}_i = \text{embed}(d_i)$$
2.  **Semantic Similarity Metric (Cosine Similarity):**
    We calculate the similarity score between the query vector and all document vectors:
    $$\text{sim}(\vec{q}, \vec{d}_i) = \cos(\theta) = \frac{\vec{q} \cdot \vec{d}_i}{\|\vec{q}\| \|\vec{d}_i\|} = \frac{\sum_{j=1}^D q_j d_{i,j}}{\sqrt{\sum_{j=1}^D q_j^2} \sqrt{\sum_{j=1}^D d_{i,j}^2}}$$
3.  **Context Assembly:**
    Retrieve the top-$k$ documents with the highest similarity scores, compiling context $C$:
    $$C = \{ d_i \mid \text{rank}(\text{sim}(\vec{q}, \vec{d}_i)) \le k \}$$
4.  **Conditioned Generation:**
    The generated response $y$ is computed by sampling from the language model's vocabulary, conditioned on the combined prompt (user query $q$ and context $C$):
    $$y \sim P(y \mid q, C)$$

---

### 2. Autonomous Agentic Systems & Tool-Calling Loops
An AI Agent uses an LLM as a central controller to plan actions, use external tools, and evaluate observations (ReAct paradigm).

*   **Reasoning-Action (ReAct) Loop:**
    ```text
    [User Input] → [Thought: Reason about next steps] → [Action: Call Tool(args)] 
                      ↑                                        ↓
                 [New Thought] ← [Observation: Tool Output] ← [Execute Tool]
    ```
*   The LLM formats a JSON or function-calling payload, executes the tool, feeds the output back into the conversation context as an `Observation`, and continues the loop until the final answer is compiled.

---

## 🎯 Navigation

`[← Deep Learning](../deep-learning/) | [Next: Cybersecurity →](../cybersecurity/)`
