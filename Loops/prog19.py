import subprocess

commands = [
    "uptime",
    "df -h",
    "free -m",
    "systemctl status docker --no-pager"
]

for cmd in commands:
    print(f"\n▶ Running: {cmd}")
    subprocess.run(cmd, shell=True)
