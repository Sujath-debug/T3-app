from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models
from .database import get_db

router = APIRouter()

@router.post("/tasks")
def create_task(title: str, description: str = None, db: Session = Depends(get_db)):
    task = models.Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Deleted"}
    return {"message": "Not found"}
