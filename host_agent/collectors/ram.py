import psutil


def get_virtual_memory():
    memory = psutil.virtual_memory()._asdict()
    memory["status"] = get_memory_status(memory["percent"])
    return memory


def get_swap_memory():
    return psutil.swap_memory()._asdict()


def get_memory_status(percent):
    if percent < 70:
        return "Healthy"
    elif percent < 90:
        return "Warning"
    else:
        return "Critical"


# important ram but in json format
def get_summary_memory():
    data = {"virtual_memory": get_virtual_memory(), "swap_memory": get_swap_memory()}
    return data
