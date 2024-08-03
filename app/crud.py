from .models import Item
from .database import get_db


async def create_item(name: str, description: str):
    db = await get_db()
    async with db.cursor() as cursor:
        await cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
        await db.commit()
        await cursor.execute("SELECT * FROM items WHERE name=%s", (name,))
        row = await cursor.fetchone()
        return Item(id=row[0], name=row[1], description=row[2])


async def get_item(item_id: int):
    db = await get_db()
    async with db.cursor() as cursor:
        await cursor.execute("SELECT * FROM items WHERE id=%s", (item_id,))
        row = await cursor.fetchone()
        if row:
            return Item(id=row[0], name=row[1], description=row[2])
        return None


async def get_item_by_name(name: str):
    import pdb; pdb.set_trace()
    db = await get_db()
    async with db.cursor() as cursor:
        await cursor.execute("SELECT * FROM items WHERE name=%s", (name,))
        row = await cursor.fetchone()
        if row:
            return Item(id=row[0], name=row[1], description=row[2])
        return None


async def update_item(item_id: int, name: str, description: str):
    db = await get_db()
    async with db.cursor() as cursor:
        await cursor.execute("UPDATE items SET name=%s, description=%s WHERE id=%s", (name, description, item_id))
        await db.commit()
        await cursor.execute("SELECT * FROM items WHERE id=%s", (item_id,))
        row = await cursor.fetchone()
        return Item(id=row[0], name=row[1], description=row[2])


async def delete_item(item_id: int):
    db = await get_db()
    async with db.cursor() as cursor:
        await cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
        await db.commit()
