from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1 import users, system_info
from app.database.database import connect_db, close_db
from celery_tasks.config import create_task
from i18n.i18n import set_locale, _
from middleware.auth import JWTMiddleware
from router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    application lifecycle management function
    """
    await connect_db()
    set_locale("en_US")
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(system_info.router, prefix="/api/v1/system_info", tags=["System Info"])
app.include_router(router.p_router, tags=["Pages"])

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")

app.add_middleware(JWTMiddleware)


# some test routes
@app.get("/1111/{task_id}")
async def aaa(task_id: int):
    return create_task(task_id)


@app.get("/i18n")
async def i18n():
    return {"message": _("aaaa")}
