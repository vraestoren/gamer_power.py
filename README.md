# <img src="https://www.gamerpower.com/favicon/apple-touch-icon.png" width="28" style="vertical-align:middle;" /> gamer_power.py

> Web-API for [GamerPower](https://www.gamerpower.com) find free games, DLC, loot, and giveaways across PC, console, and mobile platforms.

## Quick Start
```python
from gamer_power import GamerPower

gp = GamerPower()

# Get all active giveaways
giveaways = gp.get_giveaways()
print(giveaways)
```

---

## Methods

| Method | Description |
|--------|-------------|
| `get_giveaways()` | Get all active giveaways |
| `get_giveaways_by_platform(platform)` | Filter giveaways by platform |
| `get_giveaways_by_type(giveaway_type)` | Filter giveaways by type |
| `sort_giveaways(sort)` | Get giveaways sorted by a field |
| `get_giveaways_by_all(platform, giveaway_type, sort)` | Filter and sort in one call |
| `get_giveaway_details(giveaway_id)` | Get details for a specific giveaway |
| `filter_giveaway(platform, giveaway_type)` | Filter by multiple platforms and types |
| `get_total_giveaways_worth()` | Get total estimated worth of all giveaways |

---

## Reference

**Platforms:** `pc`, `steam`, `epic-games-store`, `ubisoft`, `gog`, `itch.io`, `ps4`, `ps5`, `xbox-one`, `xbox-series-xs`, `switch`, `android`, `ios`, `vr`, `battlenet`, `origin`, `drm-free`, `xbox-360`

**Types:** `game`, `loot`, `beta`

**Sort options:** `date`, `value`, `popularity`

---

## Examples
```python
gp = GamerPower()

# Filter by platform
gp.get_giveaways_by_platform(platform="steam")

# Filter by type
gp.get_giveaways_by_type(giveaway_type="loot")

# Filter and sort together
gp.get_giveaways_by_all(
    platform="steam",
    giveaway_type="game",
    sort="popularity"
)

# Filter multiple platforms and types at once
gp.filter_giveaway(
    platform="epic-games-store.steam",
    giveaway_type="game.loot"
)

# Get details for a specific giveaway
gp.get_giveaway_details(giveaway_id=525)

# Get total worth of all active giveaways
print(gp.get_total_giveaways_worth())
```
