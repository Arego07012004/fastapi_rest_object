from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, schemas, database

app = FastAPI()
db_dependency = database.SessionLocal

def get_db():
    db = db_dependency()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get("/students/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    return crud.get_student(db, student_id)

@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return crud.delete_student(db, student_id)

