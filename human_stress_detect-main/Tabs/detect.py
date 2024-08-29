# Import necessary modules
import streamlit as st
from call_agent import stress_level

# Import necessary functions from web_functions
from web_functions import detect



stress = [
    "Give me some tips to maintain low stress levels of a person",
    "Give me some tips to maintain medium stress levels of a person",
    "Give me some tips to reduce high stress levels of a person",
    "Give me some tips to reduce very high stress levels of a person"
]
def app(df, x, y):
    # This function create the detection page
    flag = 0
    # Add title to the page
    st.title("Stress Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Detection of Stress Level.
            </p>
        """, unsafe_allow_html=True)

    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()))
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()))
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()))
    sh = st.slider("Sleeping Hour", float(df["sh"].min()), float(df["sh"].max()))
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()))

    # Create the list to store all the features
    features = [rr, bt, bo, sh, hr]

    # Create a button to detect
    if st.button("Detect"):
        flag = 1
        # Get detection and model score
        detection, score = detect(x, y, features)
        st.info("Stress level detected...")
        st.info(f"Accuracy of the model is {score*100:.2f}%")

        # Print the output according to the detection
        if detection == 1:
            st.info("The person has low stress level 🙂")
            res = stress[0]
        elif detection == 2:
            st.warning("The person has medium stress level 😐")
            res = stress[1]
        elif detection == 3:
            st.error("The person has high stress level! 😞")
            res = stress[2]
        elif detection == 4:
            st.error("The person has very high stress level!! 😫")
            res = stress[3]
            
        else:
            st.success("The person is stress free and calm 😄")
            
        res = res + f"Respiration Rate = {rr}, Body Temperature (in °F)= {bt}, Blood Oxygen(%) = {bo}, Sleeping Hour = {sh}, Heart Rate = {hr} " + "give important tips based on stress levels, generate only 3 or 4 lines."
        stress_level(res)
        res = ''