from random import choice
from locust import HttpUser, task

from docs.config import INTERESTED_PAIRS


class QueryUser(HttpUser):
    @task
    def get_query(self):
        self.client.get('/courses')
        self.client.get(f'/{choice(INTERESTED_PAIRS)}')
