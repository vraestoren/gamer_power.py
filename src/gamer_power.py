from requests import Session

class GamerPower:
    def __init__(self) -> None:
        self.api = "https://www.gamerpower.com/api"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
        }
    
    def get_giveaways(self) -> dict:
        return self.session.get(
            f"{self.api}/giveaways").json()
    
    def get_giveaways_by_platform(
            self,
            platform: str = "pc") -> dict:
        return self.session.get(
            f"{self.api}/giveaways?platform={platform}").json()
    
    def get_giveaways_by_type(self, type: str = "game") -> dict:
        return self.session.get(
            f"{self.api}/giveaways?type={type}").json()
    
    def sort_giveaways(self, sort: str) -> dict:
        return self.session.get(
            f"{self.api}/giveaways?sort-by={sort}").json()
    
    def get_giveaways_by_all(
            self,
            platform: str = "steam",
            type: str = "loot",
            sort: str = "popularity") -> dict:
        return self.session.get(
            f"{self.api}/giveaways?platform={platform}&type={type}&sort-by={sort}").json()
        
    def get_giveaway_details(self, giveaway_id: int) -> dict:
        return self.session.get(
            f"{self.api}/giveaway?id={giveaway_id}").json()
    
    def filter_giveaway(
            self,
            platform: str = "epic-games-store.steam.android",
            type: str = "game.loot") -> dict:
        return self.session.get(
            f"{self.api}/filter?platform={platform}&type={type}").json()
    
    def get_total_giveaways_worth(self) -> dict:
        return self.session.get(f"{self.api}/worth").json()
