[![Cybersecurity & AI Security](../assets/cybersecurity_banner.png)](../README.md)

# Cybersecurity & AI Security

> This space tracks my parallel journey in mastering Cybersecurity and AI Security through network protocol analysis, log wrangling, and machine learning threat intelligence.

[![Track](https://img.shields.io/badge/Track-Parallel-red?logo=target&logoColor=white&style=flat-square)](../README.md)
[![Status](https://img.shields.io/badge/Status-Starting-orange?style=flat-square)](../README.md)

---

## 📂 What's in this folder

| File / Subfolder | Type / Access Badge | Description | Status |
| :--- | :--- | :--- | :--- |
| `datacamp-notes/intro_to_cyber.md` | [![Markdown](https://img.shields.io/badge/Doc-Markdown-red?logo=markdown&style=flat-square)](datacamp-notes/intro_to_cyber.md) | Principles of cyber safety, cryptography basics, and the CIA Triad. | 🔄 Starting |
| `datacamp-notes/intro_to_data_security.ipynb` | [![Notebook](https://img.shields.io/badge/Jupyter-Notebook-blue?logo=jupyter&style=flat-square)](datacamp-notes/intro_to_data_security.ipynb) | Interactive notebook covering CIA, symmetric/asymmetric cryptosystems, and access control. | ✅ Done |
| `datacamp-notes/network_security.md` | [![Markdown](https://img.shields.io/badge/Doc-Markdown-lightgrey?logo=markdown&style=flat-square)](datacamp-notes/network_security.md) | TCP/IP layers, ports, firewall rules, and network log structure. | ⏳ Upcoming |

---

## 🧮 Theoretical & Mathematical Foundations

Securing systems and modeling network threats relies heavily on number theory, asymmetric cryptography, and statistical classification evaluation.

### 1. Diffie-Hellman Key Exchange (Asymmetric Agreement)
Allows two parties to establish a shared secret over an insecure channel using modular arithmetic.
1. Alice and Bob agree on a large prime $p$ and base generator $g$.
2. Alice selects secret $a$ and sends:
   $$A = g^a \pmod p$$
3. Bob selects secret $b$ and sends:
   $$B = g^b \pmod p$$
4. The shared secret $K$ is computed by both parties:
   $$K = B^a \pmod p = A^b \pmod p = g^{ab} \pmod p$$

---

### 2. RSA Encryption Scheme (Asymmetric Cryptosystem)
Relies on the mathematical difficulty of factoring the product of two large prime numbers.
*   **Key Generation:** Select primes $p, q$, compute modulus $n = p \cdot q$, and Euler totient $\phi(n) = (p-1)(q-1)$. Select public exponent $e$ coprime to $\phi(n)$ and private exponent $d$ such that:
    $$e \cdot d \equiv 1 \pmod{\phi(n)}$$
*   **Encryption:** Given plaintext message $m$:
    $$c \equiv m^e \pmod n$$
*   **Decryption:** Recover message $m$ using private key $d$:
    $$m \equiv c^d \pmod n$$

---

### 3. Classification Performance Metrics for Intrusion Detection
When models analyze network packets for attacks, classification accuracy alone is misleading due to severe class imbalance. We evaluate using:
*   **True Positive Rate (TPR) / Sensitivity / Recall:**
    $$TPR = \frac{TP}{TP + FN}$$
    Measures the proportion of actual intrusions correctly identified.
*   **False Positive Rate (FPR) / Fall-out:**
    $$FPR = \frac{FP}{FP + TN}$$
    Measures the proportion of normal traffic flagged as malicious. Minimizing this is critical to avoid alert fatigue.

---

## 🔗 Cyber-AI Crossover Pipeline

The diagram below details the ingestion, parsing, and classification pipeline used to leverage Machine Learning models to defend systems against intrusion vectors.

[![Cybersecurity Crossover System](../assets/cybersecurity_sec_ops.svg)](README.md)

---

## 🎯 Navigation

`[← AI Engineering](../ai-engineering/) | [Next: MLOps →](../mlops/)`
