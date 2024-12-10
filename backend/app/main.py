from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1 import users, system_info
from app.database.database import connect_db, close_db
from celery_tasks.config import create_task
from middleware.auth import JWTMiddleware
from router import router

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(system_info.router, prefix="/api/v1/system_info", tags=["System Info"])
app.include_router(router.p_router, tags=["Pages"])

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_db_client():
    await connect_db()


@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db()


app.add_middleware(JWTMiddleware)


@app.get("/1111")
async def aaa():
    return create_task(123)
