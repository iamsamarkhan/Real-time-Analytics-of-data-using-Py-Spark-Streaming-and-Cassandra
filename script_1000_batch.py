import os
import time
import csv

# Open the log file
log_file_path = "./2021-10-31.csv"
log_file = open(log_file_path, "r")
csv_reader = csv.reader(log_file)

# Set up the output directory
output_dir = "./streaming/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the header for the output files
header = next(csv_reader)

# Initialize the line count
line_count = 0
file_count = 1
# Loop through the log file
while True:
    # Check if there are still lines to read
    try:
        next(csv_reader)
    except StopIteration:
        break
        
    # Read the next 1000 lines
    lines = [header] + [next(csv_reader) for i in range(999)]
    
    # Update the line count
    line_count += len(lines)
    
    # Write the lines to a new file
    #output_file_path = os.path.join(output_dir, f"log{}".format(line_count).csv)
    output_file_path = os.path.join(output_dir, f"log{file_count}.csv")
    with open(output_file_path, "w", newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(lines)
    file_count += 1
    # Wait for 3 seconds
    time.sleep(3)

# Close the log file
log_file.close()

