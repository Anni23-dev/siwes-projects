import streamlit as st

# Set up the web page title and icon
st.set_page_config(page_title="Retro Calculator", page_icon="🧮")

# Apply custom CSS to style the app with Pink, Purple, and Black
st.markdown("""
    <style>
    /* Change the main app background to black */
    .stApp {
        background-color: #000000;
    }
    
    /* Style the main title */
    h1 {
        color: #FF69B4 !important; /* Hot Pink */
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    
    /* Style the input boxes */
    .stNumberInput div div input {
        background-color: #1A1A1A !important; /* Dark Black/Gray */
        color: #00FFFF !important; /* Neon Cyan text for readability */
        border: 2px solid #8A2BE2 !important; /* Purple border */
        border-radius: 8px;
    }
    
    /* Style the dropdown selector */
    .stSelectbox div div div {
        background-color: #1A1A1A !important;
        color: #FF69B4 !important; /* Pink text */
        border: 1px solid #8A2BE2 !important;
    }
    
    /* Style the action button */
    .stButton button {
        background-color: #8A2BE2 !important; /* Purple background */
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        border: 2px solid #FF69B4 !important; /* Pink border */
        transition: 0.3s;
    }
    
    /* Button hover effect */
    .stButton button:hover {
        background-color: #FF69B4 !important; /* Turns pink on hover */
        color: black !important;
    }
    
    /* Style the result box */
    .result-box {
        background-color: #121212;
        padding: 20px;
        border-radius: 10px;
        border: 2px dashed #FF69B4;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# App layout
st.title("Anni's Calculator")
st.write("---")

# Create two columns for the number inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number:", value=0.0)

with col2:
    num2 = st.number_input("Enter second number:", value=0.0)

# Create an operation dropdown selector
operation = st.selectbox("Choose an operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

st.write("") # Adds spacing

# Calculate result when the button is clicked
if st.button("Calculate Result"):
    result = 0
    error_message = None
    
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            error_message = "Error: Cannot divide by zero!"

    # Display the result inside our custom styled box
    st.write("")
    if error_message:
        st.markdown(f'<div class="result-box"><h2 style="color: red;">{error_message}</h2></div>', unsafe_allow_html=True)
    else:
        # Check if result is a whole number to keep it clean
        if result.is_integer():
            result = int(result)
        st.markdown(f'<div class="result-box"><h2 style="color: #FF69B4;">Result: {result}</h2></div>', unsafe_allow_html=True)
