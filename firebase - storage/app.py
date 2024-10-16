from flask import Flask, request, render_template
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)
# Initialize Firebase Admin SDK
cred = credentials.Certificate('credential.json')  # Update with your service account key path
firebase_admin.initialize_app(cred, {
    'storageBucket': 'model-lab-practise-d0497.appspot.com'  # Replace with your project ID
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    # Upload file to Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    return f'File {file.filename} uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
