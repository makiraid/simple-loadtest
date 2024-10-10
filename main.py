import asyncio
import time
import json
from http_client import HTTPClient, run_load_test

def load_test(config, count):
    start_time = time.time()
    
    http_client = HTTPClient(config['url'], headers=config['headers'], body=config['body'])
    
    # Run the async load test
    results = asyncio.run(run_load_test(http_client, count))
    
    end_time = time.time()
    duration = end_time - start_time

    # Print results and performance stats
    successful_requests = sum(1 for result in results if isinstance(result, dict) and "error" not in result)
    failed_requests = count - successful_requests

    print("==== Load Test Results: ====")
    print(f"Total Requests: {count}")
    print(f"Successful Requests: {successful_requests}")
    print(f"Failed Requests: {failed_requests}")
    print(f"Total Duration: {duration:.2f} seconds")
    print(f"Requests per second: {count / duration:.2f}")

if __name__ == '__main__':
    # Load configuration from JSON file
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Input for number of requests
    while True:
        request_count_input = input("How many requests? ").strip()
        
        if not request_count_input:
            print("Error: Please input a request count.")
            continue
        
        try:
            request_count = int(request_count_input) 
            if request_count <= 0:
                print("Error: Please input a positive integer.")
                continue
            break
        except ValueError:
            print("Error: Please input a valid integer.")

    load_test(config, request_count)
