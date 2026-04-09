from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    is_done: bool = False

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        return cls(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            is_done=data.get('is_done', False),
        )