#!/usr/bin/python3
import requests
import pprint

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neodata = requests.get(NEOURL + startdate + "&" + nasacreds).json()
    # return the largest astoriod
    
    ne_objects = neodata['near_earth_objects'] 

    for date in ne_objects:
        largest = []
        for i in ne_objects[date]:
            # print out the estimated max diameter of the objects in range
           largest.append(round(i['estimated_diameter']['feet']['estimated_diameter_max']))
           
    largest.sort()
    print(largest)
    print(f'the largest object is: {largest[-1]}')
    print("\n")
    

if __name__ == "__main__":
    main()
    
