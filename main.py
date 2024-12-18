from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import delete_tables, create_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('bd cleared')
    await create_tables()
    print('bd created')
    yield
    print('off')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

tasks = []
