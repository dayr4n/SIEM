import platform
import socket


def get_summary_system():
    return {
        "HOSTNAME": socket.gethostname(),
        "OS": platform.system(),
        "DISTRIBUTION": platform.release(),
        "VERSION": platform.version(),
        "ARCHITECTURE": platform.machine(),
        "PROCESSOR": platform.processor(),
    }
