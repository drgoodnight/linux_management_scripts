import os
import datetime

# Set up the command and log file paths
command = '/path/to/ord wallet inscriptions >> log.txt'
log_file = 'log.txt'

# Write out the cronjob to a temporary file
cronjob = f'0 */2 * * * {command}\n'
with open('/tmp/crontab.txt', 'w') as f:
    f.write(cronjob)

# Install the cronjob
os.system('crontab /tmp/crontab.txt')

# Create the log file if it doesn't exist
if not os.path.exists(log_file):
    open(log_file, 'w').close()

# Append a timestamp to the log file each time the command is executed
with open(log_file, 'a') as f:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f'Command executed at {timestamp}\n')
