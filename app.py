from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    if height is None or weight is None:
        return jsonify({'error': 'Missing height or weight'}), 400
    try:
        bmi_value = calculate_bmi(float(height), float(weight))
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'bmi': round(bmi_value, 2)}), 200

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.get_json()
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')
    if None in (height, weight, age, gender):
        return jsonify({'error': 'Missing height, weight, age, or gender'}), 400
    try:
        bmr_value = calculate_bmr(float(height), float(weight), int(age), gender)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({'bmr': round(bmr_value, 2)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
