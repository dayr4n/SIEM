import psutil


def get_partitions_disk():
    partitions = psutil.disk_partitions()
    return [p._asdict() for p in partitions]


def get_usage_disk():
    usage = psutil.disk_usage("/")
    return usage._asdict()


def get_iocounters_disk():
    # I have to learn deeper this
    return {
        disk: stats._asdict()
        for disk, stats in psutil.disk_io_counters(perdisk=True).items()
    }


# important json with all the disk info
def get_summary_disk():
    return {
        "partitions": get_partitions_disk(),
        "usage": get_usage_disk(),
        "counters": get_iocounters_disk(),
    }
