import pytest
import aiohttp
import asyncio
import threading

async def sum_values(x, y):
    await asyncio.sleep(3)
    return x + y

@pytest.mark.asyncio
async def test_sum_values_resolved(event_loop):
    result = await sum_values(10, 20)
    assert result == 30

async def sum_values(x, y):
    await asyncio.sleep(3)
    return x + y

@pytest.mark.asyncio
async def test_sum_values_resolved(event_loop):
    result = await sum_values(10, 20)
    assert result == 30

async def fetch_number_fact(number):
    url = f"http://numbersapi.com/{number}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response.status

@pytest.mark.asyncio
async def test_fetch_number_fact(event_loop):
    status = await fetch_number_fact(42)
    assert status == 200


async def add_to_database(data):
    await asyncio.sleep(3)
    return True

@pytest.mark.asyncio
async def test_add_to_database(event_loop):
    success = await add_to_database({"id": 1, "name": "John"})
    assert success

def run_in_thread(func, *args):
    loop = asyncio.new_event_loop()
    result = None

    def run():
        nonlocal result
        result = loop.run_until_complete(func(*args))
        loop.stop()

    thread = threading.Thread(target=run)
    thread.start()
    thread.join()

    return result

async def compute_sum(x, y):
    await asyncio.sleep(3)
    return x + y

@pytest.mark.asyncio
async def test_run_in_thread(event_loop):
    result = run_in_thread(compute_sum, 5, 10)
    assert result == 15