import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("diet.pkl", "rb"))

st.title("Diet Recommendation")

age = st.text_area("Enter age")
wt = st.text_area("Enter weight in kg's")
ht = st.text_area("Enter height in meters")

li = ["Male", "Female"]
col = {"Female": 0, "Male": 1}
gender = st.selectbox("Select gender", li)

if age and wt and ht:
    try:
        age = float(age)
        wt = float(wt)
        ht = float(ht)

        bmi = float(wt / (ht * ht))

        if gender == "Female":
            bmr = float(655.1 + (9.563 * wt) + (1.850 * ht * 100) - (4.676 * age))
        else:
            bmr = float(66.5 + (13.75 * wt) + (5.003 * ht * 100) - (6.75 * age))

        ali = [1.2, 1.3, 1.5, 1.7, 1.9]
        act_lvl = st.selectbox("Select activity level", ali)

        gend = col.get(gender)

        data = np.array([[age, wt, ht, gend, bmi, bmr, act_lvl]])

        if st.button("Click"):
            re = model.predict(data)
            st.write(f"Recommended diet: {re[0]}")
            st.write(bmi)
            st.write(bmr)


    except ValueError:
        st.error("Please enter valid numeric values for age, weight, and height.")
else:
    st.warning("Please fill in all fields (age, weight, and height).")
