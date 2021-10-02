from typing import Dict, List
from pydantic import BaseModel, Field


class ShadowFile(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]


class ShadowTask(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]
    references_at: List[str]


class ShadowStep(BaseModel):
    source_upath: str
    text_content: str
    struct_content: str
    referenced_by: List[str]
    references_at: List[str]


class WorldReflection(BaseModel):
    loaded_files:  Dict[str, ShadowFile]
    loaded_stages: Dict[str, ShadowTask]
    loaded_steps: Dict[str, ShadowStep]
    #
    # def load_text(self, text: str):
    # def load_file(self, upath: str):

