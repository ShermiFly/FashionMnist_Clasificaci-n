from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # Aquí iría la lógica para cargar el modelo y predecir la imagen
    return {"result": "clase_predicha"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
