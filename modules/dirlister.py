import os

def run(**args):
    print("[*] Dans le module de la liste de diffusion")
    file = os.listdir(".")
    return str(file)