from typing import Any, List, Optional

from gbc_model.processing.validation import SBAInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: List[float]


class MultipleSBAInputs(BaseModel):
    inputs: List[SBAInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "City": "Alvin",
                        "Zip": 77512,
                        "Bank": "LOANS FROM OLD CLOSED LENDERS",
                        "NAICS": 0,
                        "ApprovalFY": "1996",
                        "Term": 180,
                        "NoEmp": 60,
                        "NewExist": 1.0,
                        "CreateJob": 0,
                        "RetainedJob": 0,
                        "UrbanRural": 0,
                        "RevLineCr": "0",
                        "LowDoc": "N",
                        "DisbursementGross": "$2,500,000.00",
                        "GrAppv": "$2,500,000.00",
                        "SBA_Appv": "$750,000.00",
                    }
                ]
            }
        }
