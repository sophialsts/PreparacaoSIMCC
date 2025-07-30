from pydantic import BaseModel, Field
from typing import Optional

class Producao(BaseModel):
    producoes_id: str = Field(..., min_length=36, max_length=36)
    pesquisadores_id: Optional[str] = Field(None, min_length=36, max_length=36)
    issn: str = Field(..., min_lenght=8, max_lenght=8)
    nomeartigo: str = Field(..., min_lenght=5, max_lenght=400)
    anoartigo: int = Field(...)
    
    