from flask import Flask, request, jsonify
app = Flask(__name__)

class Patient:
    def __init__(self,patient_id,name,age,disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
    def to_dict(self):
        return{
            "patient_id":self.patient_id,
            "name":self.name,
            "age":self.age,
            "disease":self.disease
        }
class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
    def to_dict(self):
        return{
            "doctor_id":self.doctor_id,
            "name":self.name,
            "specialization":self.specialization

        }
class Finance:
    def __init__(self):
        self.patients_billed = {}
    def add_bill(self,patient_id,amount):
        if patient_id in self.patients_billed:
            self.patients_billed[patient_id]=amount
        else:
            self.patients_billed[patient_id]=amount
    def delete_bill(self,patient_id):
        if patient_id in self.patients_billed:
            del self.patients_billed[patient_id]
    def get_total_bill(self):
        return sum(self.patients_billed.values())

class Hospital:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.finance = {}
    def add_patient(self,patient):
        self.patients[patient.patient_id] = [patient]
    def delete_patient(self,patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            self.finance.delete_bill(patient_id)
    def add_doctor(self,doctor):
        self.doctors[doctor.doctor_id] = doctor
    def get_patients(self,patient_id):
        return self.patients.get(patient_id,None)
    def get_doctor(self,doctor_id):
        return self.doctors.get(doctor_id,None)
    def get_total_revenue(self):
        return self.finance.get_total_bill()

hospital = Hospital()

@app.route('/add_patient',methods=['POST'])
def add_patient():
    data = request.json
    patient = Patient(data['patient_id'], data['name'], data['age'], data['disease'])
    hospital.add_patient(patient)
    return jsonify({"message": "Patient added successfully!"})

@app.route('/delete_patient/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    hospital.delete_patient(patient_id)
    return jsonify({"message": "Patient deleted successfully!"})

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    data = request.json
    doctor = Doctor(data['doctor_id'], data['name'], data['specialization'])
    hospital.add_doctor(doctor)
    return jsonify({"message": "Doctor added successfully!"})

@app.route('/get_patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = hospital.get_patient(patient_id)
    if patient:
        return jsonify(patient.to_dict())
    else:
        return jsonify({"message": "Patient not found!"}), 404

@app.route('/get_doctor/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = hospital.get_doctor(doctor_id)
    if doctor:
        return jsonify(doctor.to_dict())
    else:
        return jsonify({"message": "Doctor not found!"}), 404

@app.route('/total_revenue', methods=['GET'])
def total_revenue():
    return jsonify({"total_revenue": hospital.get_total_revenue()})

if __name__ == '__main__':
    app.run(debug=True)
        
        
