import json

def load_cookies(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_cookies(file_path, cookies):
    with open(file_path, 'w') as file:
        json.dump(cookies, file, indent=4)


# Ladda cookies
file_path = 'cookies.json'
cookies = load_cookies(file_path)

# Skriv ut laddade cookies
print("Loaded cookies:")
for cookie in cookies:
    print(cookie)

# Skapa cookie
cookie1 = {'name': 'session_id', 'value': 'abc123', 'expires': '2024-12-31', 'domain': 'example.com', 'path': '/'}
cookie2 = {'name': 'user_id', 'value': '123', 'expires': '2024-12-31', 'domain': 'example.com', 'path': '/'}

# Lägga till nya cookies
cookies.append(cookie1)
cookies.append(cookie2)

# Spara cookies
save_cookies(file_path, cookies)

print("\nCookies saved successfully.")
