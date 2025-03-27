// Model input field configurations
const modelConfigs = {
    salary: [
        { 
            name: 'years_experience', 
            label: 'Years of Experience (0-30 years)', 
            type: 'number', 
            min: 0,
            max: 30,
            placeholder: 'e.g., 5 years'
        }
    ],
    profit: [
        { 
            name: 'rd_spent', 
            label: 'R&D Spending ($0-$1,000,000)', 
            type: 'number', 
            min: 0,
            max: 1000000,
            placeholder: 'e.g., 150000'
        },
        { 
            name: 'marketing_spent', 
            label: 'Marketing Spending ($0-$1,000,000)', 
            type: 'number', 
            min: 0,
            max: 1000000,
            placeholder: 'e.g., 200000'
        },
        { 
            name: 'admin_spent', 
            label: 'Administration Spending ($0-$1,000,000)', 
            type: 'number', 
            min: 0,
            max: 1000000,
            placeholder: 'e.g., 100000'
        }
    ],
    loan: [
        { 
            name: 'income', 
            label: 'Monthly Income ($0-$50,000)', 
            type: 'number', 
            min: 0,
            max: 50000,
            placeholder: 'e.g., 5000'
        },
        { 
            name: 'credit_score', 
            label: 'Credit Score (300-850)', 
            type: 'number', 
            min: 300,
            max: 850,
            placeholder: 'e.g., 750'
        },
        { 
            name: 'loan_amount', 
            label: 'Loan Amount ($0-$500,000)', 
            type: 'number', 
            min: 0,
            max: 500000,
            placeholder: 'e.g., 250000'
        }
    ],
    house: [
        { 
            name: 'size_sqft', 
            label: 'House Size (500-5000 sq ft)', 
            type: 'number', 
            min: 500,
            max: 5000,
            placeholder: 'e.g., 2000'
        },
        { 
            name: 'num_bedrooms', 
            label: 'Number of Bedrooms (1-6)', 
            type: 'number', 
            min: 1,
            max: 6,
            placeholder: 'e.g., 3'
        },
        { 
            name: 'num_bathrooms', 
            label: 'Number of Bathrooms (1-4)', 
            type: 'number', 
            min: 1,
            max: 4,
            placeholder: 'e.g., 2'
        },
        { 
            name: 'location_score', 
            label: 'Location Score (1-10)', 
            type: 'number', 
            min: 1,
            max: 10,
            placeholder: 'e.g., 8'
        }
    ],
    fuel: [
        { 
            name: 'engine_size', 
            label: 'Engine Size (1-6 liters)', 
            type: 'number', 
            min: 1,
            max: 6,
            step: 0.1,
            placeholder: 'e.g., 2.5'
        }
    ]
};

// Model descriptions
const modelDescriptions = {
    salary: "This model predicts an employee's salary based on their years of experience using Simple Linear Regression. It establishes a linear relationship between experience and salary.",
    profit: "This model predicts a startup's profit based on three key spending areas: R&D, Marketing, and Administration. It uses Multiple Linear Regression to analyze the impact of each spending category.",
    loan: "This model predicts the probability of loan approval based on the applicant's income, credit score, and requested loan amount. It uses Logistic Regression for binary classification.",
    house: "This model predicts house prices based on size, number of bedrooms/bathrooms, and location score. It uses K-Nearest Neighbors to find similar properties and estimate prices.",
    fuel: "This model predicts a car's fuel efficiency based on engine size using Polynomial Regression. It captures the non-linear relationship between engine size and fuel efficiency."
};

// Get DOM elements
const modelSelect = document.getElementById('modelSelect');
const inputFields = document.getElementById('inputFields');
const predictionForm = document.getElementById('predictionForm');
const resultDiv = document.getElementById('result');
const predictionValue = document.getElementById('predictionValue');
const modelDescription = document.getElementById('modelDescription');
const predictButton = document.getElementById('predictButton');

// Function to create input fields based on selected model
function createInputFields(modelName) {
    inputFields.innerHTML = '';
    
    if (!modelName) {
        modelDescription.style.display = 'none';
        predictButton.disabled = true;
        return;
    }
    
    const config = modelConfigs[modelName];
    if (!config) return;
    
    // Show model description
    modelDescription.style.display = 'block';
    modelDescription.innerHTML = `<p class="mb-0">${modelDescriptions[modelName]}</p>`;
    
    config.forEach(field => {
        const div = document.createElement('div');
        div.className = 'mb-3';
        
        const label = document.createElement('label');
        label.className = 'form-label';
        label.htmlFor = field.name;
        label.textContent = field.label;
        
        const input = document.createElement('input');
        input.type = field.type;
        input.className = 'form-control';
        input.id = field.name;
        input.name = field.name;
        input.required = true;
        input.placeholder = field.placeholder;
        
        if (field.min !== undefined) input.min = field.min;
        if (field.max !== undefined) input.max = field.max;
        if (field.step !== undefined) input.step = field.step;
        
        // Add helper text below input
        const helperText = document.createElement('div');
        helperText.className = 'form-text text-muted';
        helperText.textContent = `Range: ${field.min} - ${field.max}`;
        
        div.appendChild(label);
        div.appendChild(input);
        div.appendChild(helperText);
        inputFields.appendChild(div);
    });

    predictButton.disabled = false;
}

// Handle model selection change
modelSelect.addEventListener('change', (e) => {
    createInputFields(e.target.value);
    resultDiv.style.display = 'none';
});

// Handle form submission
predictionForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const modelName = modelSelect.value;
    if (!modelName) {
        alert('Please select a model');
        return;
    }
    
    // Validate all required fields
    const inputs = inputFields.querySelectorAll('input');
    let isValid = true;
    inputs.forEach(input => {
        if (!input.value) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });

    if (!isValid) {
        alert('Please fill in all required fields');
        return;
    }
    
    const formData = new FormData(predictionForm);
    const features = {};
    
    for (const [key, value] of formData.entries()) {
        if (key !== 'model') {
            features[key] = parseFloat(value);
        }
    }
    
    try {
        predictButton.disabled = true;
        predictButton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
        
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: modelName,
                features: features
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            let resultText = '';
            switch (modelName) {
                case 'salary':
                    resultText = `Predicted Salary: $${data.prediction.toLocaleString()}`;
                    break;
                case 'profit':
                    resultText = `Predicted Profit: $${data.prediction.toLocaleString()}`;
                    break;
                case 'loan':
                    // Convert probability to Yes/No based on 0.5 threshold
                    resultText = `Loan Approval: ${data.prediction >= 0.5 ? 'Yes' : 'No'}`;
                    break;
                case 'house':
                    resultText = `Predicted House Price: $${data.prediction.toLocaleString()}`;
                    break;
                case 'fuel':
                    resultText = `Predicted Fuel Efficiency: ${data.prediction} km/l`;
                    break;
            }
            
            predictionValue.textContent = resultText;
            resultDiv.style.display = 'block';
        } else {
            throw new Error(data.error || 'Prediction failed');
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        predictButton.disabled = false;
        predictButton.innerHTML = '<i class="fas fa-calculator me-2"></i>Make Prediction';
    }
}); 