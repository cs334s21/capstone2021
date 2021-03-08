import random
import time
import redis

redis_database = redis.Redis()


def generate_jobs(database):
    for _ in range(10):
        client_id = random.randint(0, 10000)
        value = random.randint(0, 10)
        print(f"I am generating  work with value {value}!")
        database.hset("jobs_waiting", client_id, value)


def emulate_job_creation(database):
    for _ in range(5):
        generate_jobs(database)
        time.sleep(30)


emulate_job_creation(redis_database)
