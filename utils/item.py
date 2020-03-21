from pydantic import BaseModel


class Item(BaseModel):
    clear: bool = False
    test: bool = False
    face_folder: str = None