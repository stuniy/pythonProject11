from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
from ModPred import ModPred

# load model
model=pickle.load(open("predictor_model1.pkl",'rb'))

app=FastAPI()

@app.get("/")
def read_root():
    return {"msg":"Predictor"}

@app.post("/predict")
def predict_price(data:ModPred):
    data = data.dict()
    bilirubin=data['bilirubin']
    neutrophils=data['neutrophils']
    amylase=data['amylase']
    duration=data['duration']
    lymphocytes=data['lymphocytes']
    prediction = model.predict([[bilirubin, neutrophils, amylase, duration, lymphocytes]])
    if (prediction[0] ==1):
        prediction = "есть"
    else:
        prediction = "нет"
    return {
        'prediction': prediction
    }

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    uvicorn.run(app, host="127.0.0.1", port=8000)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
