import lut.lututils as lut
import os, time

routes = lut.get_routes()

while True:
    arrivals = lut.get_arrivals()
    arrivals.sort(key=(lambda a: routes[a.route_id]))

    os.system("cls")
    print()
    for arrival in arrivals:
        print(f"{routes[arrival.route_id]} @ {arrival.stop} ({arrival.get_mins()} mins)")
    time.sleep(2)