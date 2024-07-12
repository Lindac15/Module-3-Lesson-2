# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary.               
# The function should return a string formatted like this: "Itenerary 1: Alice - New York to London    
# Itinerary 2: Bob - From Tokyo to San Francisco"    

def itinerary_string(itineraries):
    output = ""
    for i, itinerary in enumerate(itineraries):
        output += f"Itenerary {i + 1}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}\n"
    return output

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(itinerary_string(itineraries)) 




