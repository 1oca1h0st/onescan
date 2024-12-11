from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class ProjectCreate(ProjectBase):
    owner: str
    pass


class ProjectResponse(ProjectBase):
    owner: str
    pass
