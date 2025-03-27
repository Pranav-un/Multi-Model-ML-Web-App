import os
import shutil
from app.models.model_trainer import ModelTrainer

def retrain_models():
    # Delete existing models directory
    models_dir = 'models/trained_models'
    if os.path.exists(models_dir):
        shutil.rmtree(models_dir)
        print("Deleted existing models directory")
    
    # Create new models directory and train models
    trainer = ModelTrainer()
    trainer.train_all_models()
    print("Models retrained successfully!")

if __name__ == "__main__":
    retrain_models() 