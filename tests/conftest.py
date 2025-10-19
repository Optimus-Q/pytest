import sys
import pytest
from pathlib import Path

root_dir = Path(__file__).resolve().parents[1]
src_path = root_dir / 'src'

if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


@pytest.fixture()
def add_value():
    return {"summary":"pytesting", "owner":"roy", "id":1}

@pytest.fixture()
def add_list(add_value):
    return [add_value, {"summary":"pytng", "oer":"ry", "id":10}]


#tasks_to = [{"name": "roy"}] # this iterates over tasks to so, first iter: {"name": "roy"}
#tasks_to = {"name": "roy"} # this iterates over tasks_to so it is over items for x in tasks_to
#tasks_to = {"name": "roy"} # this iterates over tasks_to.values() so it is over values for x in tasks_to.values()
tasks_to = [{"name": "roy"}]
@pytest.fixture(params = tasks_to)
def get_id_name(request):
    return request.param



