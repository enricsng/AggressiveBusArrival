import json
import requests
import datetime as dt
import pytz
import time

# Verify that the bus stop no is 5 digits
def getCode():
    code_no = input("Enter the bus stop code:\n")
    if len(code_no) != 5:
        print("Invalid Code entered")
        getCode()
    else:
        return code_no

# Returns the bus number
def getBus():
    bus_no = input("Enter the bus number:\n")
    return bus_no

# Takes in the bus stop code and bus number. Returns the time the next bus will arrive in HTML aware time.
def getLTAResponse(code_no, bus_no):
    # Preparing the information to be passed to the server. Accountkey is unique to developer.
    headers = {"AccountKey":"******************"}
    code_Dict = {"BusStopCode":code_no, "ServiceNo":bus_no}

    # Code to send a request to LTA for the bus stop and bus number stated.
    r = requests.get("http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2", headers = headers, params=code_Dict)

    #Checking if the result is OK. 
    if r.status_code == 200:
        print("Data received")
        
    bus_data = json.loads(r.text)
    list1 = bus_data["Services"][0]["NextBus"]["EstimatedArrival"]
    return list1

# Takes in given html arrival time and prints the current time and arrival time to console.
def printCurrentArrTime(html_arr_time):
    current_time = dt.datetime.now(pytz.timezone("Asia/Singapore"))
    arrival_time = dt.datetime.strptime(html_arr_time, "%Y-%m-%dT%H:%M:%S%z")
    
    print("Current time: " + dt.datetime.strftime(current_time,"%H:%M:%S"))
    print("Arrival time: " + dt.datetime.strftime(arrival_time,"%H:%M:%S"))

# Takes the given html arrival time and prints the remaining time in seconds to console.
def remaining_time(html_arr_time):
    current_time = dt.datetime.now(pytz.timezone("Asia/Singapore"))
    arrival_time = dt.datetime.strptime(html_arr_time, "%Y-%m-%dT%H:%M:%S%z")
    
    remaining_time = arrival_time - current_time
    nice_time = remaining_time.total_seconds()
    return nice_time


code_no = getCode()
bus_no = getBus()

while True:
    html_arr_time = getLTAResponse(code_no, bus_no)
    printCurrentArrTime(html_arr_time)
    time_left = remaining_time(html_arr_time)

    for x in range(20):
        time_left = remaining_time(html_arr_time)

        if time_left < 1:
            print("The bus should have arrived by now.")
            time.sleep(5)
            print("Trying to refresh from LTA server...")
            time.sleep(5)
            break
        
        print(f"Arriving in {time_left:.0f} seconds")
        time.sleep(1)
        print(f"Will refresh in {20-x} seconds")
    if time_left < 1:
            print("After refreshing with LTA, the bus should have arrived.")
            print("Try again later.")
            break
