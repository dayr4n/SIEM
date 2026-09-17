from fastapi import FastAPI
from .api.routes import router
from .services.agent_manager import agent_manager

app = FastAPI()
app.include_router(router)

 @app.on_event("startup")
 def startup():
    threading.Thread(target=agent_manager.runall, daemon=True).start()
