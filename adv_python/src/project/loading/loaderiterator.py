from pathlib import Path
from typing import List, Dict, Optional, Any

from src.project.loading.serialization import Serializer

class LoaderIterator:
    
    def __init__(self, 
                 serializer: Serializer,
                 num_files_per_iteration: int,
                 load_paths: Optional[List[Path]]) -> None:
        
        self.serializer = serializer
        self.num_files_per_iteration = num_files_per_iteration
        self._load_paths = load_paths
        self._current_iteration = None
    
    ### Loading paths  
    @property
    def load_paths(self) -> Optional[List[Path]]:
        return self._load_paths
    
    @load_paths.setter
    def load_paths(self, load_paths: List[Path]) -> None:
        self._load_paths = load_paths
    
    ### Iteration    
    def __iter__(self):
        self._current_iteration = 0
        return self
    
    def __next__(self) -> List[Dict[Any, Any]]:
        if self._finished_loading():
            raise StopIteration
        data_batch = self._load_data_batch()
        self._current_iteration += 1
        return data_batch
        
    def _finished_loading(self) -> bool:
        if self._current_iteration >= len(self._load_paths) / self.num_files_per_iteration:
            return True
        return False
    
    def _load_data_batch(self) -> List[Dict[Any, Any]]:
        start_index = self._current_iteration * self.num_files_per_iteration
        stop_index = start_index + self.num_files_per_iteration
        return [self.serializer.load(load_path) for load_path in 
                self._load_paths[start_index:stop_index] if load_path.exists()]
        

if __name__ == "__main__":
    li = LoaderIterator(serializer=Serializer, 
                        num_files_per_iteration=8,
                        load_paths=None)
    
    print(li.serializer)        
        
            
            