from requests import Session

class GamerPower:
    def __init__(self) -> None:
        self.api = "https://www.gamerpower.com/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }

    def _get(self, endpoint: str, params: dict = None) -> dict:
        return self.session.get(
            f"{self.api}{endpoint}", params=params).json()

    def get_giveaways(self) -> dict:
        return self._get("/giveaways")

    def get_giveaways_by_platform(
            self, platform: str = "pc") -> dict:
        return self._get(f"/giveaways?platform={platform}")

    def get_giveaways_by_type(
            self, giveaway_type: str = "game") -> dict:
        return self._get(f"/giveaways?type={giveaway_type}")

    def sort_giveaways(self, sort: str) -> dict:
        return self._get(f"/giveaways?sort-by={sort}")

    def get_giveaways_by_all(
            self,
            platform: str = "steam",
            giveaway_type: str = "loot",
            sort: str = "popularity") -> dict:
        return self._get(
            f"/giveaways?platform={platform}&type={giveaway_type}&sort-by={sort}")

    def get_giveaway_details(self, giveaway_id: int) -> dict:
        return self._get(f"/giveaway?id={giveaway_id}")

    def filter_giveaway(
            self,
            platform: str = "epic-games-store.steam.android",
            giveaway_type: str = "game.loot") -> dict:
        return self._get(
            f"/filter?platform={platform}&type={giveaway_type}")

    def get_total_giveaways_worth(self) -> dict:
        return self._get("/worth")
