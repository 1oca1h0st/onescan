from pydantic import EmailStr
from starlette.responses import JSONResponse

from app.database.database import get_database
from app.schemas.projects import ProjectBase, ProjectCreate, ProjectResponse


async def list_projects(limit: int = 10):
    db = get_database()
    project_collection = db['projects']
    projects = await project_collection.find().limit(limit).to_list(length=limit)
    return projects


async def create_project(project: ProjectBase, sub: EmailStr):
    db = get_database()
    user_collection = db['users']
    user = await user_collection.find_one({'email': sub})
    if user is None:
        return JSONResponse(status_code=403, content={"detail": "用户不存在"})

    project_info = ProjectCreate(
        name=project.name,
        owner=str(user['_id']),
    )

    project_collection = db['projects']
    try:
        # 插入项目数据
        result = await project_collection.insert_one(project_info.dict())
        if str(result.inserted_id):
            created_project_info = await project_collection.find_one({'_id': result.inserted_id})
            return ProjectResponse(**created_project_info)
        return JSONResponse(status_code=500, detail="项目插入失败")
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
