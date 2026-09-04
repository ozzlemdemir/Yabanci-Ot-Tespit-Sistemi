from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def main(request: Request):
    
    return templates.TemplateResponse(
        request, name="login.html")


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
   
    return templates.TemplateResponse(request, "dashboard.html")


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    
    return templates.TemplateResponse(request, "login.html")

@app.get("/register", response_class=HTMLResponse)
def register(request: Request):

    return templates.TemplateResponse(request, "register.html")

@app.get("/analizler", response_class=HTMLResponse)
def analizler(request: Request):
  
    return templates.TemplateResponse(request, "analyze.html")

@app.get("/profile", response_class=HTMLResponse)
def profil(request: Request):
    
    return templates.TemplateResponse(request, "profile.html")

@app.get("/gecmis", response_class=HTMLResponse)
def gecmis_analizler(request: Request):
   
    return templates.TemplateResponse(request, "history.html")
