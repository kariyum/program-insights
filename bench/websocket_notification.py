import requests
import sys
import logging
import json
import random
import time
import io

from concurrent.futures import ThreadPoolExecutor, wait

config_dev = {
    "payload": "payload.json",
    "ip": "10.3.16.105"
}

config_cert = {
    "payload": "payload_cert.json",
    "ip" : "10.4.48.146"
}

config = config_cert

f = open(config["payload"])
payload = json.load(f)
f.close()

# ip = "10.3.16.105"
ip = config["ip"]
def login(session, email: str, password: str = 'password'):
    payload = {"email": email, "password": password}
    logging.info(f"post  -> /login {payload['email']}")
    x = session.post(f"http://{ip}/login", json = payload)
    cookie = x.cookies
    if x.status_code != 200:
        raise Exception(f"User was not able to login with email: {email}, pwd: {password}, ip: {ip}")
    return cookie
count = 0
def fetchCustomHeaders(session):
    # print(f"Fetching custom headers. http://{ip}/common/custom-headers")
    t1 = time.perf_counter()
    # print(f"http://{ip}/promotion-planning/promotion/tree/by-id/P00000607")
    global count
    response = session.get(f"http://{ip}/promotion-planning/promotion/tree/by-id/P00000607", cookies = {"Authorization": session.cookies.get("Authorization")})
    count += 1
    print(count)
    response.raise_for_status()
    t2 = time.perf_counter()
    ttfb = t2 - t1
    # print(f"TTFB: {ttfb}")
    if response.status_code != 200:
        logging.exception(f"Could not fetch custom-headers response {response}")
    # print(response.elapsed)
    # for chunk in response:
    #     x = chunk
    js_resp = response.json() # json.loads(response.text)
    ttlb = time.perf_counter() - t2
    # print(f"TTLB: {ttlb}")
    response_time = time.perf_counter() - t1
    # print(f"Took: {response_time}")
    # print(f"Response length is {len(js_resp)}")
    return ttfb, ttlb, response_time

def deduce_stats(metric: str, l: list[float], verbode=True) -> None:
    s = sum(l)
    size = len(l)
    avg = s / size if size != 0 else 0
    maximum = max(l)
    minimum = min(l)
    if verbode: print(f"{metric.upper()}: min = {minimum}, max = {maximum}, avg = {avg}")
    return {
        metric: {
            "min": minimum,
            "max": maximum,
            "avg": avg,
        }
    }
    

if __name__=='__main__':
    adapter = requests.adapters.HTTPAdapter(pool_connections=1000, pool_maxsize=1000)
    session = requests.Session()
    session.mount('http://', adapter)
    session.cookies = login(session, "planner@riteaid.com")
    USERS = [1] # [2, 5, 10, 20]
    MAX_REQUESTS = 1

    stats = dict()
    for WORKERS in USERS:
        stats[WORKERS] = dict()
        with ThreadPoolExecutor(max_workers= WORKERS) as executor:
            futures = [executor.submit(fetchCustomHeaders, session) for _ in range(MAX_REQUESTS)]
            x = [f.result() for f in wait(futures).done]
            transposed_list = [[row[i] for row in x] for i in range(len(x[0]))]
            ttfb = transposed_list[0]
            ttlb = transposed_list[1]
            rsp_time = transposed_list[2]
            ttfb = deduce_stats("ttfb", ttfb)
            ttlb = deduce_stats("ttlb", ttlb)
            rsp_time = deduce_stats("response time", rsp_time)
            stats[WORKERS].update(ttfb)
            stats[WORKERS].update(ttlb)
            stats[WORKERS].update(rsp_time)
        f = open(f"data/{WORKERS}.json", "w")
        json.dump(stats[WORKERS], f)
        f.close()
            
    # print(stats)
    f = open("stats.json", "w")
    json.dump(stats, f)
    f.close()
