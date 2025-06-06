import asyncio
from queue import Queue
from typing import List
from domain.models import Quote

quote_queue: Queue[Quote] = Queue()
processed_quotes: List[Quote] = []

async def quote_worker()->None:
    while True:
        if not quote_queue.empty():
            quote = quote_queue.get()
            print(f"Quote with ID {quote.quote_id} processing....")
            await asyncio.sleep(5)
            print(f"Processed quote: {quote.quote_id}")
            processed_quotes.append(quote)
        await asyncio.sleep(0.5)
