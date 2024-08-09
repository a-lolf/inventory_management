from fastapi import FastAPI, HTTPException
from .crud import create_item, get_item, update_item, delete_item, get_item_by_name
from .cache import get_cached_item, cache_item
from .schemas import ItemCreate, ItemUpdate, ItemOut
from .tasks import print_hello
from app.logger import logger
from app.logging_config import setup_logging

setup_logging()

app = FastAPI()


@app.post("/items/", response_model=ItemOut)
async def create_inventory_item(item: ItemCreate):
    try:
        # print_hello.delay()
        existing_item = await get_item_by_name(item.name)
        if existing_item:
            raise HTTPException(status_code=400, detail="Item already exists")
        new_item = await create_item(item.name, item.description)
        return new_item
    except Exception as e:
        print(e)
        logger.error(f'create_inventory_item error', exc_info=e)


@app.get("/items/{item_id}", response_model=ItemOut)
async def read_inventory_item(item_id: int):
    try:
        cached_item = await get_cached_item(item_id)
        if cached_item:
            return cached_item
        db_item = await get_item(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        await cache_item(item_id, db_item)
        return db_item
    except Exception as e:
        print(e)


@app.put("/items/{item_id}", response_model=ItemOut)
async def update_inventory_item(item_id: int, item: ItemUpdate):
    try:
        db_item = await get_item(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        updated_item = await update_item(item_id, item.name or db_item.name, item.description or db_item.description)
        return updated_item
    except Exception as e:
        print(e)


@app.delete("/items/{item_id}")
async def delete_inventory_item(item_id: int):
    try:
        db_item = await get_item(item_id)
        if db_item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        await delete_item(item_id)
        return {"message": "Item deleted successfully"}
    except Exception as e:
        print(e)
