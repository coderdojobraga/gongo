import asyncio

import aiohttp

from bot.cogs.utils.constants import translate_belt_name
from bot.settings import API_URL, BOKKEN_JWT


async def update_belt(ninja, belt):
    async with aiohttp.ClientSession() as session:
        belt = translate_belt_name(belt)
        headers = {"Authorization": "Bearer " + BOKKEN_JWT}
        data = {"ninja": {"belt": belt}}

        # Replace '#' with '%23'
        ninja = ninja.replace("#", "%23")
        url = API_URL + "api/bot/ninja/" + str(ninja)
        async with session.patch(url, json=data, headers=headers) as resp:
            return resp.status
