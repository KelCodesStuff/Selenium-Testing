from locust import HttpUser, TaskSet, task

class AppleWebsiteTest(TaskSet):
    @task(1)
    def load_homepage(self):
        self.client.get("/")

    @task(2)
    def search_for_iphone(self):
        self.client.get("/search?query=iPhone")

class WebsiteUser(HttpUser):
    tasks = [AppleWebsiteTest]
    min_wait = 1000
    max_wait = 5000
