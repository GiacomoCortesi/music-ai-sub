from rq import Queue

class JobNotFoundException(Exception):
    pass

class JobService:
    def __init__(self, conn):
        self.q = Queue(connection=conn)
    
    def get_all(self):
        redis_jobs = self.q.get_jobs()
        jobs = []
        for redis_job in redis_jobs:
            jobs.append(self._parse_job(redis_job))

    def get(self, job_id):
        redis_job = self.q.fetch_job(job_id)

        if redis_job is None:
            raise JobNotFoundException
        
        return self._parse_job(redis_job)

    def _get_job_config(self, redis_job):
        return redis_job.get_meta().get("info", {})
    
    def _parse_job(self, redis_job):
        return {"job_id": redis_job.get_id(),
                "data": redis_job.result, 
                "config": self._get_job_config(redis_job), 
                "status": redis_job.get_status()}        

    def run(self, job_info, job_function, *args, **kwargs):
        job = self.q.enqueue(job_function, *args, **kwargs)
        # store job_info into redis job queue meta field
        job.meta["info"] = job_info
        job.save_meta()
        return self._parse_job(job)