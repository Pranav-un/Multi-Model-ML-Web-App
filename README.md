# Multi-Model Machine Learning Web Application

This web application provides a unified interface for making predictions using five different machine learning models:

1. Simple Linear Regression - Employee Salary Prediction
2. Multiple Linear Regression - Startup Profit Prediction
3. Logistic Regression - Loan Approval Prediction
4. K-Nearest Neighbors - House Price Prediction
5. Polynomial Regression - Car Fuel Efficiency Prediction

## Project Structure
```
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── model_trainer.py
│   │   └── model_loader.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       └── index.html
├── data/
│   ├── employee_salary_data.csv
│   ├── startup_profit_data.csv
│   ├── loan_approval_data.csv
│   ├── house_price_data.csv
│   └── car_fuel_efficiency_data.csv
├── models/
│   └── trained_models/
├── requirements.txt
└── run.py
```

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python run.py
```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Select a model from the dropdown menu
3. Enter the required input features
4. Click "Predict" to get the prediction result

## API Endpoints

- POST `/predict`: Main endpoint for making predictions
  - Request body: JSON with model name and input features
  - Response: JSON with prediction result

## Models

### 1. Employee Salary Prediction (SLR)
- Input: years_experience
- Output: predicted salary

### 2. Startup Profit Prediction (MLR)
- Input: R&D_spent, marketing_spent, admin_spent
- Output: predicted profit

### 3. Loan Approval Prediction (Logistic)
- Input: income, credit_score, loan_amount
- Output: loan approval probability

### 4. House Price Prediction (KNN)
- Input: size_sqft, num_bedrooms, num_bathrooms, location_score
- Output: predicted house price

### 5. Car Fuel Efficiency Prediction (Polynomial)
- Input: speed, engine_size
- Output: predicted fuel efficiency 