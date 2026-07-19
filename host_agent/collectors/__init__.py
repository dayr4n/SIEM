from .cpu import get_summary_cpu
from .disk import get_summary_disk
from .network import get_summary_network
from .processes import get_summary_processes
from .ram import get_summary_memory
from .system import get_summary_system
from .users import get_summary_users


def collect_system_information():
    return {
        "cpu": get_summary_cpu(),
        "memory": get_summary_memory(),
        "disk": get_summary_disk(),
        "network": get_summary_network(),
        "processes": get_summary_processes(),
        "system": get_summary_system(),
        "users": get_summary_users(),
    }
