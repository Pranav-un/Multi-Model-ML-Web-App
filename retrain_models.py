import os
import shutil
from app.models.model_trainer import ModelTrainer

def main():
    # Delete existing models directory if it exists
    models_dir = 'app/models/saved_models'
    if os.path.exists(models_dir):
        shutil.rmtree(models_dir)
    
    # Create new models directory
    os.makedirs(models_dir, exist_ok=True)
    
    # Initialize model trainer
    trainer = ModelTrainer()
    
    # Train all models
    print("Training salary prediction model...")
    trainer.train_salary_model()
    
    print("Training profit prediction model...")
    trainer.train_profit_model()
    
    print("Training loan approval model...")
    trainer.train_loan_model()
    
    print("Training house price model...")
    trainer.train_house_model()
    
    print("Training fuel efficiency model...")
    trainer.train_fuel_model()
    
    print("All models trained successfully!")

if __name__ == "__main__":
    main() 