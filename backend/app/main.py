from contextlib import asynccontextmanager

from celery.result import AsyncResult
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.v1 import users, system_info, projects
from app.database.database import connect_db, close_db
from app.models.targets import Targets
from celery_tasks.config import create_task, create_scan_task_cert, create_scan_nmap_scan
from i18n.i18n import set_locale, _
from middleware.auth import JWTMiddleware
from models.cert import Cert
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
app.include_router(projects.router, prefix="/api/v1/projects", tags=["Projects"])
app.include_router(router.p_router, tags=["Pages"])

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")

app.add_middleware(JWTMiddleware)


# some test routes
@app.get("/1111/{task_id}")
async def aaa(task_id: int):
    return create_task(task_id)


@app.get("/celery/result/{task_id}")
async def get_result(task_id: str):
    return AsyncResult(task_id).status


@app.get("/i18n")
async def i18n():
    return {"message": _("aaaa")}


@app.post("/celery/scan/cert")
async def cert(cert: Cert):
    return create_scan_task_cert(cert.domain)


@app.post("/celery/scan/nmap")
async def nmap(targets: Targets):
    return create_scan_nmap_scan(targets.ips)
