from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# means page router
p_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@p_router.get("/", name="dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.jinja2", {"request": request})


@p_router.get("/login", name="login")
async def login(request: Request):
    return templates.TemplateResponse("sign-in.jinja2", {"request": request})


@p_router.get("/forgot_password", name="forgot_password")
async def forgot_password(request: Request):
    return templates.TemplateResponse("forgot-password.jinja2", {"request": request})


@p_router.get("/sign_up", name="sign_up")
async def sign_up(request: Request):
    return templates.TemplateResponse("sign-up.jinja2", {"request": request})
