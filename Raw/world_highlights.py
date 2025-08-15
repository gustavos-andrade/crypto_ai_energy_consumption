import requests

# Step 1: Start a session to store cookies
session = requests.Session()

# Step 2: Login
login_url = "https://www.iea.org/login"
payload = {
    "email": "gustavo.s-andrade@hotmail.com",
    "password": "Gu250011996!"
}
session.post(login_url, data=payload)

# Step 3: Download the file (URL found via DevTools when clicking download)
download_url = "https://www.iea.org/product/download/018779-000282-018513"
response = session.get(download_url)

# Step 4: Save file locally
with open("Raw/world_highlights.xlsx", "wb") as f:
    f.write(response.content)

print("File downloaded successfully!")
