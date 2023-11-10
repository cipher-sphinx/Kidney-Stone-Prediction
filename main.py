import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('stacking_model.pkl', 'rb'))
output = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    features = [
        request.form.get('Urine_Gravity'),
        request.form.get('Urine_pH'),
        request.form.get('Osmolality'),
        request.form.get('Conductivity'),
        request.form.get('Urea'),
        request.form.get('Calcium')
    ]

    prediction = model.predict([features])[0]
    output = 'Risk of Kidney Stones' if prediction == 1 else 'No Risk of Kidney Stones'

    return render_template('index.html', prediction_text=f'Predicted output: {output}')


if __name__ == '__main__':
    app.run(debug=True)