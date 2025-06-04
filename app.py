import uvicorn
from fastapi import FastAPI
from api.routes.predict_routes import router as predict_routes
from api.routes.product_routes import router as product_routes
app = FastAPI()

app.include_router(predict_routes, prefix="/api")
app.include_router(product_routes, prefix="/api")

@app.get("/ping")
async def ping():
    return {"message": "pong"}

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0",
                port=8000, reload=True)