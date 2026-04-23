import hashlib
import time


def timestamp() -> int:
    return int(time.time())


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def paginate(items: list, page: int, per_page: int) -> list:
    start = (page - 1) * per_page
    return items[start : start + per_page]
