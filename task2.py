"""
visit the url https://www.openbrewerydb.org/ write a python script which will do the following:
1) List the names of all breweires present in the states of Alaska,Maine and New York
2) What is the count of breweries in each of the states mentioned above
3) Count the number of types of breweries present in individual cities of the states mentioned above
4) Count and list how many breweries have websites in the states of Alaska,Maine aand New York
"""

import requests  # Importing the requests library for making HTTP requests.

class Breweries:
    def __init__(self, url_1, url_2, url_3):  # Constructor method with three parameters to store the URLs.
        self.url_1 = url_1  # Assigning the first URL to the instance variable.
        self.url_2 = url_2  # Assigning the second URL to the instance variable.
        self.url_3 = url_3  # Assigning the third URL to the instance variable.
    
# Alaska

    def api_status_code_1(self):  # Method to check the API status code for the first URL.
        response = requests.get(self.url_1)  # Sending a GET request to the first URL.
        return response.status_code  # Returning the status code of the response.
    
    def fetch_api_data_1(self):  # Method to fetch data from the first URL.
        if self.api_status_code_1() == 200:  # Checking if the status code is OK.
            return requests.get(self.url_1).json()  # Returning the JSON data if the status code is OK.
        else:
            return "Error"  # Returning an error message if the status code is not OK.

# 1) List the names of all breweries present in the states of Alaska, Maine, and New York
    def names_of_breweries_in_Alaska(self):  # Method to get the names of breweries in Alaska.
        if self.api_status_code_1() == 200:  # Checking if the status code is OK.
            names = []  # Initializing an empty list to store brewery names.
            for data in self.fetch_api_data_1():  # Looping through the fetched data.
                names.append(data["name"])  # Appending the name of each brewery to the list.
            return names  # Returning the list of brewery names.

# 2) What is the count of breweries in each of the states mentioned above
    def count_of_breweries_in_Alaska(self):  # Method to count the number of breweries in Alaska.
        count = 0  # Initializing a counter variable.
        for data in self.fetch_api_data_1():  # Looping through the fetched data.
            if data["name"]:  # Checking if the brewery name is not empty.
                count += 1  # Incrementing the counter.
        return count  # Returning the total count of breweries.

# 3) Count the number of types of breweries present in individual cities of the states mentioned above   
    def count_of_types_of_breweries_in_Alaska(self):  # Method to count the types of breweries in each city of Alaska.
        city_brewery_types = {}  # Initializing an empty dictionary to store city-wise brewery types.
        for data in self.fetch_api_data_1():  # Looping through the fetched data.
            city = data.get("city")  # Getting the city name from the data.
            brewery_type = data.get("brewery_type")  # Getting the brewery type from the data.
            if city and brewery_type:  # Checking if both city and brewery type are present.
                if city not in city_brewery_types:  # Checking if the city is not already in the dictionary.
                    city_brewery_types[city] = set()  # Adding the city as a key with an empty set as its value.
                city_brewery_types[city].add(brewery_type)  # Adding the brewery type to the set of types for the city.
    
        for city, types_count in city_brewery_types.items():  # Looping through the dictionary items.
            print(f"City: {city}, Number of Brewery Types: {len(types_count)}")  # Printing city and the count of types.

# 4)Count and list how many breweries have websites in the states of Alaska, Maine, and New York             
    def count_of_websites_in_Alaska(self):  # Method to count the number of breweries with websites in Alaska.
        websites = []  # Initializing an empty list to store website URLs.
        for data in self.fetch_api_data_1():  # Looping through the fetched data.
            website_url = data.get("website_url")  # Getting the website URL from the data.
            if website_url:  # Checking if the website URL is not empty.
                websites.append(website_url)  # Appending the URL to the list.
        return len(websites)  # Returning the total count of breweries with websites.

# Maine 
    def api_status_code_2(self):  # Method to check the API status code for the second URL (Maine).
        response = requests.get(self.url_2)  # Sending a GET request to the second URL.
        return response.status_code  # Returning the status code of the response.
    
    def fetch_api_data_2(self):  # Method to fetch data from the second URL (Maine).
        if self.api_status_code_2() == 200:  # Checking if the status code is OK.
            return requests.get(self.url_2).json()  # Returning the JSON data if the status code is OK.
        else:
            return "Error"  # Returning an error message if the status code is not OK.

