from datetime import datetime, timezone

def utc_now():
    """Возвращает текущее UTC время как naive datetime для PostgreSQL"""
    return datetime.now(timezone.utc).replace(tzinfo=None)