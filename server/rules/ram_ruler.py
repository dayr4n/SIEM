from server.core.finding import Finding

class RAMRuler :
    def __init__(self):
        pass
    def find(self, ip, severity, title, description):
        return Finding(
                ip=ip,
                severity=severity,
                title=title,
                description=description
            )



    def check(self, ip, ram):
        findings = []
        vm = ram["virtual_memory"]
        usage = vm["percent"]
        status = vm["status"]
        total = vm["total"]

        #ratios 
        used_ratio = vm["used"] / total
        available_ratio = vm["available"] / total
        free_ratio = vm["free"] / total
        cached_ratio = vm["cached"] / total
        active_ratio = vm["active"] / total
        inactive_ratio = vm["inactive"] / total
        shared_ratio = vm["shared"] / total
        #FOR THIS TWO WE HAVE TO GET SNAPSHOTS IN TIME TO COMPARE HIS DIFERENTT VERSION LET'S WAIT FOR OTHER TIME TO DO IT .
        slab_ratio = vm["slab"] / total
        buffers_ratio = vm["buffers"] /total

        if used_ratio > 0.95:
            findings.append(self.find(ip, "CRITICAL", "RAM overused", f"The RAM is full {used_ratio}"))
        elif used_ratio > 0.80:
            findings.append(self.find(ip, "HIGH", "RAM high used", f"The RAM it's high used {used_ratio}"))
        elif used_ratio > 0.70:
            findings.append(self.find(ip, "HIGH", "RAM medium used", f"The RAM it's medium used {used_ratio}"))

            
        if available_ratio < 0.05:
            findings.append(self.find(ip,"CRITICAL","High memory utilisation",f"Memory usage is {used_ratio:.1%} "f"({ram["virtual_memory"]["used"]} bytes used of {ram["virtual_memory"]["total"]} bytes)."))
        elif available_ratio < 0.10:
            findings.append(self.find(ip,"HIGH","High memory utilisation",f"Memory usage is {used_ratio:.1%} "f"({ram["virtual_memory"]["used"]} bytes used of {ram["virtual_memory"]["total"]} bytes)."))

        if cached_ratio < 0.01:
            print("Memory cached")

        if active_ratio > 0.80:
            findings.append(self.find(ip,"WARNING","High percent of memory is cached",f"Memory active is {active_ratio:.1%} "f"({ram["virtual_memory"]["used"]} bytes used of {ram["virtual_memory"]["total"]} bytes)."))

        if inactive_ratio < 0.02 and used_ratio > 0.90:
            findings.append(self.find(ip,"WARNING","Low reclaimable memory",f"RAM usage is {used_ratio:.1%} and inactive memory is only {inactive_ratio:.1%}. ""Little reclaimable memory remains."))

        if shared_ratio > 0.20:
            findings.append(self.find(ip,"WARNING","High shared memory",f"RAM shared is {shared_ratio:.1%} and used memory is  {used_ratio:.1%}. "))

        return findings
