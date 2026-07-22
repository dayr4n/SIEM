import psutil


def get_virtual_ram():
    memory = psutil.virtual_memory()._asdict()
    memory["status"] = get_status_ram(memory["percent"])
    return memory


def get_swap_ram():
    return psutil.swap_memory()._asdict()


def get_status_ram(percent):
    if percent < 70:
        return "Healthy"
    elif percent < 90:
        return "Warning"
    else:
        return "Critical"


# important ram but in json format
def get_summary_ram():
    data = {"virtual_memory": get_virtual_ram(), "swap_memory": get_swap_ram()}
    return data
