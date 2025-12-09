import sys
from unittest import result

import requests


def time_to_minutes(time):
    hour,minute = time.split(':')
    return int(hour)*60 + int(minute)


def read_input():
    #including number of trains and number of requests
    first_line=input()

    #[number_of_trains,number_of_requests]
    parts=first_line.split()

    number_of_trains = int(parts[0])
    number_of_requests = int(parts[1])

    #----------read trains info----------"
    trains=[]

    for i in range(number_of_trains):
        line=input()
        parts=line.split()

        train_name=parts[0]
        train_source=parts[1]
        train_destination=parts[2]
        train_time=parts[3]
        train_capacity=parts[4]

        trains.append({
            'train_name':train_name,
            'train_source':train_source,
            'train_destination':train_destination,
            'train_time':train_time,
            'train_capacity':train_capacity
        })

        #----------read requests info----------
        requests=[]
        for i in range(number_of_requests):
            line=input()
            parts=line.split()
            request_source=parts[0]
            request_destination=parts[1]
            request_time=parts[2]
            request_count=parts[3]

            requests.append({
                'request_source':request_source,
                'request_destination':request_destination,
                'request_time':request_time,
                'request_count':request_count
            })


#finding appropriate trains for request
def find_matching_trains(trains, request):
    result = []
    for tr in trains:
        if tr["source"] == request["source"] and tr["destination"] == request["destination"]:
            if tr["time_min"] >= request["time_min"] and tr["capacity"] >= request["count"]:
                result.append(tr)
    return result


def process_all_requests(requests,trains):
    result=[]
    for request in requests:
        result.append(find_matching_trains(trains, request))
    return result


def print_output(results):
    for match_list in results:
        for tr in match_list:
            print(f'{tr["name"]} {tr["time"]} {tr["capacity"]}')
        print("----------")


