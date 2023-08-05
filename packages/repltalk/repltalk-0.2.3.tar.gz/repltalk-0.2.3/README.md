# Repl Talk
This package is an asynchronous wrapper for the (very unofficial) Repl.it api for Repl Talk

Here's some stuff

```py
import repltalk
import asyncio
client = repltalk.Client()

async def main():
	print('Leaderboards:')
	async for u in client.get_leaderboard():
		print(f'{u.username} ({u.cycles})')
	print('\nPosts:')
	for p in await client.boards.all.get_posts():
		print(p.title)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
more documentation coming soon™