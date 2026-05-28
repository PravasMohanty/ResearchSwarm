from pydantic import BaseModel
from typing import List
from datetime import datetime

class Finding(BaseModel):
    claim: str
    evidence: List[str]
    sources: List[str]
    confidence: float

class ReportSection(BaseModel):
    title: str
    content: str
    findings: List[Finding]
    confidence: float

class ResearchReport(BaseModel):
    title: str
    description: str
    executive_summary: str
    sections: List[ReportSection]
    sources: List[str]
    generated_at: datetime = datetime.utcnow()