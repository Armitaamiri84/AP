def time_to_minutes(time):
    hour, minute = time.split(':')
    return int(hour)*60 + int(minute)


def read_input():
    first_line = input()
    parts = first_line.split()
    number_of_trains = int(parts[0])
    number_of_requests = int(parts[1])

    trains = []
    for _ in range(number_of_trains):
        line = input()
        parts = line.split()
        train_name = parts[0]
        train_source = parts[1]
        train_destination = parts[2]
        train_time = parts[3]
        train_capacity = int(parts[4])

        trains.append({
            'name': train_name,
            'source': train_source,
            'destination': train_destination,
            'time': train_time,
            'time_min': time_to_minutes(train_time),
            'capacity': train_capacity
        })

    requests = []
    for _ in range(number_of_requests):
        line = input()
        parts = line.split()
        req_source = parts[0]
        req_destination = parts[1]
        req_time = parts[2]
        req_count = int(parts[3])

        requests.append({
            'source': req_source,
            'destination': req_destination,
            'time': req_time,
            'time_min': time_to_minutes(req_time),
            'count': req_count
        })

    return trains, requests


def find_matching_trains(trains, request):
    result = []
    for tr in trains:
        if tr["source"] == request["source"] and tr["destination"] == request["destination"]:
            if tr["time_min"] >= request["time_min"] and tr["capacity"] >= request["count"]:
                result.append(tr)
    return result


def process_all_requests(trains, requests):
    results = []
    for request in requests:
        results.append(find_matching_trains(trains, request))
    return results



def print_output(results):
    for match_list in results:
        for tr in match_list:
            print(f'{tr["name"]} {tr["time"]} {tr["capacity"]}')
        print("----------")


def main():
    trains, requests = read_input()
    results = process_all_requests(trains, requests)
    print_output(results)


if __name__ == "__main__":
    main()
