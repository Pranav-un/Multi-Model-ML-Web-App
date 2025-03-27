from flask import Flask, request, jsonify, render_template
from app.models.model_loader import ModelLoader

app = Flask(__name__)
model_loader = ModelLoader()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        model_name = data.get('model')
        features = data.get('features', {})

        if not model_name or not features:
            return jsonify({'error': 'Model name and features are required'}), 400

        prediction = model_loader.get_prediction(model_name, features)
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 