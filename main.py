import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from databases import create_db, drop_db
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_db()
    print("БД очищена")
    await create_db()
    print("БД активирована и готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)