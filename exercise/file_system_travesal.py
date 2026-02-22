import os

def find_large_files(directory, min_size_mb):
    """
    Traverse directory tree and return a list of absolute file paths
    larger than min_size_mb.
    """
    large_files = []
    
    # Convert MB to bytes
    min_size_bytes = min_size_mb * 1024 * 1024
    
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            
            try:
                file_size = os.path.getsize(full_path)
                
                if file_size > min_size_bytes:
                    large_files.append(os.path.abspath(full_path))
                    
            except (OSError, FileNotFoundError):
                # Skip files that cannot be accessed
                continue
    
    return large_files
