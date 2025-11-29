from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/predict")
def predict():
    return {"message": "Hello from AI Core!"}
