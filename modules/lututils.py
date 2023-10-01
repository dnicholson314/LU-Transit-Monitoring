import requests
from arrival import Arrival
from time import sleep
from os import system

# Hardcoded to all API requests, will fail if not included
API_KEY = 8882812681

def get_routes() -> dict[str, int]:
    url = "https://liberty.ridesystems.net/Services/JSONPRelay.svc/GetRoutesForMapWithScheduleWithEncodedLine"
    params = {
        "apiKey": API_KEY,
        "isDispatch": False
    }
    response = requests.get(url=url, params=params)
    payload = response.json()

    routes = {}
    for item in payload:
        name = item["Description"]
        id = item["RouteID"]

        # Filter out the one route that doesn't have any vehicles.
        if "Not in Service" in name:
            continue
        
        routes[id] = name

    return routes

def get_vehicle_ids(as_str = True):
    url = "https://liberty.ridesystems.net/Services/JSONPRelay.svc/GetMapVehiclePoints"
    params = {
        "apiKey": API_KEY, 
    }
    response = requests.get(url=url, params=params)
    payload = response.json()
    vehicle_ids = []

    for item in payload:
        id = item["VehicleID"]
        if as_str:
            id = str(id)
        vehicle_ids.append(id)

    return vehicle_ids

def get_arrivals(vehicle_ids = get_vehicle_ids()):
    url = "https://liberty.ridesystems.net/Services/JSONPRelay.svc/GetStopArrivalTimes"
    str_ids = [str(id) for id in vehicle_ids]
    params = {
        "apiKey": API_KEY,
        "vehicleIdStrings": ",".join(str_ids),
        "quantity": 3
    }
    response = requests.get(url=url, params=params)
    payload = response.json()
    arrivals = []

    for item in payload:
        route_id = item["RouteId"]
        vehicle_id = item["Times"][0]["VehicleId"]
        seconds = item["Times"][0]["Seconds"]
        stop = item["StopDescription"]

        # The API returns some estimates that aren't connected to a vehicle;
        # here, we filter those estimates out.
        if vehicle_id == None:
            continue

        arrivals.append(Arrival(route_id, vehicle_id, stop, seconds))

    return arrivals
