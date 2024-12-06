### **User Authentication Mini Project**

This project demonstrates a simple **User Authentication System** using **FastAPI** as the backend and **Streamlit** as the frontend. It includes user registration, login, and token-based authentication using JWT.

---

### **Features**
- **User Registration**: Securely register users with hashed passwords.
- **User Login**: Authenticate users and issue JSON Web Tokens (JWT).
- **Frontend Interface**: A Streamlit web application for user interaction.
- **Session Management**: Maintain login sessions using JWT tokens.
- **Single-page Navigation**: Switch between Login and Register pages dynamically.

---

### **Requirements**

#### **Backend (FastAPI)**
The FastAPI application handles:
- User registration
- User login
- JWT token generation and verification

#### **Frontend (Streamlit)**
The Streamlit application serves as the user interface:
- Allows users to register or login.
- Displays appropriate feedback messages.

---

### **Libraries Required**

#### **Backend Libraries**
1. **FastAPI**: For creating the backend API.
2. **uvicorn**: ASGI server to run the FastAPI app.
3. **Pydantic**: For data validation and schema definition.
4. **Python-Jose**: For encoding and decoding JWT tokens.
5. **Passlib**: For securely hashing passwords.

Install these libraries using:
```bash
pip install fastapi uvicorn pydantic python-jose passlib[bcrypt]
```

#### **Frontend Libraries**
1. **Streamlit**: For creating the web application.
2. **Requests**: To send HTTP requests from Streamlit to FastAPI.

Install these libraries using:
```bash
pip install streamlit requests
```

---

### **How to Run the Project**

#### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/auth-mini-project.git
cd auth-mini-project
```

#### **2. Start the Backend Server**
1. Navigate to the backend folder or ensure the FastAPI code is in the root.
2. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```
3. The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### **3. Start the Frontend App**
1. Navigate to the folder with the Streamlit app.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the app in your browser, typically at [http://localhost:8501](http://localhost:8501).

---

### **Project Structure**
```
auth-mini-project/
├── main.py         # FastAPI backend code
├── app.py          # Streamlit frontend code
├── README.md       # Project documentation
└── requirements.txt # List of required libraries
```

---

### **Endpoints**

#### **Backend API**
- **POST /register**: Register a new user.
  - **Payload**: `{ "username": "string", "password": "string" }`
  - **Response**: Success or error message.
- **POST /login**: Authenticate a user.
  - **Payload**: `{ "username": "string", "password": "string" }`
  - **Response**: JWT token for the authenticated user.

#### **Frontend Navigation**
- **Login Page**: Accepts username and password for authentication.
- **Register Page**: Accepts username and password to create a new user.

---

### **Example Usage**

#### **Register a New User**
1. Navigate to the **Register** page.
2. Enter a username and password, then click "Register."
3. You should see a success message.

#### **Login as a User**
1. Navigate to the **Login** page.
2. Enter the registered username and password, then click "Login."
3. Upon successful login, you will see a success message and session info.

#### **Logout**
1. Use the "Logout" button on the sidebar to end the session.

---
Images:
![image](https://github.com/user-attachments/assets/38f1e796-4f9e-44c1-9a6c-95c1e4387998)

---

### **Additional Notes**
1. The project uses a temporary in-memory database (`users_db`) for simplicity. You can replace this with a real database for production use.
2. Passwords are securely hashed using `bcrypt` from the Passlib library.
3. JWT tokens are signed using the `HS256` algorithm and include an expiration time.

---

### **Contributing**
Feel free to submit pull requests or open issues for any suggestions or bug fixes.

---

Created by Harsh
