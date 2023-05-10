#!/usr/bin/env python3
"""
Tasks in redis python
"""


import redis
import uuid
from functools import wraps
from typing import Union, Callable, TypeVar

T = TypeVar('T')

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a generated key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], T] = None) -> Union[T, bytes]:
        """
        Retrieve the data associated with the given key from Redis.
        If a conversion function (fn) is provided, apply it to the retrieved data before returning.
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes]:
        """
        Retrieve the data associated with the given key from Redis as a string.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, bytes]:
        """
        Retrieve the data associated with the given key from Redis as an integer.
        """
        return self.get(key, fn=int)

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called and store the count in Redis.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__  # Use the qualified name of the method as the key
            self._redis.incr(key)  # Increment the count for the key
            return method(self, *args, **kwargs)  # Call the original method and return its result
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a method in Redis.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            input_key = f"{method.__qualname__}:inputs"  # Create the input list key
            output_key = f"{method.__qualname__}:outputs"  # Create the output list key

            # Store the input arguments as a string in the input list
            self._redis.rpush(input_key, str(args))

            # Call the original method and retrieve the output
            output = method(self, *args, **kwargs)

            # Store the output in the output list
            self._redis.rpush(output_key, output)

            return output

        return wrapper

