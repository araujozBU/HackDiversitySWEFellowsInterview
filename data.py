import requests

#######################################################################
# Send a POST request to the /api/start-session endpoint ==> session_id
def start_session(first_name, last_name):
    url = "https://hackdiversity.xyz/api/start-session"
    data = {
        "firstName": first_name,
        "lastName": last_name
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json().get("session_id")
    else:
        print("Error starting session:", response.text)
        return None


#######################################################################
# Use the session_id to retrieve the data route
def get_routes(session_id, routes_url):
    headers = {
        "Authorization": f"Bearer {session_id}"
    }

    response = requests.get(routes_url, headers=headers)
    if response.status_code == 200: 
        return response.json()  
    else:
        print("Error fetching routes:", response.text)
        return []


#######################################################################
#Filter accessible data using linear search
def filter_accessible_routes(routes):
    accessible_routes = []  # store accessible routes

    # Iterate through each route
    for route in routes:
        # Check if the 'accessible' field is True
        if route.get("accessible") == True:
            accessible_routes.append(route)  # Add the route to the result list

    # Print the result for verification
    print("Non Sorted - Accessible Routes:", accessible_routes)
    return accessible_routes

#########################################################################
# Use bubble sort to sort the distances
def bubble_sort_routes_by_distance(accessible_routes):
    n = len(accessible_routes) #num entries in the accessible_routes list returned 

    for i in range(0, n): #iterate through every element in the list
        for j in range(0, n-i-1): #
            if accessible_routes[j]["distance"] > accessible_routes[j+1]["distance"]: #compare the first element to the one after it 
                accessible_routes[j], accessible_routes[j+1] = accessible_routes[j+1], accessible_routes[j] #swap

    #bubble sort results
    print("Final List of Sorted Accessible Routes - ", accessible_routes)

#######################################################################
# Submit the sorted routes to the API
def submit_sorted_routes(session_id, sorted_routes, submit_url):
    headers = {
        "Authorization": f"Bearer {session_id}"
    }
    payload = {"routes": sorted_routes}

    # Debugging: Print payload before submission
    print("Submitting Payload:", payload)

    response = requests.post(submit_url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Submission successful:", response.json())
    else:
        print("Submission failed:", response.text)


def main():
    # Start session
    session_id = start_session("Zaki", "Araujo")
    if not session_id:
        return

    # Retrieve test routes
    url = "https://hackdiversity.xyz/api/test/mockRoutes"
    submit_url = "https://hackdiversity.xyz/api/test/submit-sorted-routes"
    all_routes = get_routes(session_id, url)

    # Filter accessible routes
    filtered_routes = filter_accessible_routes(all_routes)

    # Sort accessible routes by distance
    bubble_sort_routes_by_distance(filtered_routes)

    # Submit sorted routes and get feedback
    feedback = submit_sorted_routes(session_id, filtered_routes, submit_url)
    if feedback:
        print("Feedback from test submission:", feedback)

if __name__ == "__main__":
    main()