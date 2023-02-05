import multiprocessing
from pathlib import Path

from multiprocessing_basic import create_json

if __name__ == "__main__":
    data = {"name": "Frodo", "last_name": "Baggins"}
    p = Path('/home/jbjoyce/soundofaiacademy/adv_python/data')
    
    pool = multiprocessing.Pool(2)
    pool.starmap(create_json,
                 [(data, p, 1),
                 (data, p, 2)])
    
    pool.close()