# Example content for from_root.py
import os
import sys

# Define the project root based on the location of this file
# Adjust if this file is placed somewhere other than the direct root
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def from_root(*path_segments):
    """
    Constructs an absolute path from the project root.
    Args:
        *path_segments: Variable number of path components (strings).
    Returns:
        Absolute path string.
    """
    return os.path.join(PROJECT_ROOT, *path_segments)

# You might also need to add the project root to sys.path sometimes,
# though direct imports from files in the root usually work if run from root.
# sys.path.insert(0, PROJECT_ROOT) # Uncomment if needed, but often not necessary