import requests
import uuid
import random
import time
import json

INSTAGRAM_API = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"

def random_id(prefix="android-"):
    return prefix + uuid.uuid4().hex[:16]

def gen_headers():
    return {
        "host": "i.instagram.com",
        "x-ig-app-locale": "en_OM",
        "x-ig-device-locale": "en_OM",
        "x-ig-mapped-locale": "en_AR",
        "x-pigeon-session-id": f"UFS-{uuid.uuid4()}-1",
        "x-pigeon-rawclienttime": str(time.time()),
        "x-ig-bandwidth-speed-kbps": str(random.randint(300, 1000)) + ".000",
        "x-ig-bandwidth-totalbytes-b": str(random.randint(1_000_000, 5_000_000)),
        "x-ig-bandwidth-totaltime-ms": str(random.randint(3000, 10000)),
        "x-bloks-version-id": "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb",
        "x-ig-www-claim": "0",
        "x-bloks-is-layout-rtl": "true",
        "x-ig-device-id": str(uuid.uuid4()),
        "x-ig-family-device-id": str(uuid.uuid4()),
        "x-ig-android-id": random_id(),
        "x-ig-timezone-offset": "14400",
        "x-fb-connection-type": "WIFI",
        "x-ig-connection-type": "WIFI",
        "x-ig-capabilities": "3brTv10=",
        "x-ig-app-id": "567067343352427",
        "priority": "u=3",
        "user-agent": "Instagram 275.0.0.27.98 Android (29/10; 443dpi; 1080x2224; HUAWEI; STK-L21; HWSTK-HF; kirin710; ar_OM; 458229237)",
        "accept-language": "en-OM, en-US",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept-encoding": "zstd, gzip, deflate",
        "x-fb-http-engine": "Liger",
        "ig-intended-user-id": "0",
    }

def send_recovery(email_or_username):
    if not email_or_username:
        return {"error": "Missing email_or_username"}

    body_json = {
        "adid": str(uuid.uuid4()),
        "guid": str(uuid.uuid4()),
        "device_id": random_id(),
        "query": email_or_username,
        "waterfall_id": str(uuid.uuid4())
    }

    signed_body = "SIGNATURE." + json.dumps(body_json, separators=(",", ":"))
    data = {"signed_body": signed_body}

    headers = gen_headers()

    try:
        r = requests.post(INSTAGRAM_API, headers=headers, data=data)
        return {"status": r.status_code, "response": r.text.replace('\\','')}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    print("=== Instagram Recovery Tool | By @suul ===\n")
    user = input("put ur username : ")
    result = send_recovery(user)
    print(json.dumps(result, indent=4, ensure_ascii=False))
