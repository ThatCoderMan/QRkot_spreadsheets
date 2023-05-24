from fastapi import APIRouter

from app.api.endpoints import (charity_project_router, donations_router,
                               google_api_router, user_router)

main_router = APIRouter()
main_router.include_router(
    charity_project_router, prefix='/charity_project', tags=['Charity Project']
)
main_router.include_router(
    donations_router, prefix='/donation', tags=['Donations']
)
main_router.include_router(
    google_api_router, prefix='/google', tags=['Google']
)
main_router.include_router(user_router)
