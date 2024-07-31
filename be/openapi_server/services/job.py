from redis import Redis
from rq import Queue

class JobService:
    def __init__(self):
        r = Redis()
        self.q = Queue(connection=r)
    
    def get_all(self):
        return self.q.get_jobs()
    def get_result(self, job_id):
        job = self.get(job_id)
        return job.result
    def get_status(self, job_id):
        job = self.get(job_id)
        return job.get_status()
    def get_info(self, job_id):
        job = self.get(job_id)
        return job.get_meta().get("info", {})
    def get(self, job_id):
        return self.q.fetch_job(job_id)
    def run(self, job_info, job_function, *args, **kwargs):
        job = self.q.enqueue(job_function, *args, **kwargs)
        # store job_info into redis job queue meta field
        job.meta["info"] = job_info
        job.save_meta()
        return job