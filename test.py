import requests,json
def check_ip(base_url:str,ip:str):
    try:
        o=requests.post(base_url,json={'password':"Xa4]:K%3OD0s",'ip':ip}).text
        return json.loads(o)
    except:pass
    return {'error':'check server'}

print(check_ip())