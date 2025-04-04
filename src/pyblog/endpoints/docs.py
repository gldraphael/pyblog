from fastapi import APIRouter
from starlette.responses import HTMLResponse

docs_router = APIRouter()

@docs_router.get("/", include_in_schema=False)
def api_documentation():
    return HTMLResponse("""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>pyblog API</title>
    <script src="https://unpkg.com/@stoplight/elements/web-components.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/@stoplight/elements/styles.min.css">
  </head>
  <body>
    <elements-api apiDescriptionUrl="/api/openapi.json" router="hash" />
  </body>
</html>
""")
