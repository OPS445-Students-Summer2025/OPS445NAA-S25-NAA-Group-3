#!/usr/bin/env python3

import subprocess
def get_uptime():
	#Returns system uptime as a string
	result = subprocess.run(["uptime", "-p"], stdout=subprocess.PIPE, text=True)
	return result.stdout.strip()
if __name__ == "__main__":
	print("Uptime:", get_uptime())
