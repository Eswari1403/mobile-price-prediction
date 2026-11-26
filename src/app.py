
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="centered"
)

# Load trained model
model_path = (
    Path(__file__).parent
    / "saved_models"
    / "logistic_regression_model.pkl"
)

model = joblib.load(model_path)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: #EAEAFF;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

h1 {
    color: #292477 !important;
    text-align: center;
    font-size: 38px !important;
}

h2, h3 {
    color: #39318A !important;
}

[data-testid="stForm"] {
    background: #FFFFFF;
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #D6D3F5;
}

[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 15px;
    border-radius: 14px;
    border: 1px solid #D6D3F5;
}

.stButton button,
.stFormSubmitButton button {
    background: linear-gradient(90deg, #7652DC, #5734B5);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    min-height: 45px;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    background: #39218B;
    color: white;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# Dashboard heading
st.title("📱 Mobile Price Predictor")

st.markdown(
    "<p style='text-align:center;color:#555577;'>"
    "Predict mobile phone price category using Machine Learning"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

st.subheader("🤖 Selected Machine Learning Model")

st.info("Logistic Regression")

# Model performance
st.metric("Validation Accuracy", "97.50%")

st.divider()

st.subheader("📋 Enter Mobile Specifications")

with st.form("mobile_form"):

    # Important features
    st.markdown("### 🔋 RAM & Battery")

    col1, col2 = st.columns(2)

    with col1:
        ram = st.number_input(
            "RAM (MB)", 256, 4000, 2000
        )

    with col2:
        battery_power = st.number_input(
            "Battery Power (mAh)", 500, 2000, 1500
        )

    # Camera
    st.markdown("### 📸 Camera Specifications")

    col1, col2 = st.columns(2)

    with col1:
        fc = st.number_input(
            "Front Camera (MP)", 0, 19, 5
        )

    with col2:
        pc = st.number_input(
            "Primary Camera (MP)", 0, 20, 12
        )

    # Processor
    st.markdown("### ⚙️ Processor Specifications")

    col1, col2 = st.columns(2)

    with col1:
        n_cores = st.number_input(
            "Number of Cores", 1, 8, 4
        )

    with col2:
        clock_speed = st.number_input(
            "Clock Speed (GHz)", 0.5, 3.0, 1.5
        )

    # Additional features
    with st.expander("➕ Additional Mobile Specifications"):

        col1, col2 = st.columns(2)

        with col1:
            blue = st.selectbox("Bluetooth", [0, 1])
            dual_sim = st.selectbox("Dual SIM", [0, 1])
            four_g = st.selectbox("4G Support", [0, 1])
            three_g = st.selectbox("3G Support", [0, 1])
            wifi = st.selectbox("WiFi", [0, 1])
            touch_screen = st.selectbox("Touch Screen", [0, 1])
            int_memory = st.number_input(
                "Internal Memory (GB)", 2, 64, 32
            )
            mobile_wt = st.number_input(
                "Mobile Weight (g)", 80, 200, 150
            )
            m_dep = st.number_input(
                "Mobile Depth", 0.1, 1.0, 0.5
            )

        with col2:
            px_height = st.number_input(
                "Pixel Height", 0, 1960, 800
            )
            px_width = st.number_input(
                "Pixel Width", 500, 2000, 1200
            )
            sc_h = st.number_input(
                "Screen Height (cm)", 5, 19, 12
            )
            sc_w = st.number_input(
                "Screen Width (cm)", 0, 18, 7
            )
            talk_time = st.number_input(
                "Talk Time (hours)", 2, 20, 10
            )

    predict_button = st.form_submit_button(
        "🔍 Predict Mobile Price Category",
        use_container_width=True
    )


# Prediction
if predict_button:

    total_camera_mp = fc + pc
    processor_score = n_cores * clock_speed

    input_data = pd.DataFrame([{
        "battery_power": battery_power,
        "blue": blue,
        "clock_speed": clock_speed,
        "dual_sim": dual_sim,
        "fc": fc,
        "four_g": four_g,
        "int_memory": int_memory,
        "m_dep": m_dep,
        "mobile_wt": mobile_wt,
        "n_cores": n_cores,
        "pc": pc,
        "px_height": px_height,
        "px_width": px_width,
        "ram": ram,
        "sc_h": sc_h,
        "sc_w": sc_w,
        "talk_time": talk_time,
        "three_g": three_g,
        "touch_screen": touch_screen,
        "wifi": wifi,
        "total_camera_mp": total_camera_mp,
        "processor_score": processor_score
    }])

    prediction = model.predict(input_data)[0]

    price_categories = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    st.divider()
    st.subheader("📊 Prediction Result")

    st.success(
        f"Predicted Category: Class {prediction}"
    )

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(120deg,#7652DC,#39218B);
            padding:25px;
            border-radius:18px;
            text-align:center;
            color:white;
        ">
            <h3 style="color:white;">Estimated Price Category</h3>
            <h1 style="color:#FFE66D !important;">
                {price_categories[prediction]}
            </h1>
            <p style="color:white;">
                Based on the entered mobile specifications
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.caption(
    "Developed using Python, Streamlit and Logistic Regression"
)
