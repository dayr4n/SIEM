class Agent:
    def __init__(self, ip, version, name):
        self.ip = ip
        self.version = version
        self.name = name
        self.users = {}
        self.system = {}
        self.cpu_core = {}
        self.cpu = {}
        self.ram = {}
        self.processes = {}
        self.network = {}
        self.disk = {}
