from fastapi import FastAPI
from .api.routes import router
from .services.agent_manager import agent_manager

app = FastAPI()
app.include_router(router)

# @app.on_event("startup")
# def startup():
#    threading.Thread(target=agent_manager.run, daemon=True).start()
#
#    for this i have to create a funcition in agent_manager.py called run , that make all the things .
