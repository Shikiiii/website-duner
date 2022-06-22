from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute()),
    name="static",
)

templates = Jinja2Templates(directory="html")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request}
    )

@app.get("/test")
async def read_test(request: Request):
    client_host = request.client
    print(client_host)
    return {"client_host": client_host}

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
@app.post("/usercheckip")
async def usercheckip(request: Request, ip: str):
    """
    Check user's ip information if it exists in the database upon visiting home page. If not, add to database.
    :param request:
    :param ip: String containing ip address.
    """
    pass

@app.post("/addtocart")
async def addtocart(request: Request, item: dict):
    """
    Add an item to a user's cart.
    :param request:
    :param item: Dict containing item information:
    {
        "IP": "ip",
        "ITEM": "item"
    }
    """
    pass

@app.post("/removefromcart")
async def removefromcart(request: Request, item: dict):
    """
    Remove an item from a user's cart.
    :param request:
    :param item: Dict containing item information:
    {
        "IP": "ip",
        "ITEM": "item"
    }
    """
    pass


# 404 HANDLER
@app.exception_handler(404)
async def custom_404_handler(_, __):
    """
    Handles 404 errors.
    :param _:
    :param __:
    """
    return HTMLResponse(str(open("notfound.html").read()), status_code=404)
