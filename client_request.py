import os
import subprocess

cmd = "aws ecs list-tasks --cluster VOC-Automation-Cluster"
cmd1 = "Dir"
#result = os.system(cmd)
result = subprocess.check_output(cmd1, shell=True)
#taskid = result['taskArns'][0][40:]
print(result)