import pytest

from app import get_json


@pytest.mark.asyncio
async def test_get_json_success():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert "title" in result


@pytest.mark.asyncio
async def test_another_success():
    url = "http://api.zippopotam.us/us/90210"
    result = await get_json(url)
    assert "country" in result


@pytest.mark.asyncio
async def test_another_success_1():
    url = "https://official-joke-api.appspot.com/random_joke"
    result = await get_json(url)
    assert "setup" in result