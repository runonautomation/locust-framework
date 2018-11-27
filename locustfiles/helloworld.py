import os, sys
from locust import HttpLocust, TaskSet, task
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common import debug
from fixtures import helloworld
debug.disable_ssl_warnings()

class HelloWorldTaskSet(TaskSet):
    @task(3)
    def index(self):
        res = self.client.get("/", 
        name="Get index page", 
        headers = helloworld.get_credentials(),
        verify=False)

class HelloWorldHttpLocust(HttpLocust):
    task_set = HelloWorldTaskSet

if __name__ == "__main__":
    host = "http://google.com"
    debug.debug_locust(host, [HelloWorldHttpLocust])
