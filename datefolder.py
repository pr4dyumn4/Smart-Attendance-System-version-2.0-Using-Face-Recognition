from datetime import datetime
import os
def create_folder():
    today = datetime.now()
    a = "./captures/" 
    os.makedirs(a, exist_ok=True)
    b = today.strftime('%d%m%Y')+' - '+today.strftime('%H %M')
    c = os.listdir(a)
    if b in c:
        pass
    else:
        os.mkdir(a + b)
