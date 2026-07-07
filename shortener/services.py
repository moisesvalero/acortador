import hashlib

from django.conf import settings
from django.core.cache import cache

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
CODE_LENGTH = 6
ID_OFFSET = 10_000
CACHE_TIMEOUT = 600  # 10 minutos
RATE_LIMIT_WINDOW = 60  # 1 minuto
RATE_LIMIT_MAX = 10


def base62_encode(num: int) -> str:
    if num == 0:
        return BASE62[0]
    chars = []
    while num > 0:
        num, rem = divmod(num, 62)
        chars.append(BASE62[rem])
    return "".join(reversed(chars))


def generate_short_code(link_id: int) -> str:
    encoded = base62_encode(link_id + ID_OFFSET)
    return encoded.rjust(CODE_LENGTH, BASE62[0])


def get_cached_link(code: str) -> str | None:
    return cache.get(f"link:{code}")


def set_cached_link(code: str, url: str) -> None:
    cache.set(f"link:{code}", url, CACHE_TIMEOUT)


def invalidate_link_cache(code: str) -> None:
    cache.delete(f"link:{code}")


def hash_ip(ip: str) -> str:
    salt = settings.IP_HASH_SALT
    return hashlib.sha256(f"{ip}{salt}".encode()).hexdigest()


def is_rate_limited(ip_hashed: str) -> bool:
    cache_key = f"rl:{ip_hashed}"
    count = cache.get(cache_key, 0)
    if count >= RATE_LIMIT_MAX:
        return True
    cache.set(cache_key, count + 1, RATE_LIMIT_WINDOW)
    return False
