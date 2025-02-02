from datetime import datetime


def gerador_log(funcao):
    def envelope(*args, **kwargs):
        obj = funcao(*args, **kwargs)
        try:
            with open("log.txt", "a") as arquivo:
                arquivo.write(f"\n{datetime.now()} - {funcao.__name__} - {obj}")
        except FileNotFoundError:
            with open("log.txt", "w") as arquivo:
                arquivo.write(f"\n{datetime.now()} - {funcao.__name__} - {obj}")

        return obj
        
    return envelope

