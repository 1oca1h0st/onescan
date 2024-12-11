from fastapi import APIRouter, Depends

from app.crud.projects import list_projects, create_project
from app.schemas.projects import ProjectBase
from app.utils.jwt_helper import oauth2_scheme, get_current_user

router = APIRouter(dependencies=[Depends(oauth2_scheme)])


@router.get("/list")
async def get_list_projects():
    return await list_projects(10)


@router.post("/create")
async def post_create_project(project: ProjectBase, token: str = Depends(oauth2_scheme)):
    sub = await get_current_user(token)
    return await create_project(project, sub)
