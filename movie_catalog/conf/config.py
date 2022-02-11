import os
import yaml

config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(config_path, "r") as stream:
    config = yaml.safe_load(stream)

db_config = config["postgre_db"]
django_config = config["django_config"]
