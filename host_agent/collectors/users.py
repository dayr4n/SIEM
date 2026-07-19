import psutil
from datetime import datetime


def get_logged_users():
    users = []

    for user in psutil.users():
        users.append(
            {
                "username": user.name,
                "terminal": user.terminal,
                "host": user.host,
                "login_time": datetime.fromtimestamp(user.started).isoformat(),
                "pid": user.pid,
            }
        )

    return users
