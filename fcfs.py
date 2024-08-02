import time

# Processes with their arrival and burst times
processes = [{'id': 'P1', 'arrival': 0, 'burst': 10},
             {'id': 'P2', 'arrival': 2, 'burst': 4},
             {'id': 'P3', 'arrival': 4, 'burst': 6}]

# Function to simulate FCFS scheduling
def fcfs(processes):
    time_passed = 0
    total_waiting_time = 0
    waiting_times = {}
    turnaround_times = {}
    response_times = {}
    first_response = {}

    for process in processes:
        if time_passed < process['arrival']:
            time_passed = process['arrival']
        wait_time = time_passed - process['arrival']
        total_waiting_time += wait_time
        print(f"Process {process['id']} starts at time {time_passed}")
        response_times[process['id']] = time_passed - process['arrival']
        if process['id'] not in first_response:
            first_response[process['id']] = time_passed - process['arrival']
        time_passed += process['burst']
        turnaround_times[process['id']] = time_passed - process['arrival']
        print(f"Process {process['id']} finishes at time {time_passed}")
        time.sleep(process['burst'] * 0.1)

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = sum(turnaround_times.values()) / len(turnaround_times)
    avg_response_time = sum(response_times.values()) / len(response_times)
    
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"Average response time: {avg_response_time}")

fcfs(processes)
