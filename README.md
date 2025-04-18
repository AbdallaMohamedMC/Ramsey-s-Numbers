# Ramsey-s-Numbers
This project is by Eng.Abdalla Mohamad, Eng.Kamal Elsawah, Eng.Osama Taha, Eng.Ziad Mohhamad.
With under supervision of Prof. Walid Gomaa.
At Egypt-Japan University of Science and Technology (E-JUST).

# **README - Ramsey Numbers**



# 🎯 Ramsey Theory & Pseudorandom Graph Exploration

This project is a computational exploration of **Ramsey theory** through the lens of **pseudorandom graphs** and **spectral graph analysis**. We aim to combine recent theoretical advances with algorithmic experimentation to better understand and simulate Ramsey-related phenomena.

---

## 📌 Project Overview

Ramsey theory studies unavoidable patterns in large structures—like how any sufficiently large graph must contain monochromatic cliques in any edge coloring. Our focus is on:

- Simulating **pseudorandom graphs**.
- Verifying their **spectral properties**.
- Testing Ramsey-related behavior like **monochromatic clique existence** in **colored graphs**.

---

## 🧪 Phases of the Project

### ✅ Phase 1: Pseudorandom Graph Generation & Spectral Verification
- Generated *d*-regular graphs using NetworkX.
- Calculated the **second-largest eigenvalue (λ₂)** of the adjacency matrix.
- Verified pseudorandomness via spectral norm conditions:  
  `‖A - (d/n)J‖ ≤ λ`
- Interpreted spectral gaps as indicators of randomness.

> 📂 Script: `phase1_pseudorandom_graph_spectral.py`

---

### ✅ Phase 2: Edge Coloring & Ramsey Problem Setup
- Randomly colored the edges of the graph (2-coloring).
- Visualized edge coloring using red and blue.
- Goal: Identify or simulate potential **monochromatic cliques**, which ties directly to bounds on Ramsey numbers.

> 📂 Script: `phase2_colored_graph_ramsey.py`

---

## 🚀 Final Goal

We aim to **experimentally validate small Ramsey instances** and simulate their behavior using:
- Pseudorandom graph models.
- Spectral conditions.
- SAT solver integration (future phase).
- Comparisons against known Ramsey number bounds.

The long-term vision includes:
- Extending to **3-color problems**.
- Automating search for large cliques.
- Generating statistics on random graphs' Ramsey behavior.

---

## 🧰 Tools & Libraries

- [NetworkX](https://networkx.org/) – Graph generation & visualization
- [NumPy](https://numpy.org/) – Matrix and eigenvalue operations
- [Matplotlib](https://matplotlib.org/) – Plotting graphs

---

## 📚 References

- Campos et al. (2023). *A New Limit for Patterns in Graphs* – Quanta Magazine  
- Verstraete, J. (2024). *Recent Progress in Ramsey Theory* – arXiv  
- Alon & Spencer (2016). *The Probabilistic Method*  
- Krivelevich & Sudakov (2006). *Pseudo-random Graphs*  
- Spielman, D. (2007). *Spectral Graph Theory* – Yale University  

---

## 📌 Status

🚧 *Work in progress – currently preparing for Phase 3 (SAT-based clique detection & deeper Ramsey integration).*

---


**Authors:**
- Kamal Elsawah
- Zeyad El-Said
- Abdalla Mohamad
- Osama Taha

**Supervisor:**
- Prof. Walid Gomaa
- Eng. Omnia Azzam

