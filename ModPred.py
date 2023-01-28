from pydantic import BaseModel


class ModPred(BaseModel):
    bilirubin: float
    neutrophils: float
    amylase: float
    duration: int
    lymphocytes: float