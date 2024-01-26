import lututils as lut
import os, time

routes = lut.get_routes()

while True:
    arrivals = lut.get_arrivals()
    os.system("cls")
    for arrival in arrivals:
        print(f"{routes[arrival.route_id]} @ {arrival.stop} ({arrival.get_mins()} mins)")
    time.sleep(2)