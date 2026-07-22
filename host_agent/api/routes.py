from fastapi import APIRouter
from host_agent import agent

router = APIRouter()


def set_agent(host_agent):
    global agent
    agent = host_agent


@router.get("/")
def index():
    return {"name": "SIEM Host Agent", "status": "running"}


@router.get("/dynamic")
def dynamicd():
    return agent.dynamic_data


@router.get("/static")
def staticd():
    return agent.static_data
