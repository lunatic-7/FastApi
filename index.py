from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Initialize static files
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)