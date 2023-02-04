import threading
import json
from typing import Dict, List
from pathlib import Path

NUM_FILES = 8
NUM_THREADS = 4
DATA_DIR = Path('/home/jbjoyce/soundofaiacademy/adv_python/data')

def _load_json(load_path: Path) -> Dict:
    #print(f'Thread: {threading.current_thread().name} with Path {load_path}')
    with open(load_path, 'r') as f:
        return json.load(f)

def load_json_list(load_list: List[Path], loaded_list: List[None]) -> None:
    for load_path in load_list:
        loaded_list.append(_load_json(load_path))
        
def create_list_for_threads(dir: Path, num_files: int, num_threads: int) -> List[List[Path]]:
    files_per_thread = int(num_files/num_threads)
    
    flat_list_files = [x for x in dir.iterdir()]
    list_for_threads = [flat_list_files[i:i+files_per_thread] for i in range(0, num_files, files_per_thread)]
    return list_for_threads 


if __name__ == "__main__":
    
    return_list = []
    files_list = create_list_for_threads(DATA_DIR, NUM_FILES, NUM_THREADS)
    
    # Create and start a couple of threads
    threads = []

    for i, files in enumerate(files_list):
        thread = threading.Thread(target=load_json_list, name=f'thread_{i+1}', args=[files, return_list])
        thread.start()
        threads.append(thread)
    
    
    # join threads
    for thread in threads:
        thread.join()
        
    for value in return_list:
        print(value['name'])   
    

