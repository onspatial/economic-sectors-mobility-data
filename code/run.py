import os

file_name = "data"
in_parallel = 4
os.system(f'echo "#!/bin/bash" > {file_name}.sh')
for division in ["us", "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9"] + ["ak", "al", "ar", "az", "ca", "co", "ct", "dc", "de", "fl"]:
    for i in range(1, in_parallel):
        os.system(f'echo "python code/{file_name}.py {i} {in_parallel} {division} &" >> {file_name}.sh')
    os.system(f'echo "wait" >> {file_name}.sh')
    os.system(f'echo "python code/{file_name}.py 0 0 {division}" >> {file_name}.sh')
