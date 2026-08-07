from server.core.finding import Finding

class ProcessesRuler:
    def __init__(self):
        pass

    def find(self, ip, severity, title, description):
        return Finding(
                ip=ip,
                severity=severity,
                title=title,
                description=description
            )

    def check(self, ip, process):
        fprocesses = process["file_processes"]
        processes = process["processes"]
        ROOT_WHITELIST = {
            "systemd",
            "dbus-broker",
            "NetworkManager",
            "sshd",
            "tailscaled",
            "dockerd",
            "containerd",
            "chronyd",
            "polkitd",
            "systemd-journald",
            "systemd-logind",
            "systemd-udevd",
            }
        findings = []
        for p in processes :
            if "/tmp" or "/dev/shm" or "/var/tmp" in p["exe"] :
                findings.append(
                    self.find(
                        ip,
                        "WARNING",
                        "Process being exec in danger zone",
                        f"The process {p['name']} it's being executed in {p['exe']}."
                        )
                    )
            if not p["exe"] :
                findings.append(
                    self.find(
                        ip,
                        "WARNING",
                        "Process is destroying itself , it has no path",
                        f"The process {p['name']} and doesn't have path ."
                        )
                    )
            if p["uids"][1] == 0 and p["name"] not in ROOT_WHITELIST:
                findings.append(
                    self.find(
                        ip,
                        "ADVICE",
                        f"Process running as root {p['name']}"
                    )
                )
        return findings
        
            
                

        # I have to think about how to itarate all this info ...