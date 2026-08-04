from server.core.finding import Finding


class CPURuler:

    def __init__(self):
        pass

    def check(self, ip, cpu):
        findings = {}
        current = cpu["frequency"]["current"]
        maximum = cpu["frequency"]["max"]
        usage = cpu["usage"]
        cores = len(cpu["usage_per_core"])
        load_15min = cpu["load_average"]["2"]
        ratio = current / maximum
        steal = cpu["times"]["steal"]
        if usage > 80 and ratio < 0.6:
            findings.append(Finding(
                ip=ip,
                severity="critical",
                title="CPU Overworking detected",
                description=(
                    f"CPU usage is {usage}% but frequency is "
                    f"{current}MHz/{maximum}MHz"
                )
            ))
        if load_15min > cores :
            findings.append(Finding(
            ip=ip,
            severity="warning",
            title="High CPU load",
            description=(
                f"Load average {load_15min} "
                f"is higher than CPU cores {cores}"
            )
        ))

        if steal > 30:
                findings.append(Finding(
                        ip=ip,
                        severity="warning",
                        title="High CPU steal",
                        description=(f"Your steal CPU is {steal}%")
                    ))
        return findings
        
#It's pendent to do the usage per core alert also the times alert ...