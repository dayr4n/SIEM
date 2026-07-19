import psutil


def get_inventory_processes():
    processes = []

    for proc in psutil.process_iter():
        try:
            processes.append(
                {
                    "pid": proc.pid,
                    "ppid": proc.ppid(),
                    "name": proc.name(),
                    "exe": proc.exe(),
                    "cmdline": proc.cmdline(),
                    "cwd": proc.cwd(),
                    "username": proc.username(),
                    "status": proc.status(),
                    "create_time": proc.create_time(),
                    "terminal": proc.terminal(),
                    "uids": proc.uids(),
                    "gids": proc.gids(),
                }
            )

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return processes


def get_file_processes():
    processes = []

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            files = []

            for f in proc.open_files():
                files.append({"path": f.path, "fd": f.fd, "mode": f.mode})

            if files:
                processes.append(
                    {"pid": proc.pid, "name": proc.info["name"], "files": files}
                )

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes


def get_summary_processes():
    return {
        "processes": get_inventory_processes(),
        "file_processes": get_file_processes(),
    }
