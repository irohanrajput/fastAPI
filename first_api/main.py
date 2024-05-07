from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#order of the path operation matters
# url = 'http://localhost:8000/users/4'
# The first one will always be used since the path matches first.


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/4")
async def read_user_me():
    return {"user_id": "the current"}


#query parameters: when function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

fake_items_db = [{"item_name": "no item 1"}, {"item_name": "mogambo2"}, {"item_name": "Bazigarrr3"}]

@app.get("/items/")
async def read_item(first_index: int = 1, limit: int = 2):
    return fake_items_db[first_index : first_index + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    if q:
        return {"yo, the item ID is": item_id, "query param is": q}
    return {"no query params were passed, so the item id is": item_id}

#using bool shit
@app.get("/items_bool/{item_id}")
async def read_item(item_id: str, q: str | None = None, short_desc: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q param passed here is ": q})
    if short_desc:
        item.update(
            {"description": "The description is short thoo"}
        ) 
    else:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
          
    return item

# 3