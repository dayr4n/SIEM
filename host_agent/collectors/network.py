import psutil


def get_connections_network():
    connections = []
    for conn in psutil.net_connections(kind="tcp"):
        connection = {
            "pid": conn.pid,
            "status": conn.status,
            "family": conn.family.name,
            "type": conn.type.name,
            "local_ip": conn.laddr.ip if conn.laddr else None,
            "local_port": conn.laddr.port if conn.laddr else None,
            "remote_ip": conn.raddr.ip if conn.raddr else None,
            "remote_port": conn.raddr.port if conn.raddr else None,
        }
        connections.append(connection)
    return connections


def get_if_network():
    iif = psutil.net_if_addrs()
    interfaces = []

    for name, addresses in iif.items():
        interface = {"name": name, "addresses": []}

        for addr in addresses:
            interface["addresses"].append(
                {
                    "address": addr.address,
                    "family": addr.family.name,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast,
                    "version": (
                        "ipv4"
                        if addr.family.name == "AF_INET"
                        else (
                            "ipv6"
                            if addr.family.name == "AF_INET6"
                            else "mac" if addr.family.name == "AF_PACKET" else None
                        )
                    ),
                }
            )

        interfaces.append(interface)

    return interfaces


def get_ifstats_network():
    ifstats = []
    stats = psutil.net_if_stats()

    for name, stat in stats.items():
        ifstats.append(
            {
                "name": name,
                "status": {
                    "is_up": stat.isup,
                    "duplex": stat.duplex,
                    "speed": stat.speed,
                    "mtu": stat.mtu,
                    "flags": stat.flags.split(","),
                },
            }
        )

    return ifstats


def get_iocounters_network():
    ifcounter = []
    counter = psutil.net_io_counters(pernic=True)
    for name, count in counter.items():
        ifcounter.append(
            {
                "name": name,
                "counters": {
                    "bytes_sent": count.bytes_sent,
                    "bytes_recv": count.bytes_recv,
                    "packets_sent": count.packets_sent,
                    "packets_recv": count.packets_recv,
                    "errin": count.errin,
                    "errout": count.errout,
                    "dropin": count.dropin,
                    "dropout": count.dropout,
                },
            }
        )
    return ifcounter


def get_summary_network():
    return {
        "interfaces": get_if_network(),
        "stats": get_ifstats_network(),
        "counters": get_iocounters_network(),
        "connections": get_connections_network(),
    }
