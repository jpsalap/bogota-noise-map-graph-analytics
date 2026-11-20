# bogota-noise-map-graph-analytics
Graph-theoretic modeling and centrality analysis of urban noise maps across 18 districts in Bogotá using Python (OpenCV, NumPy, SciPy, NetworkX).

# Urban Acoustic Topology & Graph Analytics (`Bogotá Noise Maps`)

Graph-theoretic framework and computer vision pipeline for modeling spatial noise distribution across **18 urban districts (localidades) in Bogotá, Colombia**, developed as a B.S. Sound Engineering thesis at Universidad de San Buenaventura (advised by Dr. Jorge Eduardo Useche, Ph.D. in Physics).

## Problem & Scalability Architecture
Strategic urban noise maps encode continuous equivalent sound pressure levels ($L_{eq}$) across standardized 5 dB(A) color bands (Colombian Resolution 0627 of 2006), but visual maps alone do not quantify how sound zones connect or propagate spatially.

* **Bottleneck Solved:** Modeling every map pixel as a node in a bipartite pixel-to-color graph generated **>1,000,000 nodes**, exceeding graph-analysis memory limits (UCINET's 32,767-node ceiling).
* **Single-Mode Weighted Graph Reformulation:** Re-architected the representation into a compact **11-node undirected weighted graph** (reducing node count by **99.999%**), where each node represents a 5 dB(A) acoustic band (from `≤ 35 dB(A)` to `> 80 dB(A)`) and edge weights encode exact spatial boundary-transition frequencies.

## Pipeline Architecture
1. **Vectorized RGB Color Quantization (`color_approximation.py`):** Uses `OpenCV` and `NumPy` 3D Euclidean distance classification in RGB space to snap anti-aliased raster pixels strictly to the 11 canonical regulatory color classes and filter exterior backgrounds.
2. **8-Directional Spatial Adjacency Scanner (`pixel_adjacency.py`):** Scans horizontal, vertical, and diagonal pixel neighborhoods (calibrated to `3.788 m` orthogonal and `5.357 m` diagonal resolution) to build symmetric adjacency matrices and $\log_{10}$-scaled edge weights.
3. **Weighted Closeness Centrality (`weighted_closeness_dijkstra.py`):** Computes shortest-path distances over inverse-weight sparse matrices using `scipy.sparse.csgraph.dijkstra`.
4. **Weighted Betweenness Centrality (`weighted_betweenness.py`):** Quantifies structural bridge nodes across urban soundscapes using `NetworkX` (`betweenness_centrality` with inverse-weight edge distances).

## Key Analytical Findings
* **Commercial & Industrial Bands as Network Bridges:** Across the 18 districts, intermediate noise bands (`50.1–55`, `55.1–60`, and `60.1–65 dB(A)`) consistently exhibited the highest weighted closeness and betweenness centrality, acting as mandatory spatial transitions between quiet residential/natural zones and high-traffic corridors.
* **Automated Outlier Detection:** Centrality distributions isolated structural anomalies across districts—such as **Barrios Unidos** lacking `(35.1–40] dB(A)` natural-noise zones and **Suba** exhibiting elevated connectivity in `≤ 35 dB(A)` peripheral zones.

## Tech Stack
* **Language:** Python
* **Computer Vision & Arrays:** `OpenCV` (`cv2`), `NumPy`, `Matplotlib`
* **Graph Algorithms:** `SciPy` (`scipy.sparse.csgraph.dijkstra`), `NetworkX`

## Citation
Joya Martínez, S., & Salazar Pinto, J. P. (2024). *Representación de información de mapas de ruido por medio de grafos* [Undergraduate Thesis]. Universidad de San Buenaventura, Bogotá.
