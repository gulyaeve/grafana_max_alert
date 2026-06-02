# from datetime import datetime
# from typing import List

from pydantic import BaseModel


# class GrafanaAlert(BaseModel):
#     status: str
#     labels: dict
#     annotations: dict
#     startsAt: datetime
#     endsAt: datetime
#     generatorURL: str
#     fingerprint: str
#     silenceURL: str
#     panelURL: str
#     values: dict
#     valueString: list
#     orgId: int



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

    def __str__(self):
        result = ""
        for alert in self.alerts:
            result += "\n".join(f"{k}: {v}" for k, v in alert["labels"].items())
            result += "\n\n"
        return result

"""
receiver='webhook'
status='firing'
alerts=[{'status': 'firing', 'labels': {'alertname': 'TestAlert', 'grafana_folder': 'Test Folder', 'instance': 'Grafana'}, 'annotations': {'summary': 'Notification test'}, 'startsAt': '2026-06-02T10:43:15.186159734+03:00', 'endsAt': '0001-01-01T00:00:00Z', 'generatorURL': '?orgId=1', 'fingerprint': '326ea703b01f6100', 'silenceURL': 'http://zabbix.itmoscow/grafana/alerting/silence/new?alertmanager=grafana&matcher=alertname%3DTestAlert&matcher=grafana_folder%3DTest+Folder&matcher=instance%3DGrafana&orgId=1', 'dashboardURL': 'http://zabbix.itmoscow/grafana/d/dashboard_uid?from=1780382595186&orgId=1&to=1780386195188', 'panelURL': 'http://zabbix.itmoscow/grafana/d/dashboard_uid?from=1780382595186&orgId=1&to=1780386195188&viewPanel=1', 'values': {'B': 22, 'C': 1}, 'valueString': "[ var='B' labels={__name__=go_threads, instance=host.docker.internal:3000, job=grafana} type='reduce' value=22 ], [ var='C' labels={__name__=go_threads, instance=host.docker.internal:3000, job=grafana} type='threshold' value=1 ]", 'orgId': 1}]
groupLabels={'alertname': 'TestAlert', 'grafana_folder': 'Test Folder', 'instance': 'Grafana'}
commonLabels={'alertname': 'TestAlert', 'grafana_folder': 'Test Folder', 'instance': 'Grafana'}
commonAnnotations={'summary': 'Notification test'}
externalURL='http://zabbix.itmoscow/grafana/'
groupKey='webhook-326ea703b01f6100-1780386195'
truncatedAlerts=0
"""