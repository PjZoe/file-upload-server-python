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
        # Handle file/photo upload
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No file selected')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(f'File saved: {filename}')  # Logs to console
                return 'File uploaded successfully!'
            else:
                return 'Invalid file type'
        
        # Handle text share (if no file, assume text in body)
        elif request.data:
            text = request.data.decode('utf-8')
            filename = 'shared_text.txt'
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as f:
                f.write(text)
            print(f'Text saved: {filename}')  # Logs to console
            return 'Text shared successfully!'
        
        else:
            return 'No data received'
    
    return 'Server is running'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)