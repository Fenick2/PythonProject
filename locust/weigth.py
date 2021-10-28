from locust import User, task, tag, between


class MyWebsiteUser(User):

    @task(4)
    def task_0(self):
        print('Task 0 was performed')

    @task(1)
    def task_1(self):
        print('Task 1 was performed')

    wait_time = between(2, 3)

# locust -f weigth.py --host=http://localhost:5000 --headless -u 1
