import psutil
import json 

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_cores():
    return {"physical": psutil.cpu_count(logical=False), 
            "logical": psutil.cpu_count(logical=True)}

def get_cpu_frequency():
    freq = psutil.cpu_freq()
    return {
        'current': freq.current,
        'min': freq.min,
        'max': freq.max
    } if freq else None

def get_load_average():
    return psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None

def get_cpu_stats():
    stats = psutil.cpu_stats()
    return {
        'ctx_switches': stats.ctx_switches,
        'interrupts': stats.interrupts,
        'soft_interrupts': stats.soft_interrupts,
        'syscalls': stats.syscalls
    }
    
def get_cpu_usage_per_core():
    return psutil.cpu_percent(interval=1, percpu=True)
    
def get_cpu_times():
    times = psutil.cpu_times()
    return {
        'user': times.user,
        'system': times.system,
        'idle': times.idle,
        'nice': getattr(times, 'nice', None),
        'iowait': getattr(times, 'iowait', None),
        'irq': getattr(times, 'irq', None),
        'softirq': getattr(times, 'softirq', None),
        'steal': getattr(times, 'steal', None),
        'guest': getattr(times, 'guest', None),
        'guest_nice': getattr(times, 'guest_nice', None)
    }
    
def get_cpu_info():
    return {
        'usage': get_cpu_usage(),
        'cores': get_cpu_cores(),
        'frequency': get_cpu_frequency(),
        'load_average': get_load_average(),
        'stats': get_cpu_stats(),
        'times': get_cpu_times(),
        "usage_per_core": get_cpu_usage_per_core()
    }
#important cpu but in json format
def get_cpu_info_json():
    return json.dumps(get_cpu_info(), indent=4)