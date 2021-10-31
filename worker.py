import asyncio
from mlq.queue import MLQ

mlq = MLQ('inference_app', 'localhost', 6379, 0)

def simple_multiply(params_dict, *args):
    return params_dict['images']

async def main():
    print("Running, waiting for messages.")
    mlq.create_listener(simple_multiply)

if __name__ == '__main__':
    asyncio.run(main())