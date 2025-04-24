
# Face Recognition Attendance System

This is a Python-based attendance system that uses face recognition to mark and manage attendance for students. The system includes functionalities for login, signup, image capture, attendance tracking, and student record management.

## 🧠 Features

- **Face Recognition**: Detect and recognize student faces using OpenCV and `face_recognition`.
- **Student Management**: Add, delete, and view student details.
- **Attendance Logging**: Mark attendance based on real-time face recognition.
- **CSV Export**: Attendance data is saved in `attendance.csv`.
- **User Authentication**: Secure login and signup system for access control.

## 📁 Project Structure

```
.
├── attendance.csv        # Stores attendance data
├── attendance.py         # Handles attendance logic using face recognition
├── developer.py          # About developer or developer tools
├── face_recognition.py   # Core face recognition logic
├── help.py               # Help section or usage instructions
├── login2.py             # Login interface logic
├── main.py               # Main application launcher (Tkinter GUI)
├── showimg.py            # Utility to display student images
├── SignUp.py             # User signup logic
├── student.py            # Student record management
```

## 💻 Requirements

Install the following packages before running:

```bash
pip install opencv-python face_recognition numpy pandas
```

Make sure you have:
- A webcam connected
- Python 3.6+

## 🚀 How to Run

1. Launch the application:

```bash
python main.py
```

2. Sign up or log in.
3. Use the GUI to:
   - Add students
   - Capture images
   - Recognize faces and mark attendance
   - View attendance records

## ✍️ Developer Info

Check `developer.py` for information about the developer.

## 🆘 Help

Run:

```bash
python help.py
```

or click **Help** in the GUI for instructions.

## 📌 Notes

- Face data should be stored in a folder that `face_recognition.py` reads from.
- Attendance is automatically saved with timestamps in the `attendance.csv` file.

## 📄 License

This project is for educational purposes.
