#!/usr/bin/env python
# encoding=utf-8

from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    # def on_start(self):
        # self.client.post("/Users/login/?next=//lowiki.tw/", {
            # "username": "anonymous",
            # "password": "foobarbaz"
        # })

    @task
    def region(self):
        self.client.get("/tw1000201-027/")

    @task
    def edit_frontpage(self):
        self.client.get("/tw1000201-027/Front_Page/_edit")

    @task
    def map(self):
        self.client.get("/tw1000201-027/map/")

    @task
    def edit_page(self):
        self.client.get(u"/tw1000201-027/梅洲里鎮平宮/_edit")

    @task
    def tags(self):
        self.client.get(u"/tw1000201-027/tags/避難收容處所")

class WebsiteUser(HttpLocust):
    host = "https://lowiki.tw"
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000

