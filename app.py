import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Carregar o modelo
with open('ML/models/model_svc.pkl', 'rb') as file:
    model = pickle.load(file)

# Dicionário de rótulos
label_maps = {
    'Gender': {'0': 'Masculino', '1': 'Feminino'},
    'Ethnicity': {'0': 'Caucasiano', '1': 'Afro-americano', '2': 'Asiático', '3': 'Outro'},
    'EducationLevel': {'0': 'Nenhum', '1': 'Ensino Médio', '2': 'Graduação', '3': 'Pós-Graduação'},
    'Smoking': {'0': 'Não', '1': 'Sim'},
    'FamilyHistoryAlzheimers': {'0': 'Não', '1': 'Sim'},
    'CardiovascularDisease': {'0': 'Não', '1': 'Sim'},
    'Diabetes': {'0': 'Não', '1': 'Sim'},
    'Depression': {'0': 'Não', '1': 'Sim'},
    'HeadInjury': {'0': 'Não', '1': 'Sim'},
    'Hypertension': {'0': 'Não', '1': 'Sim'},
    'MemoryComplaints': {'0': 'Não', '1': 'Sim'},
    'BehavioralProblems': {'0': 'Não', '1': 'Sim'},
    'Confusion': {'0': 'Não', '1': 'Sim'},
    'Disorientation': {'0': 'Não', '1': 'Sim'},
    'PersonalityChanges': {'0': 'Não', '1': 'Sim'},
    'DifficultyCompletingTasks': {'0': 'Não', '1': 'Sim'},
    'Forgetfulness': {'0': 'Não', '1': 'Sim'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        patient_data = request.form.to_dict()

        input_data = [float(value) for value in patient_data.values()]
        input_array = np.array([input_data])

        rescaledX_entrada = model[0].transform(input_array)
        prediction = model[1].predict(rescaledX_entrada)

        result_message = 'Propensão a ter Alzheimer' if prediction == 1 else 'Sem propensão a ter Alzheimer'

        translated_data = {}
        for key, value in patient_data.items():
            if key in label_maps:
                translated_data[key] = label_maps[key].get(value, value)
            else:
                translated_data[key] = value

        return render_template('result.html', result_message=result_message, patient_data=translated_data)

    except Exception as e:
        return f'Erro: {e}'

if __name__ == '__main__':
    app.run(debug=True)
