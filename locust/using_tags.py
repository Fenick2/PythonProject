from locust import User, task, tag, between


class MyWebsiteUser(User):

    @tag('tag0')
    @task
    def task_0(self):
        print("Task 0 was performed")

    @tag('tag1')
    @task
    def task_1(self):
        print("Task 1 was performed")

    @tag('tag2')
    @task
    def task_2(self):
        print("Task 2 was performed")

    @tag('tag1', 'tag2', 'tag3')
    @task
    def task_3(self):
        print("Task 3 was performed")

    wait_time = between(2, 3)

# locust -f using_tags.py --host=http://localhost:5000 --headless --tags tag1 -u 1
