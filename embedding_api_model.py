from pydantic import BaseModel
from typing import List

class EmbeddingInput(BaseModel):
  input: str | List[str]
  model: str

class EmbeddingData(BaseModel):
  object: str = 'embedding'
  index: int = 0
  embedding: List[float] = []

  class Config:
    arbitrary_types_allowed = True

class EmbeddingUsage(BaseModel):
  prompt_tokens:int = 0
  total_tokens:int = 0

class EmbeddingOutput(BaseModel):
  object: str = "list"
  data: List[EmbeddingData] = []
  model: str = 'BGE-3M'
  usage: EmbeddingUsage = None

  class Config:
    arbitrary_types_allowed = True
