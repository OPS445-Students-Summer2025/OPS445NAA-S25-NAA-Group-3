#!/usr/bin/env python3
# Author: ssuresh14
# Description: Displays current CPU usage as a percentage

import subprocess

def get_cpu_usage():
    """Returns CPU usage as a float percentage (100 - idle%)."""
    try:
        # Use top command to get CPU stats
        cmd = "top -bn1 | grep '%Cpu'"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()

        if error:
            return "Error: Unable to retrieve CPU info"

        line = output.decode('utf-8').strip()
        # Example line: "%Cpu(s):  7.3 us,  2.0 sy,  0.0 ni, 89.9 id, ..."
        parts = line.split(',')

        for part in parts:
            if 'id' in part:
                idle_str = part.strip().split(' ')[0]
                idle = float(idle_str)
                usage = 100.0 - idle
                return round(usage, 1)
        return "Error: Could not parse CPU usage"
    except Exception as e:
        return f"Exception occurred: {e}"

# Main block to run the function
if __name__ == '__main__':
    cpu_percent = get_cpu_usage()
    print(f"CPU Usage: {cpu_percent}%")