# 1) List the names of all breweries present in the states of Alaska, Maine, and New York
    def names_of_breweries_in_maine(self):  # Method to get the names of breweries in Maine.
        if self.api_status_code_2() == 200:  # Checking if the status code is OK.
            names = []  # Initializing an empty list to store brewery names.
            for data in self.fetch_api_data_2():  # Looping through the fetched data.
                names.append(data["name"])  # Appending the name of each brewery to the list.
            return names  # Returning the list of brewery names.

# 2) What is the count of breweries in each of the states mentioned above
    def count_of_breweries_in_maine(self):  # Method to count the number of breweries in Maine.
        count = 0  # Initializing a counter variable.
        for data in self.fetch_api_data_2():  # Looping through the fetched data.
            if data["name"]:  # Checking if the brewery name is not empty.
                count += 1  # Incrementing the counter.
        return count  # Returning the total count of breweries.

 # 3) Count the number of types of breweries present in individual cities of the states mentioned above      
    def count_of_types_of_breweries_in_maine(self):  # Method to count the types of breweries in each city of Maine.
        city_brewery_types = {}  # Initializing an empty dictionary to store city-wise brewery types.
        for data in self.fetch_api_data_2():  # Looping through the fetched data.
            city = data.get("city")  # Getting the city name from the data.
            brewery_type = data.get("brewery_type")  # Getting the brewery type from the data.
            if city and brewery_type:  # Checking if both city and brewery type are present.
                if city not in city_brewery_types:  # Checking if the city is not already in the dictionary.
                    city_brewery_types[city] = set()  # Adding the city as a key with an empty set as its value.
                city_brewery_types[city].add(brewery_type)  # Adding the brewery type to the set of types for the city.
    
        for city, types_count in city_brewery_types.items():  # Looping through the dictionary items.
            print(f"City: {city}, Number of Brewery Types: {len(types_count)}")  # Printing city and the count of types.

                
#4) Count and list how many breweries have websites in the states of Alaska, Maine, and New York
    def count_of_websites_in_maine(self):  # Method to count the number of breweries with websites in Maine.
        websites = []  # Initializing an empty list to store website URLs.
        for data in self.fetch_api_data_2():  # Looping through the fetched data.
            website_url = data.get("website_url")  # Getting the website URL from the data.
            if website_url:  # Checking if the website URL is not empty.
                websites.append(website_url)  # Appending the URL to the list.
        return len(websites)  # Returning the total count of breweries with websites.

# New York
    def api_status_code_3(self):  # Method to check the API status code for the third URL (New York).
        response = requests.get(self.url_3)  # Sending a GET request to the third URL.
        return response.status_code  # Returning the status code of the response.
    
    def fetch_api_data_3(self):  # Method to fetch data from the third URL (New York).
        if self.api_status_code_3() == 200:  # Checking if the status code is OK.
            return requests.get(self.url_3).json()  # Returning the JSON data if the status code is OK.
        else:
            return "Error"  # Returning an error message if the status code is not OK.

