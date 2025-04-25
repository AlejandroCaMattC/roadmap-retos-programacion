import random
import time
import threading

"""Callbacks in Python"""

# Callbacks are functions that are passed as arguments
# to other functions and are executed


def greeting_process(name: str, callback):
    print("Executing greeting process...")
    callback(name)


def greet_callback(name: str):
    print(f"Hello, {name}")


greet_callback("Alejandro")

greeting_process("Alejandro", greet_callback)

"""Exercise"""

# Create a order simulator from a restaurant using callbacks.


def order_process(dish_name: str, confirm_callback, ready_callback, delivered_callback):
    def process():
        print("Executing order process...\n")
        confirm_callback(dish_name)
        time.sleep(random.randint(1, 10))
        ready_callback(dish_name)
        time.sleep(random.randint(1, 10))
        delivered_callback(dish_name)

    threading.Thread(target=process).start()


def confirm_order(dish_name: str):
    print(f"Your order {dish_name} has been confirmed \n")


def order_ready(dish_name: str):
    print(f"Your order {dish_name} is ready \n")


def order_delivered(dish_name: str):
    print(f"Your order {dish_name} has been delivered \n")


order_process("Pizza de Anchoas", confirm_order, order_ready, order_delivered)
order_process("Pizza 4 quesos", confirm_order, order_ready, order_delivered)
order_process("Pizza Suprema", confirm_order, order_ready, order_delivered)
order_process("Pizza Hawaiana", confirm_order, order_ready, order_delivered)
