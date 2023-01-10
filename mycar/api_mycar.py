import asyncio
import aiohttp

import config

class MycarAPI:
    def __init__(self, regnum, owner):
        self.regnum = regnum
        self.owner = owner
    
    def get_headers(self):
        return {"Authorization": config.env["auth_key"], "Content-Type": "application/json"}

    def get_unit_apis(self):
        return [
            {
                "url": f"{config.env['auth_key']}/assist/eCar/CarRegiste",
                "req_data": {"TASK": "0", "REGINUMBER": f"{self.regnum}", "OWNERNAME": f"{self.owner}", "CARREGIOPEN": "0"} 
            },
            {
                "url": f"{config.env['auth_key']}/scrap/common/car/RecallTargetVerification",
                "req_data": {"CARNUMBER": f"{self.regnum}"} 
            },
            {
                "url": f"{config.env['auth_key']}/assist/common/carzen/CarAllInfoInquiry",
                "req_data": {"REGINUMBER": f"{self.regnum}", "OWNERNAME": f"{self.owner}"} 
            }
        ]

    async def call_apis(self):
        async with aiohttp.ClientSession(headers=self.get_headers()) as session:          
            return await asyncio.gather(*[self.fetch(session, api) for api in self.get_unit_apis()])

    async def fetch(self, session, api):
        async with session.post(api["url"], json=api["req_data"]) as response:
            resp_data = await response.json()
            resp_data["api_url"] = str(response.url).split("/")[-1]
            return resp_data
