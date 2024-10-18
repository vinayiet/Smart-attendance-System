import streamlit as st
from deepface import DeepFace
from pymongo import MongoClient
from datetime import datetime
import numpy as np
from PIL import Image

# MongoDB Connection
uri = "mongodb+srv://vinayiet435:1234567890@attendancemanagemtsyste.uzcm7.mongodb.net/?retryWrites=true&w=majority&appName=AttendanceManagemtSystem"
client = MongoClient(uri)
db = client["attendance_system"]
users_collection = db["users"]

# Initialize session state for navigation
if "section" not in st.session_state:
    st.session_state.section = None  # None = No section selected, 'register' or 'attendance'

def save_user(name, email, image_embedding):
    """Save user data to MongoDB and log the result."""
    try:
        user_data = {
            "name": name,
            "email": email,
            "images": [image_embedding],  # Store as a list of embeddings
            "attendance": []
        }
        users_collection.insert_one(user_data)
        st.success("User registered successfully!")
    except Exception as e:
        st.error(f"Failed to register user: {e}")

def get_all_users():
    """Retrieve all registered users from MongoDB."""
    try:
        return list(users_collection.find({}))
    except Exception as e:
        st.error(f"Error fetching users: {e}")
        return []

def mark_attendance(user_id):
    """Mark attendance for a recognized user."""
    try:
        users_collection.update_one(
            {"_id": user_id},
            {"$push": {"attendance": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}
        )
        st.success("Attendance marked successfully!")
    except Exception as e:
        st.error(f"Error marking attendance: {e}")

def get_face_embedding(image):
    """Extract face embedding using DeepFace."""
    try:
        result = DeepFace.represent(image, model_name='Facenet')
        return result[0]['embedding']
    except Exception as e:
        st.error(f"Failed to generate embedding: {e}")
        return None

def cosine_similarity(embedding1, embedding2):
    """Compute cosine similarity between two embeddings."""
    return np.dot(embedding1, embedding2) / (np.linalg.norm(embedding1) * np.linalg.norm(embedding2))

st.title("Facial Recognition Attendance System")

# Sidebar for navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Register", key="register_button"):
    st.session_state.section = "register"
elif st.sidebar.button("Mark Attendance", key="attendance_button"):
    st.session_state.section = "attendance"

# Registration Section
if st.session_state.section == "register":
    st.subheader("User Registration")
    name = st.text_input("Name", key="name_input")
    email = st.text_input("Email", key="email_input")

    image_data = st.camera_input("Capture your image", key="camera_register")
    if st.button("Register", key="submit_register"):
        if name and email and image_data:
            image = np.array(Image.open(image_data))
            embedding = get_face_embedding(image)

            if embedding is not None:
                save_user(name, email, embedding)
        else:
            st.error("Please provide name, email, and capture your image.")

# Attendance Section
if st.session_state.section == "attendance":
    st.subheader("Mark Attendance")
    st.write("Please capture your image to mark attendance.")

    image_data = st.camera_input("Capture your image", key="camera_attendance")
    if image_data and st.button("Mark Attendance", key="submit_attendance"):
        image = np.array(Image.open(image_data))
        captured_embedding = get_face_embedding(image)

        if captured_embedding is not None:
            users = get_all_users()
            matched_user = None
            threshold = 0.7  # Adjust as needed

            for user in users:
                if 'images' in user and user['images']:
                    for stored_embedding in user['images']:
                        similarity = cosine_similarity(np.array(stored_embedding), captured_embedding)
                        if similarity > threshold:
                            matched_user = user
                            break
                if matched_user:
                    break

            if matched_user:
                mark_attendance(matched_user["_id"])
            else:
                st.error("Face not recognized! Please try again.")
