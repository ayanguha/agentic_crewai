from crewai.tools import BaseTool, tool
from typing import Type
from pydantic import BaseModel, Field
from urllib.request import urlopen 
from urllib.parse import urlencode
import requests
import json, datetime

class F1APISearchInput(BaseModel):
    """Input schema for Fetch F1 Details Tool."""
    query: str = Field(..., description="Search Query provided by the Agent")


def get_api_data():
        base_url = "https://api.openf1.org/v1"
        session_year = datetime.datetime.now().year
        date_end = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d") 
        session_type = "Race"
        params = [("year", session_year), ("date_end%3C", date_end), ("session_type", session_type)] 
        query_string = "&".join([f"{k}={v}" for k, v in params]) 
        url = f"{base_url}/sessions?{query_string}"
        sessions = requests.get(url, verify=False).json() 
        final_result = []
        for s in sessions:
                params = [("session_key", s['session_key']), ("position%3C", 5)]
                query_string = "&".join([f"{k}={v}" for k, v in params]) 
                url = f"{base_url}/session_result?{query_string}" 
                session_results = requests.get(url, verify=False).json() 
                for sr in session_results:
                        
                        dn = requests.get(f"{base_url}/drivers", params = { "driver_number": sr['driver_number'], "session_key": s["session_key"]}).json()
                        output_dict = {
                                'session_key': s['session_key'],
                                'date_start' : s['date_start'],
                                'date_end' : s['date_end'],
                                'circuit_short_name' : s['circuit_short_name'],
                                'country_name' : s['country_name'],
                                'position' : sr['position'],
                                'driver_name' : dn[0]['full_name']
                        }
                        final_result.append(output_dict)
        print("=================== Tool Response: ========================")
        print(final_result)
        print("===========================================================")
        return final_result 



class PastResultTool(BaseTool):
    name: str = "fetch_past_results"
    description: str = "Fetch past results for F1"
    base_url:str = "https://api.openf1.org/v1"
    args_schema: type[BaseModel] = F1APISearchInput
    def _run(self, query: str) -> str:
        session_year = datetime.datetime.now().year
        date_end = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d") 
        session_type = "Race"
        params = [("year", session_year), ("date_end%3C", date_end), ("session_type", session_type)] 
        query_string = "&".join([f"{k}={v}" for k, v in params]) 
        url = f"{self.base_url}/sessions?{query_string}"
        print(url)
        try:
                
                return get_api_data()
        except:
                raise  



if __name__ == "__main__":
        get_api_data()