import runpod
import requests

def get_my_ip(job):
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']


runpod.serverless.start({"handler": get_my_ip})