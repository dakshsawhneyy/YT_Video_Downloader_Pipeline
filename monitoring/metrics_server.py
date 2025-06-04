# Creating and exposing metrics over HTTP
from prometheus_client import start_http_server, Summary, Counter, Histogram
import threading
import time
import random

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Action counters #* Using Counter to INCREMENT different function called
search_counter = Counter("search_requests_total", "Total number of search actions performed")
download_counter = Counter("download_requests_total", "Total number of download actions performed")
delete_counter = Counter("delete_requests_total", "Total number of delete actions performed")

# Download duration histogram - measures time to download
download_duration_histogram = Histogram("download_duration_seconds", "Time taken to download video")

def start_metrics_server():
    # Start up the server to expose the metrics.
    start_http_server(8000)  # Start exposing on port 8000
    print("Prometheus metrics server started on port 8000")

# Simulate some work to record metrics
@REQUEST_TIME.time() # measures how long process_request() takes.
def process_request():
    time.sleep(random.random())

def run_metrics_server_in_thread(): # Run the metrics server in a separate thread
    metrics_thread = threading.Thread(target=start_metrics_server)
    metrics_thread.daemon = True
    metrics_thread.start()