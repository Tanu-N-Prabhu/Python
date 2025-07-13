# Autoencoder from Scratch (No Deep Learning Libraries)

This notebook walks through a step-by-step implementation of a **basic autoencoder** using only **NumPy**. Autoencoders are a type of neural network used to compress and reconstruct data, making them a powerful tool for **unsupervised learning**, **dimensionality reduction**, and **anomaly detection**.

---

## What You'll Learn

- The structure and purpose of an autoencoder
- How to encode and decode input data using matrix operations
- How to train a simple neural network using forward and backward propagation
- How to visualize the reconstruction of handwritten digits

---

## What is an Autoencoder?

An **autoencoder** is a type of neural network trained to **reproduce its input** as output. It learns a compressed representation of the data through:

- **Encoder**: Maps input to a lower-dimensional space (latent/bottleneck)
- **Decoder**: Reconstructs the input from the latent space

### Architecture

```
Input → Encoder → Bottleneck → Decoder → Output
```

The network is trained to minimize the **reconstruction error** between the original input and its output.

---

## Files Included

| File                           | Description                                      |
|:--------------------------------|:--------------------------------------------------|
| `autoencoder_from_scratch.ipynb` | Complete NumPy implementation of an autoencoder |
| `README.md`                    | This file explains the notebook and usage      |

---

## Dataset Used

- `sklearn.datasets.load_digits()`: 8×8 grayscale handwritten digits
- Each image is flattened into a 64-dimensional vector
- Pixel values scaled between 0 and 1

---

## How to Use

1. Clone or download this repository
2. Open `autoencoder_from_scratch.ipynb` in:
   - Jupyter Notebook or
   - Google Colab
3. Run all cells to:
   - Load and preprocess the dataset
   - Train the autoencoder using forward and backpropagation
   - Visualize original vs reconstructed digits

---

## Architecture Details

| Layer        | Size    | Activation |
|:--------------|:---------|:------------|
| Input        | 64      | —          |
| Encoder      | 32      | Sigmoid    |
| Bottleneck   | 16      | Sigmoid    |
| Decoder      | 32      | Sigmoid    |
| Output       | 64      | Sigmoid    |

- Loss function: **Mean Squared Error (MSE)**
- Optimizer: **Manual gradient descent**
- Epochs: 100 (can be increased for better performance)

---

## Why Are Outputs Blurry?

- Limited bottleneck size (only 16 features)
- Shallow architecture (1 encoder + 1 decoder layer)
- Use of sigmoid activation smoothens outputs
- Trained on few epochs

To improve:
- Use more hidden layers or ReLU activation
- Train for more epochs
- Increase the bottleneck size

---

## Requirements

```bash
pip install numpy matplotlib scikit-learn
```

 ---

 ## License
This project is open-source under the MIT License. Use it freely for teaching or learning.

---

## Contribute
Suggestions and pull requests are welcome! You could:
  * Add denoising autoencoders
  * Add dropout regularization
  * Extend to convolutional autoencoders

> Happy learning! 
