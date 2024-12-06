import os
import platform
import psutil


def get_os_type():
    """获取操作系统类型"""
    return platform.system()


def get_uptime():
    """获取系统运行时间"""
    uptime_seconds = psutil.boot_time()
    return uptime_seconds


def get_cpu_usage():
    """获取CPU使用率"""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """获取内存使用率"""
    memory_info = psutil.virtual_memory()
    return {
        'total': memory_info.total,
        'available': memory_info.available,
        'percent': memory_info.percent,
        'used': memory_info.used,
        'free': memory_info.free
    }
