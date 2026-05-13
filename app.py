from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from TextSummarizationProject.pipeline.prediction import PredictionPipeline

text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response(content="Training completed successfully.", media_type="text/plain")
    except Exception as e:        
        return Response(content=f"An error occurred during training: {str(e)}", media_type="text/plain")  
    

@app.post("/predict")
async def predict(text: str):
    try:
        predictor = PredictionPipeline()
        summary = predictor.predict(text)
        return Response(content=f"Generated Summary: {summary}", media_type="text/plain")
    except Exception as e:
        return Response(content=f"An error occurred during prediction: {str(e)}", media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)