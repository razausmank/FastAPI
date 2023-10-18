from fastapi import FastAPI
from . import models
from .database import engine, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# try:
#     conn = psycopg.connect("dbname=FastApi user=postgres password=root", row_factory=dict_row)
#     cursor = conn.cursor()
#     print("database connection was succesfull ")
# except Exception as error:
#     print("connecting to database failed")
#     print("error", error)


app.include_router(post.router)
app.include_router(user.router)

@app.get('/')
def root():
    return {"message", "Hello World"}



