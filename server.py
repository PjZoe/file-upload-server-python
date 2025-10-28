# Author: Nadika Prabhath
# GitHub Username: nadikaprabhath
# GitHub URL: https://github.com/nadikaprabhath
# Copyright (c) 2025 Nadika Prabhath. All rights reserved.

import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()  # Saves to the current directory
app.secret_key = 'super_secret_key'  # For flash messages, change this in production

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'doc', 'docx'}  # Add more as needed

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print(f"Request Content-Type: {request.content_type}")  # Debug: Shows if multipart
        print(f"Request Files: {request.files.keys()}")  # Debug: Should show 'file' if correct
        
        # Handle file/photo upload
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No file selected')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(f'File saved: {filename}')
                return 'File uploaded successfully!'
            else:
                return 'Invalid file type'
        
        # Handle text share (if no file, assume text in body)
        elif request.data:
            try:
                text = request.data.decode('utf-8')
                filename = 'shared_text.txt'
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
                    f.write(text)
                print(f'Text saved: {filename}')
                return 'Text shared successfully!'
            except UnicodeDecodeError:
                # Fallback for binary data mistakenly sent as text
                filename = 'shared_binary.dat'
                with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as f:
                    f.write(request.data)
                print(f'Binary data saved as: {filename} (likely a misconfigured file upload)')
                return 'Binary data received (check Shortcut setup for files)'
        
        else:
            return 'No data received'
    
    return 'Server is running'

if __name__ == '__main__':
    print("")
    print("-------------------------------------------------------")
    print("Author: Nadika Prabhath")
    print("GitHub Username: nadikaprabhath")
    print("GitHub URL: https://github.com/nadikaprabhath")
    print("Copyright (c) 2025 Nadika Prabhath. All rights reserved.")
    print("-------------------------------------------------------")
    print("")
    
    app.run(host='0.0.0.0', port=5000, debug=True)