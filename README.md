# pixiechess-client

Unofficial Python client for the [PixieChess](https://www.pixiechess.xyz) API.

## Install

```bash
pip install pixiechess-client
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add pixiechess-client
```

Requires Python 3.13+.

## Quick start

```python
from pixiechess_client import PixieChessClient

with PixieChessClient() as client:
    user = client.users.get("username")
    print(f"{user.username_display}: {user.rating:.0f} rating, {user.wins}W-{user.losses}L")
```

## Async

```python
import asyncio
from pixiechess_client import AsyncPixieChessClient

async def main():
    async with AsyncPixieChessClient() as client:
        user = await client.users.aget("username")
        print(user.username_display)

asyncio.run(main())
```

## Resources

### Users

```python
user = client.users.get("username")           # by username
user = client.users.get("0x1234...")         # by address

history = client.users.match_history("0x1234...", limit=15, page=1)
for match in history.matches:
    print(f"{match.outcome}: {match.rating_change:+.1f}")

# auto-paginate all matches
for match in client.users.match_history_iter("0x1234..."):
    print(match.game_id)
```

### Leaderboard

```python
lb = client.leaderboard.get(page=1)
for entry in lb.entries:
    print(f"#{entry.rank} {entry.username_display} ({entry.rating:.0f})")

# auto-paginate all players
for entry in client.leaderboard.iter():
    print(entry.username_display)

# points leaderboard
pts = client.leaderboard.points(page=1)
for entry in pts.entries:
    print(f"#{entry.rank} {entry.username_display} ({entry.total_points} pts)")
```

### Games

```python
game = client.games.get("game_id_here")
rating = client.games.rating_change("game_id_here", "0x1234...")
print(f"Rated: {rating.rated}, change: {rating.change}")
```

### Pieces

```python
pieces = client.pieces.get("0x1234...", limit=10, grouped=True)
for piece in pieces.pieces:
    print(piece.metadata.name)

burned = client.pieces.burned("0x1234...", limit=10)

# auto-paginate
for piece in client.pieces.iter("0x1234..."):
    print(piece.metadata.name)
```

### Auctions

```python
active = client.auctions.active()
for auction in active:
    print(f"{auction.metadata.piece_key} - {auction.last_mint_price_in_wei} wei")

past = client.auctions.past(page=1)
info = client.auctions.piece_info("knightmare")
volume = client.auctions.daily_volume(range="7d")
prices = client.auctions.prices()
summary = client.auctions.today_summary()
```

### Tournaments

```python
tournaments = client.tournaments.list(limit=10, sort="date", date_filter="today")
for t in tournaments.tournaments:
    print(f"{t.name} - {t.prize_amount} {t.prize_currency}")

details = client.tournaments.details("tournament_id_here")
waitlist = client.tournaments.waitlist("tournament_id_here")
```

### Misc

```python
config = client.misc.config()
balance = client.misc.vault_balance()
price = client.misc.eth_usd_price()

feed = client.misc.live_feed(limit=10, type="auction_purchase,pack_purchase")
for event in feed:
    print(event["type"], event["data"])
```

## Pagination

Paginated endpoints support both manual and auto-paginating access:

```python
# manual
page1 = client.leaderboard.get(page=1)
page2 = client.leaderboard.get(page=2)

# auto-paginate (yields individual items across all pages)
for entry in client.leaderboard.iter():
    print(entry.username_display)
```

Auto-paginating iterators are available on: `leaderboard.iter()`, `leaderboard.points_iter()`, `users.match_history_iter()`, `pieces.iter()`, `pieces.burned_iter()`.

## License

MIT
