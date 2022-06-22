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
async def root(request: Request):
    # Check user's ip information if it exists in the database upon visiting home page. If not, add to database.
    pass

@app.post("/addtocart")
async def root(request: Request):
    # Add items to user's cart.
    pass

@app.post("/removefromcart")
async def root(request: Request):
    # Remove items from user's cart.
    pass


# 404 HANDLER

@app.exception_handler(404)
async def custom_404_handler(_, __):
    return HTMLResponse(str(open("notfound.html").read()), status_code=404)