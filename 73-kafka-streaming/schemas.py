from pydantic import BaseModel
from typing import Optional


class AnalyticsEvent(BaseModel):
    event_type: str          # "page_view", "click", "purchase"
    user_id: Optional[int] = None
    page: Optional[str] = None
    element: Optional[str] = None
    product: Optional[str] = None
    amount: Optional[float] = None
    timestamp: str


class MetricsSnapshot(BaseModel):
    page_views: int = 0
    clicks: int = 0
    purchases: int = 0
    total_revenue: float = 0.0
    events_per_second: float = 0.0
