from fastapi import FastAPI

from app.routers import user, auth, project, task

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(project.router)
app.include_router(task.router)

@app.get("/")
def read_root():
    return {"status": "API rodando com sucesso!"}