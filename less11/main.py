from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dish(BaseModel):
    id: int
    name: str
    price: float
    is_ready: bool = False

menu = [
    {"id": 1, "name": "Pizza", "price": 10.99, "is_ready": False},
    {"id": 2, "name": "Burger", "price": 8.99, "is_ready": False},
    {"id": 3, "name": "Pasta", "price": 12.99, "is_ready": False},
    {"id": 4, "name": "Salad", "price": 6.99, "is_ready": False}
]

orders = []

@app.get("/menu")
def get_menu(): 
    return {"You can order": menu}


@app.post("/orders")
def create_order(dish: Dish):
    orders.append(dish)
    return {f"Your: {dish.name} has been ordered!"}

@app.get("/orders")
def get_orders():
    if orders:
        return {"Our orders": orders}
    return "You don`t orders any dishes yet"
    

@app.put("/orders/{dish_id}")
def update_dish(dish_id: int, ready_status: bool):
    dish = next(d for d in orders if d.id == dish_id)
    if dish:
        dish.is_ready = ready_status
        return {f"Your {dish.name} {'ready' if ready_status else 'not ready'}"}
    return {"message": "Dish not found"}

@app.delete("/orders/{dish_id}")
def delete_order(dish_id: int):
    dish_to_remove = next(d for d in orders if d.id == dish_id)
    if dish_to_remove:
        orders.remove(dish_to_remove)
        return {f"Your {dish_to_remove} has been canceled"}
    return {"message": "Dish not found"}
