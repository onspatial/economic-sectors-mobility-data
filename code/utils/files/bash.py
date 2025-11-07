
import utils.files.path as file_path    
import os
def save_run_paths_to_file(run_paths, file, parallel=8):
    tracker=0
    with open(file, 'w') as f:
        for line in run_paths:
            tracker+=1
            folder = ('/').join(line.split('/')[0:-1])
            run_sh = line.split('/')[-1]
            f.write(f'cd {folder}\n')
            f.write(f'echo "Processing {folder}"\n')
            f.write(f'touch run.lock\n')
            f.write(f'bash {run_sh} >run.log.txt 2>&1 && touch run.unlock & \n')
            f.write(f'cd {file_path.get_project_path()}\n')
            if tracker%parallel==0:
                f.write(f'echo waiting for {parallel} to finish\n')
                f.write(f'wait\n')
            f.write('\n')
        f.write(f'wait\n')
        f.write(f'shutdown -h now\n')

def run_command(command):
    os.system(command)
