import modules.lututils as lut

routes = lut.get_routes()

while True:
    arrivals = lut.get_arrivals()
    lut.system("cls")
    for arrival in arrivals:
        print(f"{routes[arrival.route_id]} @ {arrival.stop} ({arrival.get_mins()} mins)")
    lut.sleep(2)