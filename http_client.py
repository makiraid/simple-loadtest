import aiohttp
import asyncio
from datetime import datetime

class HTTPClient:
    def __init__(self, url, headers=None, body=None):
        self.url = url
        self.headers = headers
        self.body = body

    async def fetch(self, session):
        try:
            async with session.request('POST', self.url, headers=self.headers, json=self.body) as response:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
                results = await response.json()

                if response.status == 200:
                    print(f"[{timestamp}] Success: {results}")
                    return results
                else:
                    print(f"[{timestamp}] Error: {results}")
                    return {"error": f"Error: {results}"}
        except Exception as e:
            return {"error": str(e)}

async def run_load_test(http_client, count):
    async with aiohttp.ClientSession() as session:
        tasks = [http_client.fetch(session) for _ in range(count)]
        return await asyncio.gather(*tasks)
