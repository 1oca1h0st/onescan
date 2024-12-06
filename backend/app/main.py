from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from app.api.v1 import users
from app.database.database import connect_db, close_db

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from middleware.auth import JWTMiddleware

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_db_client():
    await connect_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db()


app.add_middleware(JWTMiddleware)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/login", name="login")
async def login(request: Request):
    return templates.TemplateResponse("sign-in.jinja2", {"request": request})


@app.get("/forgot_password", name="forgot_password")
async def forgot_password(request: Request):
    return templates.TemplateResponse("forgot-password.jinja2", {"request": request})


@app.get("/sign_up", name="sign_up")
async def sign_up(request: Request):
    return templates.TemplateResponse("sign-up.jinja2", {"request": request})


@app.get("/dashboard", name="dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.jinja2", {"request": request})
