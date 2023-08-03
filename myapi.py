'''
Tutorial by: FreeCodeCamp
FastAPI for beginners
Tutorial link: https://www.youtube.com/watch?v=tLKKmouUams&t=261s&ab_channel=freeCodeCamp.org
'''

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

# end point is one end of the communication channel
# localhost/delete-user
# delete-user is the end point

# GET - Get an information
# POST - Create something new
# PUT - Update something in a particular object
# DELETE - Delete something

students = {
    1: {
        "name" : "umer",
        "age" : 26,
        "year" : "graduation"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/") # "/" is endpoint for home page
def index():
    return {"name": "First Data"}


# Path parameters
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Please select the ID of the student", gt=0, lt=5)):
    return students[student_id]


# Query parameters
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, ): # esteric '*' allows to use optional before required query/parameters
    for student_id in students:
        if students[student_id]["name"]== name:
            return students[student_id]
    return {"Data": "Not found"}

# Combining Path and Query parameters
@app.get("/get-by-name-new/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int): # esteric '*' allows to use optional before required query/parameters
    for student_id in students:
        if students[student_id]["name"]== name:
            return students[student_id]
    return {"Data": "Not found"}

# Request Body and The Post Method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Already Exists"}
    
    students[student_id] = student
    return students[student_id]

# Put Method - Put method is used to update something that already exists
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return{"Error": "Student does not exists"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

# Delete Method - Delete data or object from database
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exits"}
    
    del students[student_id]
    return {"Message":"Student deleted successfully"}


        

