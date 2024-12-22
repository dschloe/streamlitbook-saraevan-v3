from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import endpoints
from .config import get_settings

def create_application() -> FastAPI:
    settings = get_settings()
    
    app = FastAPI(
        title=settings.app_name,
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    # CORS 설정
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # API 라우터 등록
    app.include_router(
        endpoints.router,
        prefix=settings.api_v1_prefix
    )
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}
    
    return app

app = create_application() 