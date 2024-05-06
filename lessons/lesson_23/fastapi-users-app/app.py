from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from views.hello import router as router_hello
from views.items import router as router_items
from views.users import router as router_users

app = FastAPI()
app.include_router(router_hello)
app.include_router(router_items)
app.include_router(router_users)


@app.get("/")
def index_page():
    return {"message": "Hello World"}


@app.get("/demo-html/", response_class=HTMLResponse)
def demo_html():
    return """
    <!DOCTYPE html>
    <html>
    <body>
    
    <h1>My First Heading</h1>
    
    <p>My first paragraph.</p>
    
    </body>
    </html>
    """
