from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Define a Pydantic model for the item
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def create_item(item: Item):
    items = []
    if os.path.exists("items.json"):
        with open("items.json", "r") as f:
            try:
                items = json.load(f)
            except json.JSONDecodeError:
                items = []
    
    new_item = item.dict()
    new_item["id"] = len(items) + 1
    items.append(new_item)

    with open("items.json", "w") as f:
        json.dump(items, f, indent=4)
    
    return new_item

@app.get("/items")
def read_items():
    if not os.path.exists("items.json"):
        raise HTTPException(status_code=404, detail="Items not found")

    with open("items.json", "r") as f:
        try:
            items = json.load(f)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Error reading items file")

    return items

# Atualiza um item com base no ID
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    if not os.path.exists("items.json"):
        raise HTTPException(status_code=404, detail="Items not found")
    
    with open("items.json", "r") as f:
        items = json.load(f)

    # Busca o item pelo ID
    for item in items:
        if item["id"] == item_id:
            item.update(updated_item.dict())  # Atualiza o item com os novos dados
            with open("items.json", "w") as f:
                json.dump(items, f, indent=4)
            return item

    raise HTTPException(status_code=404, detail="Item not found")

# Deleta um item com base no ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if not os.path.exists("items.json"):
        raise HTTPException(status_code=404, detail="Items not found")
    
    with open("items.json", "r") as f:
        items = json.load(f)

    # Filtra o item pelo ID
    items = [item for item in items if item["id"] != item_id]

    # Salva os itens restantes de volta no arquivo
    with open("items.json", "w") as f:
        json.dump(items, f, indent=4)

    return {"message": "Item deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)
