try:
    with open('./bot/secrets.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        API_KEY = lines[0]
        API_SECRET_KEY = lines[1]
except Exception as e:
    print(f"Error reading secrets: {e}")
    API_KEY = None
    API_SECRET_KEY = None
