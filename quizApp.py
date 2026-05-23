import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Quiz App",
    layout="wide",
)

st.title(" General Knowledge Quiz App")

# Question 1
st.header("Question 1")
q1 = st.radio(
    "**Which planet is known as the Red Planet?**",
    ["Venus", "Mars", "Jupiter", "Saturn"]
)
st.divider()

# Question 2
st.header("Question 2")
image = Image.open("monalisa.jpeg")
st.image(image, width=250)
q2 = st.radio(
    "**Who painted this painting?**",
    ["Michelangelo", "Raphael", "Leonardo da Vinci", "Vincent van Gogh"]
)
st.divider()

# Question 3
st.header("Question 3")
q3 = st.radio(
    "**What is the tallest building in the world?**",
    ["Shanghai Tower", "Burj Khalifa", "Merdeka 118", "Empire State Building"]
)

# Submit button
if st.button("Submit Answers"):
    score = 0

    # Check Q1
    if q1 == "Mars":
        st.success("Q1 Correct!")
        score += 1
    else:
        st.error("Q1 Wrong!")

    # Check Q2
    if q2 == "Leonardo da Vinci":
        st.success("Q2 Correct!")
        score += 1
    else:
        st.error("Q2 Wrong!")

    # Check Q3
    if q3 == "Burj Khalifa":
        st.success("Q3 Correct!")
        score += 1
    else:
        st.error("Q3 Wrong!")

    st.divider()

    # Final Score
    st.subheader(f"Your Score: {score}/3")