"""
Redis Client Configuration
"""
import redis.asyncio as redis
from typing import Optional
import json

from app.core.config import settings


class RedisClient:
    """Redis client wrapper for caching and session management"""
    
    def __init__(self):
        self.redis: Optional[redis.Redis] = None
    
    async def initialize(self):
        """Initialize Redis connection"""
        self.redis = await redis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
    
    async def close(self):
        """Close Redis connection"""
        if self.redis:
            await self.redis.close()
    
    async def get(self, key: str) -> Optional[str]:
        """Get value from Redis"""
        if not self.redis:
            return None
        return await self.redis.get(key)
    
    async def set(
        self,
        key: str,
        value: str,
        expire: Optional[int] = None
    ) -> bool:
        """Set value in Redis with optional expiration"""
        if not self.redis:
            return False
        return await self.redis.set(key, value, ex=expire)
    
    async def delete(self, key: str) -> bool:
        """Delete key from Redis"""
        if not self.redis:
            return False
        return await self.redis.delete(key) > 0
    
    async def exists(self, key: str) -> bool:
        """Check if key exists in Redis"""
        if not self.redis:
            return False
        return await self.redis.exists(key) > 0
    
    async def get_json(self, key: str) -> Optional[dict]:
        """Get JSON value from Redis"""
        value = await self.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return None
        return None
    
    async def set_json(
        self,
        key: str,
        value: dict,
        expire: Optional[int] = None
    ) -> bool:
        """Set JSON value in Redis"""
        try:
            json_str = json.dumps(value)
            return await self.set(key, json_str, expire)
        except (TypeError, json.JSONEncodeError):
            return False
    
    async def increment(self, key: str) -> int:
        """Increment value in Redis"""
        if not self.redis:
            return 0
        return await self.redis.incr(key)
    
    async def decrement(self, key: str) -> int:
        """Decrement value in Redis"""
        if not self.redis:
            return 0
        return await self.redis.decr(key)


# Create global Redis client instance
redis_client = RedisClient()
