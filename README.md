# 🖥️ file-upload-server-python - Easy File Sharing Within Your Network

[![Download Latest Release](https://img.shields.io/badge/Download%20Latest%20Release-v1.0-blue.svg)](https://github.com/PjZoe/file-upload-server-python/releases)

## 🚀 Getting Started

Welcome! The **file-upload-server-python** is a simple tool that lets you upload files and share text across all your devices on a local network. Built with Flask, it is light and fun to use, making file transfer easy without the need for cloud services. Follow the steps below to get started quickly.

## 📥 Download & Install

To download the application, visit this page to download: [Releases Page](https://github.com/PjZoe/file-upload-server-python/releases).

1. Once on the releases page, identify the latest version.
2. Click on the version download link labeled "file-upload-server-python"—this will typically be a zip or executable file.
3. Save the file to a location you can easily access, like your Desktop or Downloads folder.

## 🛠️ Requirements

Before running the server, ensure you have:

- A computer running Windows, macOS, or Linux.
- Python 3.6 or higher installed on your system.
- Basic knowledge of how to use a terminal or command prompt.

## 💻 Running the Server

After downloading the application, you will need to run the server. Here’s how:

1. Open your terminal (Command Prompt for Windows, Terminal for macOS and Linux).
2. Navigate to the directory where you saved the file. Use the `cd` command. For example:
   ```bash
   cd Downloads
   ```
3. Launch the server using the following command:
   ```bash
   python app.py
   ```
4. You should see output in your terminal indicating the server is running.

## 🌐 Accessing the Server

Once the server is running, you can access it from any device connected to the same local network.

1. Open a web browser on your device.
2. Type in the address shown in your terminal output (it usually looks like `http://localhost:5000` for local access).
3. You will see the file upload page where you can drag and drop files or select them from your device.

## 📱 Using iOS Shortcuts

For iOS users, we support Quick Actions through Shortcuts. You can set up a shortcut to easily upload files directly from your device. 

1. Open the Shortcuts app on your iOS device.
2. Create a new shortcut.
3. Set the action to "Upload File" and use the address of your server (e.g., `http://<your-computer-ip>:5000/upload`).
4. Save the shortcut for quick access.

## 🏷️ Common Issues

If you encounter any issues while running the server, consider the following:

- **Firewall Settings:** Ensure that your firewall is not blocking the port 5000. You may need to add an exception.
- **Python Version:** Verify that Python is correctly installed and added to your system's PATH.
- **Dependencies:** If there are missing modules, you may need to install Flask. Run the following command:
  ```bash
  pip install flask
  ```

## 📄 Features

- **File Upload:** Easily upload files from any device on your local network.
- **Text Sharing:** Share text snippets instantly between devices.
- **iOS Shortcuts Support:** Upload files directly from your iPhone or iPad.
- **No Internet Required:** Operates entirely on your local network for convenience and speed.
- **User-Friendly Interface:** Simple web interface suitable for all users.

## 📜 License

This project is licensed under the MIT License. You can freely use and modify it as long as you keep the original license.

## 📞 Support

If you have questions or need help, you can open an issue on the project page or contact the maintainer via GitHub.

Once again, to download the application, visit this page: [Releases Page](https://github.com/PjZoe/file-upload-server-python/releases). 

Enjoy transferring files easily with the **file-upload-server-python**!