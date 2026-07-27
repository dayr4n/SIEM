from server.models.agent import Agent


class AgentManager:
    def __init__(self):
        self.agents = {}

        self.total_agents = 0
        self.online_agents = 0
        self.registration_count = 0

    def register(self, data):
        ip = data["ip"]
        agent = data["agent"]
        version = data["version"]

        if ip not in self.agents:
            new_agent = Agent(ip=ip, version=version, name=agent)
            self.agents[ip] = new_agent
            self.total_agents += 1
            self.online_agents += 1
            self.registration_count += 1
            print(f"[+] Agent registered: {new_agent.name} ({new_agent.ip})")
            print(f"[*] Total agents: {self.total_agents}")
        else:
            return "The Agent already exists sorry you can't create it .."

    def staticinfo(self, data):
        ip = data["ip"]

        if ip not in self.agents:
            print("Sorry your agent is not registered..")
        else:
            agent = self.agents[ip]
            agent.users = data["users"]
            agent.system = data["system"]
            agent.cpu_core = data["cpu_core"]
            print("STATIC INFO STORED ON THE SERVER AGENT ..")

    def dynamicinfo(self, data):
        ip = data["ip"]

        if ip not in self.agents:
            print("Sorry your agent is not registered..")
        else:
            agent = self.agents[ip]
            agent.cpu = data["cpu"]
            agent.ram = data["ram"]
            agent.processes = data["processes"]
            agent.network = data["network"]
            agent.disk = data["disk"]
            print("DYNAMIC INFO STORED ON THE SERVER AGENT ..")

    def list_agents(self):
        return {
            ip: {
                "name": agent.name,
                "version": agent.version,
                "ram": agent.ram,
                "cpu": agent.cpu,
                "users": agent.users,
                "system": agent.system,
                "processes": agent.processes,
                "network": agent.network,
                "disk": agent.disk,
            }
            for ip, agent in self.agents.items()
        }

    def get_agent(self, ip):
        return self.agents.get(ip)

    # SYSTEM INFO
    def get_system(self, ip, field):
        agent = self.get_agent(ip)

        if not agent:
            return None
        else:
            return agent.system.get(field)

    # USERS INFO \ INCOMPLETE THERE IS MORE INFORMATION LEFT

    def get_users(self, ip):
        agent = self.get_agent(ip)

        if not agent:
            return None
        else:
            return agent.users

    # CPU INFO

    def get_cpu(self, ip):
        agent = self.get_agent(ip)

        if not agent:
            return None
        else:
            return agent.cpu

    # NETWORK INFO
    def get_network(self, ip, field):
        agent = self.get_agent(ip)

        if not agent:
            return None
        else:
            return agent.network.get(field)

    # DISK INFO

    def get_disk(self, ip, field):
        agent = self.get_agent(ip)

        if not agent:
            return None
        else:
            return agent.disk.get(field)


agent_manager = AgentManager()

# IMPORTANT I GOT TO CREATE THE AGENT CLASS , AND AFTER IT I GOT TO CREATE THE DEF TO ENTER
# IN HIS ATRIBUTES THE INFO OF THE HOST , ALL THAT WILL WORK FIRST FROM THE AGENT MANAGER , THIS AGENT WILL GET THE INFO TO AFTER IT
# ORQUEST THE AGENTS .
