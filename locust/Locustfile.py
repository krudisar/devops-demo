from locust import HttpUser, task, between
#
import logging
from locust import events
#

''' test si considered as successful if ...
  More than 1% of the requests failed
  The average response time is longer than 200 ms
  The 95th percentile for response time is larger than 800 ms
'''
@events.quitting.add_listener
def _(environment, **kw):
    if environment.stats.total.fail_ratio > 0.01:
        logging.error("Test failed due to failure ratio > 1%")
        environment.process_exit_code = 1
    elif environment.stats.total.avg_response_time > 10:
        logging.error("Test failed due to average response time ratio > 10 ms")
        environment.process_exit_code = 1
    elif environment.stats.total.get_response_time_percentile(0.95) > 800:
        logging.error("Test failed due to 95th percentile response time > 800 ms")
        environment.process_exit_code = 1
    else:
        environment.process_exit_code = 0

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
         self.client.get("/")

    @task(2)
    def fast_response(self):
         self.client.get("/fast")

    @task(3)
    def slow_response(self):
         self.client.get("/slow")

    @task(4)
    def errors_response(self):
         self.client.get("/unstable")
