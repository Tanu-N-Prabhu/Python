# Handwritten Digit Recognition (MNIST)

This project demonstrates how to build a machine learning model to recognize handwritten digits (0–9) using the MNIST dataset. It uses a Random Forest classifier trained on the pixel values of 28×28 grayscale images.

---

## Dataset Overview

**Name**: MNIST Handwritten Digit Dataset  
**Source**: [Kaggle - MNIST in CSV](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv)  
**License**: Open Data (free to use for educational purposes)  
**Format**: CSV (no image files needed)

### Files Included
- `mnist_train.csv` → 60,000 training samples
- `mnist_test.csv` → 10,000 test samples

Each row in the dataset contains:
- `label`: The true digit (0–9)
- `pixel0` to `pixel783`: Grayscale pixel values of the 28×28 image (flattened)

---

## Project Objectives

- Load and explore the MNIST dataset
- Train a Random Forest model on pixel data
- Visualize sample digits
- Evaluate performance using classification metrics
- Make predictions on uploaded PNG images

---

## Tech Stack

- Python
- scikit-learn
- pandas & numpy
- matplotlib & seaborn
- Google Colab
- PIL / OpenCV (for custom PNG image prediction)

---

## How to Use

### Option 1: Run on Google Colab

1. Open the Jupyter notebook (`mnist_digit_recognition.ipynb`)
2. Upload `mnist_train.csv` and `mnist_test.csv` when prompted
3. Run the notebook cells sequentially
4. To test your own digit image:
   - Call `predict_custom_png_image()`
   - Upload a PNG image (ideally 28×28 pixels, grayscale, white background, black digit)
   - View the prediction and probability scores

---

### Sample PNG Upload Funtion

```python
def predict_custom_png_image():
    from google.colab import files
    uploaded = files.upload()

    for filename in uploaded.keys():
        # Open and convert image to grayscale
        img = Image.open(io.BytesIO(uploaded[filename])).convert('L')  # 'L' for grayscale

        # Resize to 28x28 if not already
        img = img.resize((28, 28))

        # Convert to NumPy array and invert colors (MNIST: white background, black digit)
        img_array = np.array(img)
        img_array = 255 - img_array  # Invert colors

        # Normalize pixel values
        img_array = img_array / 255.0

        # Flatten to 1D vector (784,)
        flat_img = img_array.flatten().reshape(1, -1)

        # Predict
        prediction = model.predict(flat_img)[0]
        prediction_proba = model.predict_proba(flat_img)[0]

        # Show the image
        plt.imshow(img_array, cmap='gray')
        plt.title(f"Predicted Digit: {prediction}")
        plt.axis('off')
        plt.show()

        # Show top 3 probabilities
        top_3 = np.argsort(prediction_proba)[::-1][:3]
        print("🔮 Prediction Probabilities:")
        for idx in top_3:
            print(f"{idx}: {prediction_proba[idx]*100:.2f}%")
```

## 🖼️ PNG Image Prediction (Bonus Feature)

You can upload your own digit images and get model predictions.  
Supported format: `.png` (black digit on white background).

### Example:
```python
predict_custom_png_image()
```

The model will:

* Resize and normalize the image
* Predict the digit
* Show the top 3 predicted classes with probability

---

## Sample Output

```text
Prediction Probabilities:
3: 85.76%
5: 10.21%
8: 2.17%

Predicted Digit: 3
```
---

##  Model Used
* `RandomForestClassifier(n_estimators=100)`
* Accuracy on test set: ~96%
* Input Features: 784 (flattened pixels)
* Target: 0–9 digits

---

## Learning Outcomes
* Handling flattened image data
* Training classical ML models for image classification
* Evaluating performance using confusion matrix and classification report
* Accepting user-uploaded input for real-time prediction

---

##  File Structure

```text
mnist_digit_recognition/
├── mnist_digit_recognition.ipynb   # Jupyter Notebook (Colab-ready)
├── mnist_train.csv                 # Training data
├── mnist_test.csv                  # Test data
└── README.md                       # Project overview
```

---

## Acknowledgments
Dataset inspired by UCI & Scikit-learn.
> This project is created for educational and demonstration purposes.

---

## Contact
Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)

