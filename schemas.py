from typing import Optional
from pydantic import BaseModel


class GrafanaAnnotations(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None


class GrafanaPayload(BaseModel):
    annotations: Optional[GrafanaAnnotations]
    labels: Optional[dict] = None