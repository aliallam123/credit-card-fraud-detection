from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Credit Card Fraud Detection API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}