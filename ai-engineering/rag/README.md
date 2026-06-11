[![RAG & Embeddings](../../assets/hub_banner.png)](../../README.md)

# Introduction to Embeddings with the OpenAI API

> This space tracks my learning notes and practical implementations for the **Introduction to Embeddings with the OpenAI API** course, covering semantic vector generation, distance metrics, classification/clustering on embeddings, and vector databases.

[![Embeddings](https://img.shields.io/badge/Embeddings-OpenAI-black?logo=openai&style=flat-square)](https://platform.openai.com)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)](../../README.md)

---

## 📂 What's in this folder

| File | Type / Access Badge | Description | Status |
| :--- | :--- | :--- | :--- |
| `embeddings_openai_api.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&style=flat-square)](embeddings_openai_api.ipynb) | Interactive notebook covering vector generation, distance calculations, and clustering. | ✅ Done |
| `README.md` | [![Markdown](https://img.shields.io/badge/Doc-Markdown-red?logo=markdown&style=flat-square)](README.md) | This document (comprehensive embeddings course notes, code summaries, and vector math). | ✅ Done |

---

## 🧮 Theoretical & Mathematical Foundations

### 1. Vector Distance & Similarity Metrics
Embeddings are represented as dense float vectors $u, v \in \mathbb{R}^D$, where $D$ is the dimensionality of the vector space. We calculate the semantic similarity of texts by calculating the distance between their vectors:

*   **Cosine Similarity:**
    Measures the cosine of the angle between two vectors. Values range from -1 to 1:
    $$\text{sim}(u, v) = \cos(\theta) = \frac{u \cdot v}{\|u\| \|v\|} = \frac{\sum_{i=1}^D u_i v_i}{\sqrt{\sum_{i=1}^D u_i^2} \sqrt{\sum_{i=1}^D v_i^2}}$$
*   **Dot Product Similarity:**
    If the vectors are normalized ($\|u\| = \|v\| = 1$), the cosine similarity simplifies to the dot product:
    $$\text{sim}(u, v) = u \cdot v = \sum_{i=1}^D u_i v_i$$
*   **Euclidean (L2) Distance:**
    Measures the straight-line distance between two points in Euclidean space:
    $$d(u, v) = \sqrt{\sum_{i=1}^D (u_i - v_i)^2}$$

---

### 2. t-Distributed Stochastic Neighbor Embedding (t-SNE)
Used to visualize high-dimensional embedding spaces in 2D or 3D. t-SNE maps vector similarities to conditional probabilities representing similarities:
$$p_{j|i} = \frac{\exp\left(-\|x_i - x_j\|^2 / 2\sigma_i^2\right)}{\sum_{k \neq i} \exp\left(-\|x_i - x_k\|^2 / 2\sigma_i^2\right)}$$
Where $\sigma_i$ is the variance of the Gaussian centered on datapoint $x_i$.

---

## 📔 Chapter-by-Chapter Course Summaries

### Chapter 1: What are Embeddings?
Embeddings are numerical vector representations of text that capture semantic and contextual meaning.
*   **API Model Options:**
    1.  `text-embedding-3-small` (Default, 1536 dimensions, highly efficient).
    2.  `text-embedding-3-large` (Up to 3072 dimensions, highly precise).
*   **Code Example:**
    ```python
    from openai import OpenAI
    client = OpenAI(api_key="your-api-key")

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input="Machine learning models require clean numerical features."
    )
    
    embedding = response.data[0].embedding
    print(f"Dimension size: {len(embedding)}")  # Outputs: 1536
    print(f"Vector preview: {embedding[:5]}")
    ```

---

### Chapter 2: Semantic Similarity Search
Finding document chunks matching a user query by calculating cosine distances.
*   **Code Example (Using Pandas & NumPy):**
    ```python
    import numpy as np
    import pandas as pd

    # Mock database of embeddings
    data = pd.DataFrame({
        "text": ["A cat is sitting on a rug.", "Deep neural networks are cool.", "The weather is sunny today."],
        "embedding": [...]  # Pre-calculated 1536-dim lists
    })

    # User Query
    query_vector = client.embeddings.create(
        model="text-embedding-3-small",
        input="feline resting on carpet"
    ).data[0].embedding

    # Compute Cosine Similarity
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    data["similarity"] = data["embedding"].apply(lambda x: cosine_similarity(query_vector, x))
    sorted_data = data.sort_values(by="similarity", ascending=False)
    print(sorted_data[["text", "similarity"]].head(1))
    ```

---

### Chapter 3: Classification & Clustering on Embeddings
Using embeddings as feature matrices ($X$) for classical Scikit-learn models.
*   **Code Example (Supervised Classification):**
    ```python
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report

    # X is the matrix of embedding vectors, y is the class label
    X = np.array(data["embedding"].to_list())
    y = data["label"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    
    predictions = clf.predict(X_test)
    print(classification_report(y_test, predictions))
    ```

---

### Chapter 4: Retrieval-Augmented Generation (RAG) Flow
Integrating vector searches with LLMs to provide context-accurate generation.
1.  **Retrieve:** Generate query embedding and query a vector database (e.g. ChromaDB) to fetch top $k$ related text chunks.
2.  **Augment:** Insert the fetched text chunks directly into the model's system prompt context.
3.  **Generate:** Call the chat completions endpoint to answer the query.

---

## 🎯 Navigation

`[← LLM APIs](../llm-apis/README.md) | [Next: Agents](../agents/README.md)`
