## **Smart Attendance System**  

This project is a **facial recognition-based attendance system** that registers users and marks their attendance through captured images. It leverages **Streamlit** for the web interface, **MongoDB** for data storage, and **DeepFace** for facial recognition.

---

## **Table of Contents**  
1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Setup Instructions](#setup-instructions)  
4. [How to Use](#how-to-use)  
5. [Project Structure](#project-structure)  
6. [Known Issues](#known-issues)  
7. [Future Enhancements](#future-enhancements)  

---

## **Features**  
- **User Registration:** Capture the user’s image and save it with their details in MongoDB.  
- **Facial Recognition:** Attendance is marked when the user's face matches the stored embedding.  
- **Attendance Logs:** Attendance timestamps are stored for each recognized user.  
- **Simple Web Interface:** Streamlit-based UI for easy navigation.  

---

## **Tech Stack**  
- **Python:** Programming language.  
- **Streamlit:** Framework for building the web interface.  
- **DeepFace:** Library for facial recognition.  
- **MongoDB:** NoSQL database for storing user details and attendance logs.  
- **NumPy:** Library for numerical operations, including cosine similarity calculation.  
- **Pillow (PIL):** Library for image processing.  

---

## **Setup Instructions**  

### **1. Prerequisites**  
- Python 3.7+ installed on your machine.  
- MongoDB Atlas account (or local MongoDB server).  
- Install required Python libraries:
  ```bash
  pip install streamlit deepface pymongo pillow numpy
  ```

### **2. MongoDB Setup**  
1. Create a **cluster on MongoDB Atlas** and get the connection URI.  
2. Replace the `uri` variable in `app.py` with your MongoDB connection string:
   ```python
   uri = "your_mongodb_connection_string"
   ```

### **3. Running the Project**  
Navigate to the project directory and run the Streamlit app:
```bash
streamlit run app.py
```
This will open the app in your browser at `http://localhost:8501`.  

---

## **How to Use**  

### **1. User Registration**  
- Click on **"Register"** in the sidebar.  
- Enter your **Name** and **Email**.  
- Capture your image using the **camera input**.  
- Click **Register** to save the user details in MongoDB.

### **2. Mark Attendance**  
- Click on **"Mark Attendance"** in the sidebar.  
- Capture your image using the camera input.  
- If the face matches any registered user, attendance will be marked.  
- If no match is found, an error message will appear.  

---

## **Project Structure**  
```
facial-recognition-system/
│
├── app.py             # Main application code  
├── requirements.txt   # Python dependencies  
└── README.md          # Project documentation (this file)  
```

---

## **Known Issues**  
1. **Face Matching with Accessories:** If registered with glasses, attendance might not be marked without glasses.  
2. **Performance:** Facial recognition might slow down for large datasets.  
3. **Similarity Threshold:** Adjust the threshold value if face matching is too strict or lenient.

---

## **Future Enhancements**  
- **Support for Multiple Embeddings:** Store multiple embeddings per user to handle variations (e.g., with/without glasses).  
- **Admin Dashboard:** Add an admin interface to view user lists and attendance records.  
- **Email Notifications:** Notify users when their attendance is marked.  
- **Mobile App Integration:** Extend functionality to a mobile app for ease of use.  

---

## **Contributors**  
- **Vinay Sharma**