# 1) List the names of all breweries present in the states of Alaska, Maine, and New York
    def names_of_breweries_in_newyork(self):  # Method to get the names of breweries in New York.
        if self.api_status_code_3() == 200:  # Checking if the status code is OK.
            names = []  # Initializing an empty list to store brewery names.
            for data in self.fetch_api_data_3():  # Looping through the fetched data.
                names.append(data["name"].encode("utf-8"))  # Appending the name of each brewery to the list.
            return names  # Returning the list of brewery names.

 # 2) What is the count of breweries in each of the states mentioned above   
    def count_of_breweries_in_newyork(self):  # Method to count the number of breweries in New York.
        count = 0  # Initializing a counter variable.
        for data in self.fetch_api_data_3():  # Looping through the fetched data.
            if data["name"]:  # Checking if the brewery name is not empty.
                count += 1  # Incrementing the counter.
        return count  # Returning the total count of breweries.

 # 3) Count the number of types of breweries present in individual cities of the states mentioned above      
    def count_of_types_of_breweries_in_newyork(self):  # Method to count the types of breweries in each city of New York.
        city_brewery_types = {}  # Initializing an empty dictionary to store city-wise brewery types.
        for data in self.fetch_api_data_3():  # Looping through the fetched data.
            city = data.get("city")  # Getting the city name from the data.
            brewery_type = data.get("brewery_type")  # Getting the brewery type from the data.
            if city and brewery_type:  # Checking if both city and brewery type are present.
                if city not in city_brewery_types:  # Checking if the city is not already in the dictionary.
                    city_brewery_types[city] = set()  # Adding the city as a key with an empty set as its value.
                city_brewery_types[city].add(brewery_type)  # Adding the brewery type to the set of types for the city.
    
        for city, types_count in city_brewery_types.items():  # Looping through the dictionary items.
            print(f"City: {city}, Number of Brewery Types: {len(types_count)}")  # Printing city and the count of types.

# 4)Count and list how many breweries have websites in the states of Alaska, Maine, and New York             
    def count_of_websites_in_newyork(self):  # Method to count the number of breweries with websites in New York.
        websites = []  # Initializing an empty list to store website URLs.
        for data in self.fetch_api_data_3():  # Looping through the fetched data.
            website_url = data.get("website_url")  # Getting the website URL from the data.
            if website_url:  # Checking if the website URL is not empty.
                websites.append(website_url)  # Appending the URL to the list.
        return len(websites)  # Returning the total count of breweries with websites.

# Main section
if __name__ == '__main__':
    # URLs for the three states
    url_1 = "https://api.openbrewerydb.org/v1/breweries?by_state=Alaska"
    url_2 = "https://api.openbrewerydb.org/v1/breweries?by_state=Maine"
    url_3 = "https://api.openbrewerydb.org/v1/breweries?by_state=New York"

    # Creating an instance of the Breweries class
    brewery = Breweries(url_1, url_2, url_3)

    # Printing the list of names of breweries in Alaska, Maine, and New York
    print("List of names of all breweries in Alaska, Maine, and New York:")
    print("Alaska:")
    for name in brewery.names_of_breweries_in_Alaska():
        print(name)
    
    print("\nMaine:")
    for name in brewery.names_of_breweries_in_maine():
        print(name)

    print("\nNew York:")
    for name in brewery.names_of_breweries_in_newyork():
        print(name)

    # Printing the count of breweries in Alaska, Maine, and New York
    print("\nCount of breweries in Alaska, Maine, and New York:")
    print("Alaska:", brewery.count_of_breweries_in_Alaska())
    print("Maine:", brewery.count_of_breweries_in_maine())
    print("New York:", brewery.count_of_breweries_in_newyork())

    # Printing the count of types of breweries in cities of Alaska, Maine, and New York
    print("\nCount of types of breweries in cities of Alaska, Maine, and New York:")
    print("Alaska:")
    brewery.count_of_types_of_breweries_in_Alaska()
    print("\nMaine:")
    brewery.count_of_types_of_breweries_in_maine()
    print("\nNew York:")
    brewery.count_of_types_of_breweries_in_newyork()

    # Printing the count of breweries having websites in Alaska, Maine, and New York
    print("\nCount of breweries having websites in Alaska, Maine, and New York:")
    print("Alaska:", brewery.count_of_websites_in_Alaska())
    print("Maine:", brewery.count_of_websites_in_maine())
    print("New York:", brewery.count_of_websites_in_newyork())

    # Calculating the total number of breweries with websites in Alaska, Maine, and New York
    total_websites = (
        brewery.count_of_websites_in_Alaska() +
        brewery.count_of_websites_in_maine() +
        brewery.count_of_websites_in_newyork()
    )
    
    # Printing the total number of breweries with websites in Alaska, Maine, and New York
    print("Number of breweries with websites in Alaska, Maine, and New York:", total_websites)
