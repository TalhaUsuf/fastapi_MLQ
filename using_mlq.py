# ========================================================================
# [1]“mlq: Documentation,” Openbase. https://openbase.com/python/mlq/documentation (accessed Oct. 31, 2021).
# ========================================================================


import time
from mlq.queue import MLQ




# Create MLQ: namespace, redis host, redis port, redis db
mlq = MLQ('inference_app', 'localhost', 6379, 0)

job_id = mlq.post({'images': 1234})

result = None
while not result:
    time.sleep(0.1)
    job = mlq.get_job(job_id)
    result = job['result']
    print(result)
