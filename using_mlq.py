# ========================================================================
# [1]“mlq: Documentation,” Openbase. https://openbase.com/python/mlq/documentation (accessed Oct. 31, 2021).
# ========================================================================


import time
from mlq.queue import MLQ
from tqdm import trange
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
import uvicorn

desc = """

## How it works

See the figure in readme

"""

app = FastAPI(
                title="MLQ app",
                description=desc,
                docs_url="/documentation"
            )



# Create MLQ: namespace, redis host, redis port, redis db
mlq = MLQ('inference_app', 'localhost', 6379, 0)

IDS = None
RESULTS = None

@app.get("/", response_class=RedirectResponse, status_code=status.HTTP_302_FOUND)
async def docs():
    return "/documentation"


@app.get("/results/", status_code=status.HTTP_200_OK)
async def get_result():
    global IDS, RESULTS

    results_ = []
    # get global variable
    for k in trange(len(IDS), desc="GETTING result", colour="yellow"):
    # loop over the jod IDs list and retreive results one by one
        
        # against each of the ID ---> acquire results like this
        result = None
        while not result:
            time.sleep(0.1)
            job = mlq.get_job(IDS[k])
            # retreive results in FIFO order , if ist item's results have not been calculated then result var. will be None
            result = job['result'] # if not calculated then result will be None
            

        results_.append(result)

    RESULTS = results_

    print(RESULTS)

    return {
                "results" : RESULTS,
            }




@app.get("/get_result/{id}", status_code=status.HTTP_200_OK)
async def get_result(id:str):
    global IDS, RESULTS

  
    # against each of the ID ---> acquire results like this
    result = None
    while not result:
        time.sleep(0.1)
        job = mlq.get_job(id)
        # retreive results in FIFO order , if ist item's results have not been calculated then result var. will be None
        result = job['result'] # if not calculated then result will be None

    return {
                "results" : result,
            }


@app.post("/inference/{n_imgs}", status_code=status.HTTP_200_OK)
async def get_inference(n_imgs : int):
    global IDS
    ids = []
    _ = []
    for k in trange(n_imgs, total=n_imgs, desc="IMG. NO:", colour="green"):

        job_id = mlq.post({'images': 1234})

        ids.append(job_id)


    print(ids)
    for mk in ids:
        result = None
        while not result:
            time.sleep(0.1)
            job = mlq.get_job(mk)
            # retreive results in FIFO order , if ist item's results have not been calculated then result var. will be None
            result = job['result'] # if not calculated then result will be None
            _.append(result)
            

    # set global variable
    IDS = ids

    print(IDS)

    return {'msg': 'Processing, check back soon.', 'job_id': ids, "results" : _}






if __name__ == '__main__':
    uvicorn.run("using_mlq:app", host="0.0.0.0", port=8081, reload=True, debug=True)