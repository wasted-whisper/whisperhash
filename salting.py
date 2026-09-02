import subprocess
from encryption_engine import EncryptionEngine

salt=lambda : subprocess.call("./shellcode/salt.sh",shell=True)

slt=salt()

def salting(message):
    ...

def counter(message,rails,offset,direction):
    ...

def state_operation(message,rails,offset,direction):
    ...