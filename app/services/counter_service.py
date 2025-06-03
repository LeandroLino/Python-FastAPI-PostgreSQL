from sqlalchemy.orm import Session
from app.models.counter import APICounter

class CounterService:
    @staticmethod
    def get_counter(db: Session, endpoint: str) -> int:
        counter = db.query(APICounter).filter(APICounter.endpoint == endpoint).first()
        if not counter:
            counter = APICounter(endpoint=endpoint, count=0)
            db.add(counter)
            db.commit()
            db.refresh(counter)
        return counter.count
    
    @staticmethod
    def increment_counter(db: Session, endpoint: str) -> int:
        counter = db.query(APICounter).filter(APICounter.endpoint == endpoint).first()
        if not counter:
            counter = APICounter(endpoint=endpoint, count=1)
            db.add(counter)
        else:
            counter.count += 1
        db.commit()
        db.refresh(counter)
        return counter.count
