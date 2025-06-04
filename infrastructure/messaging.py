import asyncio
from queue import Queue

quote_queue = Queue()
processed_quotes = []

async def quote_worker():
    while True:
        if not quote_queue.empty():
            quote = quote_queue.get()
            print(f"Quote with ID {quote.quote_id} processing....")
            await asyncio.sleep(5)
            print(f"Processed quote: {quote.quote_id}")
            processed_quotes.append(quote)
        await asyncio.sleep(0.5)
