import os
import json

DEFAULT_FILE_NAME = "service-search.ini"
DEFAULT_FILE_CONTENT = {
	"core" : {
		"networkMask" : "192.168.0.X",
		"startIP" : 0,
		"serviceName" : "service"
	}
}

def load_config(config_file = DEFAULT_FILE_NAME):
	if not os.path.exists(config_file):
		file = open(config_file, "xt")
		file.writelines(json.dumps(DEFAULT_FILE_CONTENT, indent=2))
	file = open(config_file, "rt")
	conf = json.load(file)
	return conf