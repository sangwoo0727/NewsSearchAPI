from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"]
    )
    from app.router.search_router import search_router
    from app.router.test_router import test_router
    from app.router.agg_router import agg_router
    from app.router.vector_search_router import vector_search_router
    app.include_router(search_router)
    app.include_router(test_router)
    app.include_router(agg_router)
    app.include_router(vector_search_router)

    return app


