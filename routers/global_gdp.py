import requests
from fastapi import FastAPI, Query
import requests

app = FastAPI()


@app.get("/data")
async def get_imf_data():
    url = "https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from IMF API"}


@app.get("/data/country")
async def get_imf_data(country: str = Query(..., description="Country code")):
    url = f"https://www.imf.org/external/datamapper/api/v1/NGDP_RPCH?country={country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from IMF API"}


