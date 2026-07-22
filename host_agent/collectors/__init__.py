from .cpu import *
from .ram import *
from .disk import *
from .network import *
from .processes import *
from .system import *
from .users import *


def collect_system_information():
    return {
        "cpu": get_summary_cpu(),
        "memory": get_summary_ram(),
        "disk": get_summary_disk(),
        "network": get_summary_network(),
        "processes": get_summary_processes(),
        "system": get_summary_system(),
        "users": get_summary_users(),
    }
