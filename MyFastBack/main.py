import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import jap

app = FastAPI(title='Jefferson API', description='Jefferson Backend')

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

app.include_router(jap.router)


# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
