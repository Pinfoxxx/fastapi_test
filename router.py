from fastapi import APIRouter, Depends
from typing import Annotated
from schemas import TaskAddSchema, TaskIdSchema, TaskSchema
from repository import TaskRepo

router = APIRouter(
    prefix="/tasks", # С помощью префикса можно пометить, что у всех ручек будет один и тот же путь
    tags=["Tasks"]
)

tasks = []


@router.post("")
async def add_task(
    task: Annotated[TaskAddSchema, Depends()], # Благодаря этой штуковине у нас образуются поля ввода
)-> TaskIdSchema: # IDE обычно ругается на тот момент, когда мы сюда пихаем схему, а не словарь, но это нормально
    task_id = await TaskRepo.add_task(task) # Теперь с помощью класса TaskRepo можно добавлять задачу одной строкой
    return {"success": True, "task_id": task_id} # type: ignore


@router.get("")
async def get_tasks() -> list[TaskSchema]:
    tasks = await TaskRepo.find_all() # Используем метод find_all из класса TaskRepo
    return tasks # Возвращаем список задач