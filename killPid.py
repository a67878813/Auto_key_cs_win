import psutil
p = psutil.Process(14044)
print(p)
print(p.cpu_times())

print(p.memory_info())
#print(p.open_files())
#print(p.connections())
#logging.info(f'kill pid={pid},name={p.name()} ')
print('------')

#kill
p.terminate()