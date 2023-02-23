"""
tools.

path
"""

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__.replace(".", "-"))


from ansys.tools.path.path import (
    SUPPORTED_ANSYS_VERSIONS,
    find_ansys,
    change_default_ansys_path,
    save_ansys_path,
    get_ansys_path,
    get_available_ansys_installations,
)
