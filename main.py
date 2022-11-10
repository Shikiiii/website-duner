# This is a useful comment.
# This is another useful comment.
# This is the last useful comment.

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import JSONResponse
import managedb

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute()),
    name="static",
)

templates = Jinja2Templates(directory="html")

@app.get("/")
async def root(request: Request):
    if not managedb.check_if_user_exists(request.client.host):
        managedb.add_user(request.client.host)
    return templates.TemplateResponse(
        "home.html", {"request": request}
    )

@app.get("/order")
async def order(request: Request):
    return templates.TemplateResponse(
        "order.html", {"request": request}
    )

@app.get("/cart")
async def cart(request: Request):
    return templates.TemplateResponse(
        "purchase.html", {"request": request}
    )

@app.get("/information")
async def purchase(request: Request):
    return templates.TemplateResponse(
        "form.html", {"request": request}
    )

@app.get("/completed")
async def completed(request: Request):
    return templates.TemplateResponse(
        "completed.html", {"request": request}
    )

# REQUESTS

@app.post("/addtocart")
async def addtocart(request: Request, info: dict):
    """
    Add an item to a user's cart.
    :param request:
    :param info: Information
    """

    return JSONResponse(content=managedb.add_to_cart(info))

@app.post("/removefromcart")
async def removefromcart(request: Request, info: dict):
    """
    Remove an item from a user's cart.
    :param request:
    :param info: Dict containing item information:
    {
        "IP": "ip",
        "ITEM": "item"
    }
    """
    return JSONResponse(content=managedb.remove_from_cart(info))

@app.post("/getcartitems")
async def getcartitems(request: Request, ip: dict):
    """
    Add an item to a user's cart.
    :param request:
    :param ip: IP Address
    """

    return JSONResponse(content=managedb.get_cart_items(ip))

@app.post("/updatecart")
async def getcartitems(request: Request, info: dict):
    """
    Add an item to a user's cart.
    :param request:
    :param info: Information
    """

    return JSONResponse(content=managedb.update_cart(info))

@app.post("/updateuser")
async def updateuser(request: Request, info: dict):
    """
    Add an item to a user's cart.
    :param request:
    :param info: Information
    """

    return 200


# 404 HANDLER
@app.exception_handler(404)
async def custom_404_handler(_, __):
    """
    Handles 404 errors.
    :param _:
    :param __:
    """
    return HTMLResponse(str(open("notfound.html").read()), status_code=404)
