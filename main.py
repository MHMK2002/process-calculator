import psutil

sum_vms = 0;
for proc in psutil.process_iter():
    try:
        # Fetch process details as dict
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
        pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
        sum_vms += pinfo['vms']
        # Append dict to list
        print(pinfo)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print(f'Sum of vms: {sum_vms} MB')
