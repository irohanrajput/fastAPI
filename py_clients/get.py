





















import requests

url = 'http://localhost:8000/items_bool/4'
# url = 'http://localhost:8000/items'

r = requests.get(url, params={"q": "irohanrajput"})

print (r.json())


# Recap¶
# Import FastAPI.
# Create an app instance.
# Write a path operation decorator (like @app.get("/")).
# Write a path operation function (like def root(): ... above).
# Run the development server (like uvicorn main:app --reload).