
shoe = {
    "brand": "Nike",
    "wide": False,
    "color": "Black",
    "shoe_size": 12,
    "string_color" : ["orange", "blue", "purple"]
}

print(shoe["shoe_size"])

x = shoe["brand"]
print(x)

x = shoe.keys()

print(x)

shoe["tongue_color"] = "black"

print(x)

chaddict = {
    "brand": "Indian",
    "model": "Scout",
    "year": 2003
    }
print(f"The {chaddict['year']} {chaddict['brand']} {chaddict['model']} would be a perfect fit for your collection")  

placedict = {
    "state": "Texas",
    "city": "Austin",
    "road": "Interstate 4"
    }
print(f"Think of how it would feel to own a bike like that in {placedict['city']} {placedict['state']} gliding down {placedict['road']}!")

print(f"I'd love to cruise around {placedict['city']} on a {chaddict['model']}! Seeing the sights from {placedict['road']} while riding a {chaddict['brand']} through {placedict['state']} would be awesome!!")
