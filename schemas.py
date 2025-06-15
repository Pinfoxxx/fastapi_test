from typing import Optional
from pydantic import BaseModel, ConfigDict


class TaskAddSchema(BaseModel):
    name: str
    description: Optional[str] = None # Не всегда python определяет конструкцию str | None, поэтому лучше писать именно через модуль Optional


class TaskSchema(TaskAddSchema):
    id: int

    model_config = ConfigDict(from_attributes=True)


# Валидация данных / пример выводимых данных для ручки post
class TaskIdSchema(BaseModel):
    ok: bool = True
    task_id: int