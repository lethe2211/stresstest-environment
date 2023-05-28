import random
from locust import HttpUser, task, constant_throughput

# Describe how a user should behave
class SampleUser(HttpUser):
    wait_time = constant_throughput(1) # Adjust the request rate to 1 per second

    # This method is called only once when the user is created
    def on_start(self):
        pass

    @task
    def get(self):
        id = random.randint(1, 100)
        self.client.get(f"/api/{id}")