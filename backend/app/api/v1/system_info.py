from fastapi import APIRouter, Depends

from app.utils.jwt_helper import oauth2_scheme
from app.utils.system_info import get_os_type, get_uptime, get_cpu_usage, get_memory_usage

router = APIRouter(dependencies=[Depends(oauth2_scheme)])


@router.get("/os_type")
def read_os_type():
    """获取操作系统类型"""
    return {"os_type": get_os_type()}


@router.get("/uptime")
def read_uptime():
    """获取系统运行时间"""
    return {"uptime_seconds": get_uptime()}


@router.get("/cpu_usage")
def read_cpu_usage():
    """获取CPU使用率"""
    return {"cpu_usage_percent": get_cpu_usage()}


@router.get("/memory_usage")
def read_memory_usage():
    """获取内存使用率"""
    return get_memory_usage()
