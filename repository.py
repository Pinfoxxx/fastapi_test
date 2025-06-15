# Репозиторий для работы с БД

from sqlalchemy import select
from databases import new_session, TaskModel
from schemas import TaskAddSchema, TaskSchema


class TaskRepo:
    @classmethod
    async def add_task(cls, data: TaskAddSchema) -> int: # Указываем, что ф-ция помимо всего должна вернуть int
        async with new_session() as session:
            task_dict = data.model_dump() # Создаём словарик с дампом модели

            task = TaskModel(**task_dict) # Задачу раскрываем как кварги из словаря task_dict и отправляем в модель алхимии
            session.add(task) # Добавляем в сессию (не асинхронно) задачу
            await session.flush() # Отправление изменения в БД с получением id
            await session.commit() # Сохранение изменений с БД
            return task.id # Возвращаем id задачи


    @classmethod
    async def find_all(cls) -> list[TaskSchema]:
        async with new_session() as session:
            query = select(TaskModel) # Вспомогательная штука для result
            result = await session.execute(query) # Взаимодействуем с сессией через select
            task_models = result.scalars().all() # Возвращение в переменную всех задач
            task_schemas = [TaskSchema.model_validate(task_model) for task_model in task_models] # Конвертация в pydantic-схему
            return task_schemas # Возвращаем результат