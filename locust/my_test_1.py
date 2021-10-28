from locust import HttpUser, task, between


class MyWebSiteUser(HttpUser):
    @task
    def load_user_profile(self):
        self.client.get("/count_views")

    wait_time = between(1, 3)

# locust -f my_test_1.py --host=http://localhost:5000/ --headless -u 2000 -r 50 -t 40s
