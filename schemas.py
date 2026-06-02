from pydantic import BaseModel


class GrafanaPayload(BaseModel):
    receiver: str
    status: str

    alerts: list
    groupLabels: dict

    commonLabels: dict

    commonAnnotations: dict
    externalURL: str
    groupKey: str
    truncatedAlerts: int