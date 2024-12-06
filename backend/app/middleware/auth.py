# app/middleware/jwt_middleware.py

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse, RedirectResponse
from app.utils.jwt_helper import verify_token


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 静态资源检查
        path = request.url.path
        # 只对/api端点进行防护
        if not path.startswith("/api"):
            return await call_next(request)

        # 正常继续验证
        authorization: str = request.headers.get("Authorization")
        if authorization:
            try:
                scheme, token = authorization.split()
                if scheme.lower() != "bearer":
                    return JSONResponse(status_code=401, content={"detail": "Invalid authentication scheme"})
                verify_token(token)
            except (ValueError, HTTPException):
                return JSONResponse(status_code=401, content={"detail": "Invalid or missing token"})
        else:
            if request.url.path not in ("/api/v1/login", "/api/v1/register"):
                return JSONResponse(status_code=401, content={"detail": "Authorization header missing"})

        response = await call_next(request)
        return response
