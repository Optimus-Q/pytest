import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parents[1]
src_path = root_dir / 'src'

if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))