from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data for ice cream shops
ice_cream_shops_data = {
    "Paris": ["Gelato Paradiso", "Ben & Jerry's", "Cold Stone Creamery"],
    "London": ["Scoop", "Yorica!", "Amorino"],
    "New York": ["Van Leeuwen", "Big Gay Ice Cream", "Ample Hills Creamery"],
    "Tokyo": ["Sulbing", "Grom", "Marble Slab Creamery"],
    "Mumbai": ["Natural Ice Cream", "Bachelors", "Amul"]
}

# Sample data for hotels
hotels_data = {
    "Paris": ["Marriott", "Hilton", "Holiday Inn"],
    "London": ["InterContinental", "The Ritz", "Park Plaza"],
    "New York": ["Hilton", "Marriott", "Sheraton"],
    "Tokyo": ["Park Hyatt", "Hilton", "Mandarin Oriental"],
    "Mumbai": ["Taj Mahal Palace", "The Oberoi", "ITC Grand Central"]
}

# Sample data for wheelchair locations
wheelchair_locations_data = {
    "Paris": ["Louvre Museum", "Eiffel Tower", "Champs-Élysées"],
    "London": ["British Museum", "London Eye", "Tower of London"],
    "New York": ["Central Park", "Times Square", "Empire State Building"],
    "Tokyo": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing"],
    "Mumbai": ["Gateway of India", "Siddhivinayak Temple", "Juhu Beach"]
}

# Sample data for activities
activities_data = {
    "Paris": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
    "London": ["Big Ben", "British Museum", "London Eye"],
    "New York": ["Statue of Liberty", "Broadway Shows", "Central Park Zoo"],
    "Tokyo": ["Tokyo Disneyland", "Akihabara", "Harajuku"],
    "Mumbai": ["Marine Drive", "Elephanta Caves", "Haji Ali Dargah"]
}

# Sample data for weather
weather_data = {
    "Paris": "Sunny",
    "London": "Cloudy",
    "New York": "Partly Cloudy",
    "Tokyo": "Rainy",
    "Mumbai": "Humid"
}

# Sample data for parking locations
parking_data = {
    "Paris": ["Parking A", "Parking B", "Parking C"],
    "London": ["Parking X", "Parking Y", "Parking Z"],
    "New York": ["Parking 1", "Parking 2", "Parking 3"],
    "Tokyo": ["Parking Alpha", "Parking Beta", "Parking Gamma"],
    "Mumbai": ["Parking East", "Parking West", "Parking North"]
}

@app.route('/icecream/<destination>', methods=['GET'])
def get_icecream(destination):
    icecream_shops = ice_cream_shops_data.get(destination, [])
    return jsonify({"ice_cream_shops": icecream_shops})

@app.route('/hotels/<destination>', methods=['GET'])
def get_hotels(destination):
    hotels = hotels_data.get(destination, [])
    return jsonify({"hotels": hotels})

@app.route('/wheelchair/<destination>', methods=['GET'])
def get_wheelchair_locations(destination):
    wheelchair_locations = wheelchair_locations_data.get(destination, [])
    return jsonify({"wheelchair_locations": wheelchair_locations})

@app.route('/activities/<destination>', methods=['GET'])
def get_activities(destination):
    activities = activities_data.get(destination, [])
    return jsonify({"activities": activities})

@app.route('/weather/<destination>', methods=['GET'])
def get_weather(destination):
    weather = weather_data.get(destination, "Weather information not available")
    return jsonify({"weather": weather})

@app.route('/parking/<destination>', methods=['GET'])
def get_parking(destination):
    parking = parking_data.get(destination, [])
    return jsonify({"parking": parking})

if __name__ == '__main__':
    app.run(debug=True)
