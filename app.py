from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase Setup
cred = credentials.Certificate("firebase_key.json")  # ADD this file later
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    teacher_name = request.form['teacher_name']
    teacher_email = request.form['teacher_email']
    parent_name = request.form['parent_name']
    student_name = request.form['student_name']
    parent_phone = request.form['parent_phone']

    # Push to Firestore
    data = {
        'teacher_name': teacher_name,
        'teacher_email': teacher_email,
        'parent_name': parent_name,
        'student_name': student_name,
        'parent_phone': parent_phone
    }
    db.collection('parent_teacher_info').add(data)

    return "Data submitted successfully! 🎉"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
