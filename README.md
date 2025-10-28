# File Upload Server

A simple Flask-based file upload server that accepts files and text shares from any device on your local network.

## Features

- 📁 Upload multiple file types (images, documents, videos, PDFs)
- 📝 Share text content directly
- 🌐 Access from any device on the same network
- 🔒 File type validation for security
- ✅ Simple HTTP endpoint for easy integration
- 📱 iOS Shortcuts integration for quick sharing

## Supported File Types

- **Documents**: txt, pdf, doc, docx
- **Images**: png, jpg, jpeg, gif
- **Videos**: mp4, mov

## Installation

1. **Install Python 3.x** (if not already installed)

2. **Install Flask**:
```bash
pip install flask
```

3. **Download the script** and save it as `app.py`

## Usage

### Starting the Server

Run the server from your terminal:

```bash
python app.py
```

The server will start on `http://0.0.0.0:5000` and be accessible from any device on your network.

### Finding Your Server Address

1. Find your computer's local IP address:
   - **Windows**: `ipconfig` (look for IPv4 Address)
   - **Mac/Linux**: `ifconfig` or `ip addr` (look for inet address)

2. Access the server at: `http://YOUR_IP_ADDRESS:5000/upload`

### Uploading Files

**Using cURL:**
```bash
curl -F "file=@/path/to/your/file.jpg" http://YOUR_IP:5000/upload
```

**Using Python:**
```python
import requests

files = {'file': open('document.pdf', 'rb')}
response = requests.post('http://YOUR_IP:5000/upload', files=files)
print(response.text)
```

**Using JavaScript/Fetch:**
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://YOUR_IP:5000/upload', {
    method: 'POST',
    body: formData
})
.then(response => response.text())
.then(data => console.log(data));
```

### Sharing Text

```bash
curl -X POST -d "Your text content here" http://YOUR_IP:5000/upload
```

Text will be saved as `shared_text.txt` in the server directory.

## iOS Shortcuts Setup

### Shortcut for Files or Photos

1. Open **Shortcuts** app → Tap **"+"** to create a new shortcut
2. Add action: Search for **"Get Contents of URL"**
3. Configure:
   - **Method**: POST
   - **URL**: `http://YOUR_LAPTOP_IP:5000/upload` (replace with your actual IP)
   - **Request Body**: 
     - Tap the "File" label (or circle next to it) and change type to **Form**
     - Once set to Form, tap **"Add New Field"** (or + icon)
     - Choose field type: **File**
     - Set **Key**: `file` (exactly, lowercase)
     - Set **Value**: Tap "Choose Variable" → Select **Shortcut Input** (this takes the shared photo/file from the share sheet)
     - *(Optional)* Add more fields as "Text" type for additional data
   - **Note**: No need to add Content-Type header – Shortcuts sets "multipart/form-data" automatically for Form with File fields
4. *(Optional)* Add a **"Show Notification"** action at the end with text like "File sent!" to confirm success
5. Name it something like **"Share File to Laptop"**

**To use**: In Photos app (for photos) or Files app (for files), select the item → Share → More → Run your shortcut. It will send the file to your laptop's server.

### Shortcut for Text

1. Create a new shortcut
2. Add action: **"Get Contents of URL"**
3. Configure:
   - **Method**: POST
   - **URL**: `http://YOUR_LAPTOP_IP:5000/upload`
   - **Request Body**: 
     - Tap **"Add New Field"** → Choose **"Text"**
     - **Key**: (leave blank or use 'text')
     - **Value**: **Shortcut Input** (or use "Get Clipboard" if sharing copied text)
4. *(Optional)* Add confirmation notification
5. Name it **"Share Text to Laptop"**

**To use**: Copy text → Open Shortcuts → Run it. Or add to share sheet for notes/apps.

## Configuration

### Change Upload Directory

Edit this line in the code:
```python
app.config['UPLOAD_FOLDER'] = os.getcwd()  # Change to your desired path
```

### Add More File Types

Edit the `ALLOWED_EXTENSIONS` set:
```python
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'zip', 'mp3'}  # Add your types
```

### Change Port

Modify the last line:
```python
app.run(host='0.0.0.0', port=8080, debug=True)  # Change port number
```

## Security Notes

⚠️ **Important**: This server is designed for local network use only.

- Change `app.secret_key` to a random string before production use
- Files are saved to the current directory by default
- Set `debug=False` in production environments
- Consider adding authentication for sensitive use cases
- Only use on trusted networks

## Troubleshooting

**Port already in use:**
```bash
# Use a different port
python app.py --port 5001
```

**Cannot access from other devices:**
- Check firewall settings
- Ensure devices are on the same network
- Verify the correct IP address is being used

**File not saving:**
- Check write permissions in the upload directory
- Ensure sufficient disk space

**iOS Shortcut not working:**
- Verify your laptop's IP address is correct
- Ensure the server is running
- Check that both devices are on the same Wi-Fi network
- Make sure the Request Body is set to "Form" type, not "File" or "JSON"

## Example Use Cases

- Quick file transfers between devices
- Mobile photo uploads to PC
- Simple document sharing in local networks
- Text snippet sharing between devices
- One-tap photo backup from iPhone to laptop

## License

MIT License

Copyright (c) 2025 Nadika Prabhath

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

**Created by Nadika Prabhath**
