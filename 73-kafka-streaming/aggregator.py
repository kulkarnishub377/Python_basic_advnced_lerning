import time
import threading

# Thread-safe in-memory metrics store
_lock = threading.Lock()
_metrics = {
    "page_views": 0,
    "clicks": 0,
    "purchases": 0,
    "total_revenue": 0.0,
    "total_events": 0,
    "start_time": time.time(),
}


def record_event(event_type: str, amount: float = 0.0):
    """Thread-safe metric recording."""
    with _lock:
        _metrics["total_events"] += 1
        if event_type == "page_view":
            _metrics["page_views"] += 1
        elif event_type == "click":
            _metrics["clicks"] += 1
        elif event_type == "purchase":
            _metrics["purchases"] += 1
            _metrics["total_revenue"] += amount


def get_metrics() -> dict:
    """Return a snapshot of current metrics."""
    with _lock:
        elapsed = max(time.time() - _metrics["start_time"], 1)
        return {
            "page_views": _metrics["page_views"],
            "clicks": _metrics["clicks"],
            "purchases": _metrics["purchases"],
            "total_revenue": round(_metrics["total_revenue"], 2),
            "events_per_second": round(_metrics["total_events"] / elapsed, 1),
        }
