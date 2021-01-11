
import os

def get_resource_path(resource):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resources/' + resource)

