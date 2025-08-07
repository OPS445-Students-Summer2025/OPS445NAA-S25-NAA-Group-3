#!/usr/bin/env python3

import os

def get_disk_usage():
    # We’ll collect all the mount points (places where storage is "connected")
    # Start with just the root directory (/) which is always there
    mount_points = ['/']
    
    # We'll store our results here to return at the end
    result = []

    # We use the file /proc/mounts to find all active mount points (like /, /home, /boot, etc.)
    try:
        with open("/proc/mounts", "r") as f:
            for line in f:
                parts = line.split()
                device = parts[0]    # Example: /dev/sda1
                mount_point = parts[1]  # Example: / or /boot

                # Only include real devices (those that start with /dev/)
                if device.startswith("/dev/") and mount_point not in mount_points:
                    mount_points.append(mount_point)
    except:
        # If there's an error reading /proc/mounts, just add a message and return
        result.append("Could not read /proc/mounts")
        return result

    # Now for each mount point, collect disk usage info
    for mount in mount_points:
        try:
            # statvfs gets file system statistics
            stats = os.statvfs(mount)

            # Total blocks * block size = total space in bytes
            total = stats.f_blocks * stats.f_frsize

            # Used space = total - free
            used = (stats.f_blocks - stats.f_bfree) * stats.f_frsize

            # Convert total bytes to gigabytes (GB) using integer division
            total_gb = total // (1024 ** 3)

            # Used percentage = (used space / total space) * 100
            used_percent = (used / total) * 100

            # Add a nicely formatted line to our result
            result.append(f"Mount: {mount} | Total: {total_gb} GB | Used: {used_percent:.2f}%")
        except:
            # If there's a problem reading that mount, we’ll still record it
            result.append(f"Mount: {mount} | Could not get disk usage")

    return result  # Return the final list of results

