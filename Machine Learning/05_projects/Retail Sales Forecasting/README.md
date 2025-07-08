# Retail Sales Forecasting

Forecast daily retail sales using machine learning on a real-world ecommerce dataset.

## Project Overview

This project applies a machine learning model (XGBoost) to forecast daily sales using transaction data from an online retail store. We process the raw data, convert it into a daily time series, engineer calendar features, and build a forecasting model that predicts future sales.

---

## Dataset

- **Source:** [Ecommerce Dataset (Kaggle)](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
- **File Required:** `data.csv`
- **Features Used:**
  - `InvoiceDate`: Transaction timestamp
  - `Quantity`: Number of items
  - `UnitPrice`: Price per unit
  - `Sales`: Derived column = Quantity × UnitPrice

---

## Project Structure

```text

retail_sales_forecasting/
├── retail_sales_forecasting.ipynb # Complete Colab-ready notebook
├── README.md # Project overview and usage instructions


```

---

## How to Run

1. **Download** `data.csv` from [here](https://www.kaggle.com/datasets/carrie1/ecommerce-data).
2. Open `retail_sales_forecasting.ipynb` in **Google Colab**.
3. Upload `data.csv` using the Colab file upload cell.
4. Run all cells to:
   - Clean and transform the data
   - Engineer features
   - Train an XGBoost regressor
   - Forecast future daily sales
   - Plot actual vs predicted results

---

## Machine Learning Model

- **Model Used:** XGBoost Regressor
- **Features:** Day, Month, Year, DayOfWeek
- **Target:** Total daily sales
- **Metric:** Root Mean Squared Error (RMSE)

---

## Example Forecast Plot

The notebook will generate this:

![forecast](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Matplotlib_logo.svg/1920px-Matplotlib_logo.svg.png)

> (Replace with a screenshot of your Colab graph)

---

## Results

- The model successfully captures sales patterns using calendar-based features.
- Good fit with RMSE showing acceptable prediction error.
- Ideal for further experimentation with lag features, holiday effects, or advanced models like Prophet or LSTM.

---

## Future Improvements

- Add lag features (`sales[t-1]`, `t-7`, etc.)
- Use product-level or country-level grouping
- Explore deep learning (LSTM) or Facebook Prophet
- Create a forecasting dashboard with Streamlit

---


Created by [Tanu Nanda Prabhu](https://github.com/Tanu-N-Prabhu) – feel free to reach out via GitHub or [tanunprabhu95@gmail.com](tanunprabhu95@gmail.com)
