from fastapi import FastAPI

from routers import company

from routers import job
from database import engine,Base
Base.metadata.create_all(bind=engine)

app= FastAPI()
print("engine is",engine)
app.include_router(company.router)
app.include_router(job.router)

@app.get("/")
def read_root():
    return{"Hello":"World"}
@app.get("/about")
def read_root():
    return{"about":"This is about page"}
@app.get("/contact")
def read_root():
    return{"contact":"This is contact page"}