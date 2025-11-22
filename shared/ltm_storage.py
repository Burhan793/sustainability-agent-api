"""
Long-Term Memory (LTM) storage implementation using JSON files.
Provides persistent storage for agent responses and learning.
"""

import json
import os
from typing import Any, Optional
from datetime import datetime
import hashlib


class LTMStorage:
    """
    JSON-based Long-Term Memory storage.
    Stores successful responses for quick retrieval and learning.
    """
    
    def __init__(self, storage_path: str):
        """
        Initialize LTM storage.
        
        Args:
            storage_path: Directory path where LTM files will be stored
        """
        self.storage_path = storage_path
        self.memory_file = os.path.join(storage_path, "memory.json")
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Create storage directory and file if they don't exist."""
        os.makedirs(self.storage_path, exist_ok=True)
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, 'w') as f:
                json.dump({}, f)
    
    def _generate_key(self, query: str) -> str:
        """
        Generate a hash key from the query for storage.
        
        Args:
            query: The user query
            
        Returns:
            Hash key for the query
        """
        return hashlib.md5(query.lower().strip().encode()).hexdigest()
    
    def write(self, key: str, value: Any) -> bool:
        """
        Write a key-value pair to LTM.
        
        Args:
            key: Storage key
            value: Value to store
            
        Returns:
            True on success, False otherwise
        """
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
            
            memory[key] = {
                "value": value,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "access_count": 0
            }
            
            with open(self.memory_file, 'w') as f:
                json.dump(memory, f, indent=2)
            
            return True
        except Exception as e:
            print(f"[LTM] Error writing to memory: {e}")
            return False
    
    def read(self, key: str) -> Optional[Any]:
        """
        Read a value from LTM.
        
        Args:
            key: Storage key
            
        Returns:
            Stored value or None if not found
        """
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
            
            if key in memory:
                # Update access count
                memory[key]["access_count"] = memory[key].get("access_count", 0) + 1
                memory[key]["last_accessed"] = datetime.utcnow().isoformat() + "Z"
                
                with open(self.memory_file, 'w') as f:
                    json.dump(memory, f, indent=2)
                
                return memory[key]["value"]
            
            return None
        except Exception as e:
            print(f"[LTM] Error reading from memory: {e}")
            return None
    
    def search_similar(self, query: str) -> Optional[Any]:
        """
        Search for similar queries in memory.
        
        Args:
            query: Query to search for
            
        Returns:
            Cached response if found, None otherwise
        """
        key = self._generate_key(query)
        return self.read(key)
    
    def store_response(self, query: str, response: Any) -> bool:
        """
        Store a successful response in LTM.
        
        Args:
            query: The original query
            response: The response to store
            
        Returns:
            True on success, False otherwise
        """
        key = self._generate_key(query)
        return self.write(key, response)
