from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = 'http://51.21.252.70:8000/predict'

OCCUPATIONS = [
    'Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
    'Marketing Manager', 'Insurance Agent', 'HR Manager', 'Pharmacist',
    'Teacher', 'Software Engineer', 'Consultant', 'Driver', 'Shop Owner',
    'Nurse', 'Accountant', 'Government Employee', 'Architect', 'Engineer',
    'Real Estate Agent', 'Civil Servant', 'Plumber', 'Retail Manager',
    'Chef', 'Electrician', 'Carpenter', 'Doctor', 'Lab Technician',
    'Data Analyst', 'Lawyer', 'Content Writer'
]

@app.route('/')
def index():
    return render_template('index.html', occupations=OCCUPATIONS)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = {
        'age': int(data['age']),
        'weight': float(data['weight']),
        'height': float(data['height']),
        'income_lpa': float(data['income_lpa']),
        'smoker': data['smoker'] == 'true' or data['smoker'] is True,
        'city': data['city'],
        'occupation': data['occupation']
    }
    try:
        response = requests.post(API_URL, json=input_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            category = result['response']['predicted_category']
            confidence = round(result['response']['confidence'] * 100, 2)
            return jsonify({'success': True, 'category': category, 'confidence': confidence})
        else:
            return jsonify({'success': False, 'error': f'API Error {response.status_code}: {response.text}'})
    except requests.exceptions.ConnectionError:
        return jsonify({'success': False, 'error': "Could not connect to the FastAPI server. Make sure it's running on port 8000."})
    except requests.exceptions.Timeout:
        return jsonify({'success': False, 'error': "Request timed out. The prediction server took too long to respond."})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
