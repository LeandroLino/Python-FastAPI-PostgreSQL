from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    post_count: int

class PostResponse(BaseModel):
    version: str
    message: str
    total_calls: int
