import joblib
import numpy as np
import os

class ModelLoader:
    def __init__(self):
        self.models_dir = 'models/trained_models'
        self.models = {}
        self.load_all_models()

    def load_all_models(self):
        """Load all trained models from disk"""
        model_files = {
            'salary': 'salary_model.joblib',
            'profit': 'profit_model.joblib',
            'loan': 'loan_model.joblib',
            'house': 'house_model.joblib',
            'fuel': 'fuel_model.joblib'
        }

        for model_name, file_name in model_files.items():
            file_path = os.path.join(self.models_dir, file_name)
            if os.path.exists(file_path):
                self.models[model_name] = joblib.load(file_path)
            else:
                print(f"Warning: Model file {file_name} not found!")

    def predict_salary(self, years_experience):
        """Predict salary based on years of experience"""
        if 'salary' not in self.models:
            raise ValueError("Salary prediction model not loaded")
        
        X = np.array([[years_experience]])
        prediction = self.models['salary'].predict(X)[0]
        return round(prediction, 2)

    def predict_profit(self, rd_spent, marketing_spent, admin_spent):
        """Predict startup profit based on spending"""
        if 'profit' not in self.models:
            raise ValueError("Profit prediction model not loaded")
        
        X = np.array([[rd_spent, marketing_spent, admin_spent]])
        prediction = self.models['profit'].predict(X)[0]
        return round(prediction, 2)

    def predict_loan_approval(self, income, credit_score, loan_amount):
        """Predict loan approval probability"""
        if 'loan' not in self.models:
            raise ValueError("Loan approval model not loaded")
        
        X = np.array([[income, credit_score, loan_amount]])
        probability = self.models['loan'].predict_proba(X)[0][1]
        return round(probability, 2)

    def predict_house_price(self, size_sqft, num_bedrooms, num_bathrooms, location_score):
        """Predict house price based on features"""
        if 'house' not in self.models:
            raise ValueError("House price prediction model not loaded")
        
        X = np.array([[size_sqft, num_bedrooms, num_bathrooms, location_score]])
        prediction = self.models['house'].predict(X)[0]
        return round(prediction, 2)

    def predict_fuel_efficiency(self, engine_size):
        """Predict car fuel efficiency based on engine size"""
        if 'fuel' not in self.models:
            raise ValueError("Fuel efficiency prediction model not loaded")
        
        # Create input array with proper shape
        X = np.array([[float(engine_size)]])
        
        # Use the pipeline to predict
        prediction = self.models['fuel'].predict(X)[0]
        return round(prediction, 2)

    def get_prediction(self, model_name, features):
        """Get prediction from specified model with given features"""
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not found")

        prediction_methods = {
            'salary': self.predict_salary,
            'profit': self.predict_profit,
            'loan': self.predict_loan_approval,
            'house': self.predict_house_price,
            'fuel': self.predict_fuel_efficiency
        }

        return prediction_methods[model_name](**features) 