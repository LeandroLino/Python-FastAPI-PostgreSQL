from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.services.counter_service import CounterService
from app.schemas.api_response import HealthCheckResponse, PostResponse
from app.core.config import settings

router = APIRouter()

@router.get("/health", response_model=HealthCheckResponse)
def health_check(db: Session = Depends(get_db)):
    """Rota de health check que retorna o número de chamadas POST"""
    post_count = CounterService.get_counter(db, "post_endpoint")
    return HealthCheckResponse(status="OK", post_count=post_count)

@router.post("/api", response_model=PostResponse)
def post_endpoint(db: Session = Depends(get_db)):
    """Rota POST que incrementa contador e retorna versão da API"""
    total_calls = CounterService.increment_counter(db, "post_endpoint")
    return PostResponse(
        version=settings.api_version,
        message="API chamada com sucesso",
        total_calls=total_calls
    )
