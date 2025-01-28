from datetime import datetime

def gerador_log(funcao):
    def envelope(*args, **kwargs):
        obj = funcao(*args, **kwargs)
        print(f"{datetime.now()} - {funcao.__name__} - {obj}")
        return obj
        
    return envelope