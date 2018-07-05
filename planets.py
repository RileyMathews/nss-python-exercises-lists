planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranas", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("pluto")
del(planet_list[8])
print(planet_list)

rocky_planets = planet_list[0:4]
print(rocky_planets)

spacecraft_list = [('Voyager', 'Saturn'), ('Cassini', 'Saturn'), ('Rover', 'Mars'), ('Falcon', 'Earth'), ('Enterprise', 'Mercury')]
print(spacecraft_list)

for planet in planet_list:
    for spacecraft in spacecraft_list:
        if spacecraft[1] == planet:
            print( f"{planet} has been visited by {spacecraft[0]}")