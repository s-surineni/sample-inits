import asyncio
import aiohttp
import time


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(download_site(session, url)) for url in sites
        ]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    asyncio.run(download_all_sites(sites))
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
