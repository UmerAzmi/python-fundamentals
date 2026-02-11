# 🔢 NumPy (Numerical Computing)

This folder contains my structured learning and practical implementation of **NumPy**, starting from fundamentals and extending to real project usage (AI QR Code project).

The notebooks progress from core concepts → indexing → mathematical operations → real-world AI application.

---

## 📂 Files Included

### 1.ipynb – NumPy Basics & Memory Understanding

Covers:

- What NumPy is and why it is faster than Python lists
- Continuous memory concept
- Bits, Bytes, and data types
  - int8, int16, int32
  - float32
- Creating 1D, 2D, and 3D arrays
- Understanding:
  - `ndim` (number of dimensions)
  - `shape`
  - `dtype`
  - `itemsize`
  - `nbytes`
- Memory usage comparison between different data types

This notebook builds the foundation for understanding how NumPy works internally.

---

### 2.ipynb – Indexing, Slicing & Modifying Arrays

Covers:

- Accessing elements in 2D arrays using `[row, column]`
- Accessing full rows and full columns
- Fancy slicing `[start:end:step]`
- Modifying elements inside arrays
- Working with 3D arrays
- Understanding multidimensional indexing
- Shape rules when replacing values
- Using `:` across different dimensions

This notebook focuses heavily on **array access and manipulation logic**.

---

### 3.ipynb – Array Initialization, Math & Statistics

Covers:

Array Initialization:

- `np.zeros()`
- `np.ones()`
- `np.full()`
- `np.full_like()`
- `np.random.rand()`
- `np.random.randint()`
- `np.identity()`
- `np.repeat()`

Array Manipulation:

- Embedding arrays using slicing
- Building structured matrix patterns

Copying Arrays:

- Reference vs `.copy()`
- Memory behavior explanation

Mathematical Operations:

- Element-wise arithmetic (`+`, `-`, `*`, `/`)
- Power operations (`**`)
- Trigonometric functions (`np.cos()`)

Statistics:

- `np.min()`
- `np.max()` with axis
- `np.sum()` with axis
- Understanding `axis=0` vs `axis=1`

File Handling:

- `np.genfromtxt()` for reading data
- `.astype()` for type conversion

This notebook connects NumPy fundamentals to practical computation and data handling.

---

### 4.ipynb – NumPy in AI QR Code Project

Demonstrates real-world usage of NumPy in an AI project.

Covers:

Image Handling:

- Converting PIL images to NumPy arrays
- Understanding image shape `(height, width, channels)`
- RGB pixel structure

Normalization:

- Scaling pixel values from 0–255 → 0–1
- Why normalization is important for deep learning

Reshaping:

- Adding batch dimension
- Reshaping for model input

Deep Learning Integration:

- Converting NumPy arrays to PyTorch tensors
- Preparing data for AI models

This notebook shows how NumPy integrates into computer vision and deep learning workflows.

---

## ⚠️ Notebook Preview Issue

GitHub may sometimes show **"Unable to render code block"** for `.ipynb` files.

If the notebook does not preview correctly:

- Download the file
- Open it using **Jupyter Notebook** or **JupyterLab**
- Or run it inside **VS Code/PyCharm (with Python extension installed)**

This ensures the notebook runs properly with all outputs visible.

---

## 🎯 Purpose of This Section

- Build strong foundational understanding of NumPy
- Understand memory behavior and performance
- Master indexing and slicing logic
- Perform mathematical and statistical operations efficiently
- Apply NumPy in real-world AI workflows

---

> 🚧 This section may be expanded in the future with advanced topics such as groupby operations, merging datasets, handling missing data in depth, and exploratory data analysis (EDA).
