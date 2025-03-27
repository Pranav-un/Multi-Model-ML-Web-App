import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import joblib
import os

class ModelTrainer:
    def __init__(self):
        self.models_dir = 'models/trained_models'
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)

    def train_salary_model(self):
        # Load and prepare data
        data = pd.read_csv('employee_salary_data.csv')
        X = data[['years_experience']]
        y = data['salary']
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Save model
        joblib.dump(model, os.path.join(self.models_dir, 'salary_model.joblib'))
        return model

    def train_profit_model(self):
        # Load and prepare data
        data = pd.read_csv('startup_profit_data.csv')
        X = data[['R&D_spent', 'marketing_spent', 'admin_spent']]
        y = data['profit']
        
        # Train model
        model = LinearRegression()
        model.fit(X, y)
        
        # Save model
        joblib.dump(model, os.path.join(self.models_dir, 'profit_model.joblib'))
        return model

    def train_loan_model(self):
        # Load and prepare data
        data = pd.read_csv('loan_approval_data.csv')
        X = data[['income', 'credit_score', 'loan_amount']]
        y = data['loan_approved']
        
        # Train model
        model = LogisticRegression()
        model.fit(X, y)
        
        # Save model
        joblib.dump(model, os.path.join(self.models_dir, 'loan_model.joblib'))
        return model

    def train_house_model(self):
        # Load and prepare data
        data = pd.read_csv('house_price_data.csv')
        X = data[['size_sqft', 'num_bedrooms', 'num_bathrooms', 'location_score']]
        y = data['house_price']
        
        # Train model
        model = KNeighborsRegressor(n_neighbors=5)
        model.fit(X, y)
        
        # Save model
        joblib.dump(model, os.path.join(self.models_dir, 'house_model.joblib'))
        return model

    def train_fuel_model(self):
        # Load and prepare data
        data = pd.read_csv('car_fuel_efficiency_data.csv')
        
        # Create polynomial features transformer
        poly = PolynomialFeatures(degree=3, include_bias=True)
        
        # Create and fit the model
        model = LinearRegression()
        
        # Create pipeline
        pipeline = make_pipeline(poly, model)
        
        # Prepare data - only use engine_size
        X = data[['engine_size']]
        y = data['fuel_efficiency']
        
        # Fit the pipeline
        pipeline.fit(X, y)
        
        # Save the pipeline
        joblib.dump(pipeline, os.path.join(self.models_dir, 'fuel_model.joblib'))
        return pipeline

    def train_all_models(self):
        """Train all models and save them"""
        print("Training salary prediction model...")
        self.train_salary_model()
        
        print("Training profit prediction model...")
        self.train_profit_model()
        
        print("Training loan approval model...")
        self.train_loan_model()
        
        print("Training house price prediction model...")
        self.train_house_model()
        
        print("Training fuel efficiency model...")
        self.train_fuel_model()
        
        print("All models trained and saved successfully!")

if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.train_all_models() 