from app.models.model_trainer import ModelTrainer

if __name__ == "__main__":
    print("Starting model training...")
    trainer = ModelTrainer()
    trainer.train_all_models()
    print("Model training completed!") 