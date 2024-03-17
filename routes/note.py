from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()

# Initialize the Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Define the root route
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    
    docs = conn.notes.notes.find({})
    return templates.TemplateResponse(request= request, name="index.html", context={"newDocs": docs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    
    note = conn.notes.notes.insert_one(formDict)
    docs = conn.notes.notes.find({})
    
    # return templates.TemplateResponse(request= request, name="index.html", context={"newDocs": docs})
    return {"Success": "Note created successfully."}
    
