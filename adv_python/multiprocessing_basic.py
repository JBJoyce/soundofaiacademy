import multiprocessing
import json
from pathlib import Path
from typing import Dict

def create_json(input: Dict[str, str], root: Path, i:int) -> None:
    with open(file=root / f'frodo_{i}.json', mode='w') as file:
        json.dump(input, file)

if __name__ == "__main__":
    
    hobbit_dict = {"name": "Frodo", "last_name": "Baggins"}
    p = Path('/home/jbjoyce/soundofaiacademy/adv_python/data')
    
    process_1 = multiprocessing.Process(target=create_json, args=[hobbit_dict, p, 1], daemon=True)
    process_2 = multiprocessing.Process(target=create_json, args=[hobbit_dict, p, 2], daemon=True)
    
    process_1.start()
    process_2.start()    
    
    process_1.join()
    process_2.join()
            