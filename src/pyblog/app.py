from pyblog.api.app import create_app
from pyblog.containers import Container

container = Container()
app = create_app(container)
