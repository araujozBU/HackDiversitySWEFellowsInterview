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
#Filter accessible data using linear search
accessible_routes = []  # store accessible routes

# Iterate through each route
for route in routes:
    # Check if the 'accessible' field is True
    if route.get("accessible") == True:
        accessible_routes.append(route)  # Add the route to the result list

# Print the result for verification
print("Non Sorted - Accessible Routes:", accessible_routes)

#########################################################################
# Use bubble sort to sort the distances

n = len(accessible_routes) #num entries in the accessible_routes list returned 

for i in range(0, n): #iterate through every element in the list
    for j in range(0, n-i-1): #
        if accessible_routes[j]["distance"] > accessible_routes[j+1]["distance"]: #compare the first element to the one after it 
            accessible_routes[j], accessible_routes[j+1] = accessible_routes[j+1], accessible_routes[j] #swap

#bubble sort results
print("Final List of Sorted Accessible Routes - ", accessible_routes)