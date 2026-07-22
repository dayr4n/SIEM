import threading
from .agent import HostAgent
from fastapi import FastAPI
from .api.routes import router, set_agent

# AGENT \ HERE WE ARE GOING TO LAUNCH THE LOCALAGENT THAT WE HAVE CREATED IN AGENT.PY..
localAgent = HostAgent()
set_agent(localAgent)
# API \ HERE WE CAN SEE THE MAIN STARTUP OF THE API THAT WILL RESPONSE ALL THE SERVER REQUESTS , ALSO IN A FUTURE WE WILL TRY TO MAKE THAT API CALLED BY THE HOST SYSTEM..
app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup():
    threading.Thread(target=localAgent.run, daemon=True).start()
