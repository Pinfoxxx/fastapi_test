import uvicorn
from typing import Annotated
from fastapi import FastAPI, Depends
from schemas import TaskAddSchema
from contextlib import asynccontextmanager # Либа для создания контекстных менеджеров
from databases import create_db, drop_db # Импорт для жизненного цикла
from router import router as tasks_router

# Ф-ция жизненного цикла fastapi
@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_db()
    print("БД сброшена")
    await create_db()
    print("БД создана и готова к работе")
    yield
    print("Отключение сервера")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)