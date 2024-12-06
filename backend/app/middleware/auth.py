from fastapi import Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from app.utils.jwt_helper import verify_token  # 确保此函数能够验证您的 JWT 令牌

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # 跳过静态资源和非 API 端点的 JWT 身份验证
        if not path.startswith("/api"):
            return await call_next(request)

        if path in ["/api/v1/users/login", "/api/v1/users/register"]:
            return await call_next(request)

        authorization: str = request.headers.get("Authorization")
        if authorization:
            try:
                scheme, token = authorization.split()
                if scheme.lower() != "bearer":
                    return JSONResponse(status_code=401, content={"detail": "无效的认证方案"})

                # 使用 verify_token 函数来验证 JWT
                verify_token(token)
            except (ValueError, HTTPException):
                return JSONResponse(status_code=401, content={"detail": "无效或缺失的令牌"})
        else:
            return JSONResponse(status_code=401, content={"detail": "缺少授权头"})

        response = await call_next(request)
        return response
