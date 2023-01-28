import streamlit as st
import requests
import json


def main():
    st.title("Предсказание осложнений после операции")

    bilirubin = st.number_input("Билирубин")

    neutrophils = st.number_input("Нейрофилы")

    amylase = st.number_input("Амилазе")

    duration = st.number_input("Длительность операции")

    lymphocytes = st.number_input("Лимфоциты")

    input_data = {
        "bilirubin": bilirubin,
        "neutrophils": neutrophils,
        "amylase": amylase,
        "duration": duration,
        "lymphocytes": lymphocytes,
    }

    price = 0
    if st.button("Predict"):
        price = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_data))
        price = price.json()
        p = price['prediction']
        st.success(f'Осложнения {p} ')


if __name__ == '__main__':
    main()