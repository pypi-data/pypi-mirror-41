# aioeachlimit

Apply an async function to each item in an array or queue with limited concurrency

## Install

`pip install aioeachlimit`

## Usage

```
async def f(item):
    asyncio.sleep(3)
	return item * 2

items = [1, 2, 3, 4]

async for result in aioeachlimit(items, f, concurrency_limit=2):
	print(result)  # Prints 2 4 6 8 in random order
```

If you don't need to return anything:

```
await aioeachlimit(items, f, concurrency_limit=2, discard_results=True)
```

If `items` is an `asyncio.Queue` then aioeachlimit will read from it indefinitely.

## Tests

`pytest .`
