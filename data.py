import requests

#######################################################################
# Send a POST request to the /api/start-session endpoint ==> session_id
url = "https://hackdiversity.xyz/api/start-session"
data = {
    "firstName": "Zaki",
    "lastName": "Araujo"
}

response = requests.post(url, json=data)
if response.status_code == 200:
    session_id = response.json().get("session_id")
else:
    print("Error:", response.text)


#######################################################################
# Use the session_id to retrieve the data route
headers = {
    "Authorization": f"Bearer {session_id}"
}
routes_url = "https://hackdiversity.xyz/api/navigation/routes"

response = requests.get(routes_url, headers=headers)
if response.status_code == 200: 
    routes = response.json()  
else:
    print("Error fetching routes:", response.text)


#######################################################################
#Fucntion to check if the data is accessible using linear search
def filter_accessible_routes(routes):
    
    accessible_routes = []  # List to store accessible routes

    # Iterate through each route
    for route in routes:
        # Check if the 'accessible' field is True
        if route.get("accessible") == True:
            accessible_routes.append(route)  # Add the route to the result list

    return accessible_routes  # Return the filtered list

accessible_routes = filter_accessible_routes(routes)

# Print the result for verification
print("Accessible Routes:", accessible_routes)