from .start import start_router
from .health import health_router
from .calendar import calendar_router

routers = [
    start_router,
    health_router,
    calendar_router
]
