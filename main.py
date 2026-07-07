from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI assignment"
    }

@app.get("/about")
def about():
    return {
            "student_name": "Suksham Raina",
            "course": "FastAPI",
            "topic": "First API Assignment",
            "status": "Learning"
        }
    
@app.get("/trainer")
def trainer():
    return {
        "name": "Hemanth",
        "role": "Trainer",
        "subject": "FastAPI"
    }

@app.get("/courses")
def courses():
    return{
        "courses": [
            { 
                "id": 1, 
                "name": "Python Basics", 
                "duration": "1 week" 
            },
            { 
                "id": 2, 
                "name": "FastAPI", 
                "duration": "2 weeks" 
            },
            { 
                "id": 3, 
                "name": "SQL Basics", 
                "duration": "1 week" 
            }
        ]
    }

@app.get("/students")
def students():
    return {
        "students": [
            { 
                "id": 1, 
                "name": "Akhil", 
                "course": "Python", 
                "city": "Hyderabad" 
            },
            { 
                "id": 2, 
                "name": "Sai", 
                "course": "FastAPI", 
                "city": "Vijayawada" 
            }
        ]
    }

@app.get("/college")
def college():
    return {
        "college_name": "Model Institute of Engineering and Technology",
        "location": "Jammu",
        "department": "Computer Science-AIML",
        "current_module": "FastAPI Basics"
    }

@app.get("/technologies")
def technologies():
    return[
            "Python",
            "FastAPI",
            "JSON",
            "HTTP",
            "REST API"
        ]
    
# @app.get("/students/{student_id}")
# def get_student_by_id(student_id:int):
#     return{
#         "student_id":student_id,
#         "message":"learning Dynamic URL's"
#     }

# courses=["Python Basics","FastAPI","SQL Basics","Java"]

# @app.get("/courses/{course_id}")
# def get_course_by_id(course_id:str):
#     for course in courses:
#         if course == course_id:
#             return{
#                 "course_id":course_id,
#                 "message":"This is Dynamic URL for course"
#             }
#     return{
#         "message":"Course not found"
#     }

# @app.get("/books/{book_id}/author/{author_id}")
# def get_book_and_author_by_id(book_id:int,author_id:int):
#     return{
#         "book_id":book_id,
#         "Book Name":"One Piece",
#         "author_id":author_id,
#         "Author Name":"Eichira Oda",
#         "message":"Thank you for visiting"
#     }

# @app.get("/students/{student_id}/courses/{course_id}")
# def get_student_and_course_by_id(student_id:int,course_id):
#     return {
#         "Student id":student_id,
#         "Student Name":"Suksham Raina",
#         "Course id":course_id,
#         "Course Name":"Fast API"
#     }