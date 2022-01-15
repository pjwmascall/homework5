# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name : return pet
    return None

def remove_pet_by_name(pet_shop, name):
    # pet_shop["pets"] = [pet for pet in pet_shop["pets"] if pet["name"] is not name]
    for pet in pet_shop["pets"]:
        if pet["name"] == name : pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return True if customer["cash"] >= pet["price"] else False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is not None:
        if customer_can_afford_pet(customer, pet):
            name = pet["name"]
            amount = pet["price"]
            pets_sold = 1
            remove_pet_by_name(pet_shop, name)
            add_pet_to_customer(customer, pet)
            remove_customer_cash(customer, amount)
            add_or_remove_cash(pet_shop, amount)
            increase_pets_sold(pet_shop, pets_sold)
        else:
            pass
    else:
        pass