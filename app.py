from flask import Flask, request, render_template, send_file
import os
from phone_formatter import process_csv

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'cleaned'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename == '':
        return '❌ No selected file'
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    output_file = os.path.join(OUTPUT_FOLDER, 'cleaned_numbers.csv')

    file.save(filepath)
    process_csv(filepath, output_file)

    return send_file(output_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
