# Database things
import pymongo
uri = 'mongodb+srv://ceco:1234@websiteproject.gntpa.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client.siteinfo
users = db.users
carts = db.carts
purchases = db.purchases
import pprint

def add_user(ip: str):
    """
    Add a new user to the database.
    """

    dict = {
        "ip": ip,
        "cart": {

        },
        "information": {
            "personinfo": {
                "name": "name",
                "email": "email",
                "address": "address",
                "city": "city",
                "region": "region",
                "ZIP": "zip"
            },
            "cardinfo": {
                "name": "name",
                "cardnumber": "cardnumber",
                "expmonth": "expmonth",
                "expyear": "expyear",
                "CVV": "cvv"
            }
        }
    }

    users.insert_one(dict)


def add_to_cart(info: dict):
    """
    Add a new item to a user's cart.
    """
    userToUpdate = {"ip": info["ip"]}

    cart = users.find_one({"ip": info["ip"]})["cart"]
    if info["item"] in cart:
        cart[info["item"]] += 1
    else:
        cart[info["item"]] = 1

    users.update_one(userToUpdate, {"$set": {"cart": cart}})


def remove_from_cart(info):
    """
    Remove an item from a user's cart.
    """

    userToUpdate = {"ip": info["ip"]}

    cart = users.find_one({"ip": info["ip"]})["cart"]
    if info["item"] in cart:
        cart.pop(info["item"])

    users.update_one(userToUpdate, {"$set": {"cart": cart}})

def update_cart(info):
    """
    Update cart's quantity.
    """

    userToUpdate = {"ip": info["ip"]}

    cart = users.find_one({"ip": info["ip"]})["cart"]
    if info["item"] in cart:
        cart[info["item"]] = info["quantity"]

    users.update_one(userToUpdate, {"$set": {"cart": cart}})

def finish_order():
    """
    Finish a user's order and move it to queue.
    """
    pass

def get_cart_items(ip: dict):
    """
    Get user's items in cart.
    :param ip:
    :return items
    """

    userToUpdate = {"ip": ip["ip"]}

    cart = users.find_one({"ip": ip["ip"]})["cart"]
    return cart

def update_user_info(info: dict):
    """
    Update user's information after ordering.
    :param info:
    :return:
    """

    user = {"ip": info["ip"]}
    userToUpdate = users.find_one(user)
    userToUpdate["information"]["personinfo"]["name"] = info["name"]
    userToUpdate["information"]["personinfo"]["email"] = info["email"]
    userToUpdate["information"]["personinfo"]["address"] = info["address"]
    userToUpdate["information"]["personinfo"]["city"] = info["city"]
    userToUpdate["information"]["personinfo"]["region"] = info["region"]
    userToUpdate["information"]["personinfo"]["ZIP"] = info["zipcode"]
    userToUpdate["information"]["cardinfo"]["name"] = info["cardname"]
    userToUpdate["information"]["cardinfo"]["cardnumber"] = info["cardnumber"]
    userToUpdate["information"]["cardinfo"]["expmonth"] = info["cardexpmonth"]
    userToUpdate["information"]["cardinfo"]["expyear"] = info["cardexpyear"]
    userToUpdate["information"]["cardinfo"]["CVV"] = info["cardcvv"]

    users.update_one(user, {"$set": userToUpdate})
    return userToUpdate

def check_if_user_exists(ip: str):
    """
    Checks if a user already exists. Returns True if it does. False if it doesn't.
    :param ip:
    :return: True or False
    """

    if users.find_one({"ip": ip}) is not None:
        return True
    else:
        return False
