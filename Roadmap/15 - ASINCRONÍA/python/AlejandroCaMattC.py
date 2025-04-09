import datetime
import time
import asyncio

"""Asynchronous"""


async def synctask(name: str, duration: int):
    """Simulate a task that takes a certain amount of time to complete."""
    print(
        f"Starting task {name}. Duration: {duration}s. Start: {datetime.datetime.now()}")
    await asyncio.sleep(duration)
    print(f"Task: {name}. End: {datetime.datetime.now()}")


asyncio.run(synctask("1", 2))

"""Exercise"""


async def async_tasks():
    await asyncio.gather(synctask("C", 10), synctask("B", 7), synctask("A", 4))
    await synctask("D", 1)


asyncio.run(async_tasks())
