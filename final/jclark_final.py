# CMSY-156
# Programmer name: Joseph Clark 
# 02/28/22 
# Final Project: IP Log parsing

# IP prefixes from OUCH
BAD_IP_PREFIXES = [
  "168.193",
  "224.174",
  "233.012"
]

def main():
  # Prompt the user for a filename and attempt to open it continuously until a valid filename is entered 
  while True:
    filename = input("Enter the path to the IP log: ")
    try:
        ip_log = open(filename, "r")
        break
    except Exception as e:
        print(f"Error opening IP log {filename}. Please try again")
  
  # Prompt the user for an output filename and attempt to open it for writing until a valid filename is entered
  while True:
    filename = input("Enter the path for the output report: ")
    try:
        output_file = open(filename, "x")
        break
    except:
        print(f"Error opening file {filename} for writing. Please try again")

  # Count the number of IPs and specifically bad IPs in the file
  total_records = 0
  total_bad_records = 0
  bad_ips = []

  for line in ip_log:
    total_records += 1
    # Prefix is only 6 characters
    ip_prefix = line[:7]
    # Check if the prefix is in the list of bad prefixes
    if ip_prefix in BAD_IP_PREFIXES:
      # Store entire bad IP record in a list
      bad_ips.append(line)
      # Count bad IPs
      total_bad_records += 1
  
  # Close the IP log file because we're done with it
  ip_log.close()

  # Write the output file
  write_output_file(total_records, bad_ips, output_file)

  print("Program Complete!")

# Writes the output report file
def write_output_file(total_records, bad_ips, output_file):
  # Report header
  output_file.writelines("""
Output Report
-------------
""")

  # Report statistics
  output_file.writelines("The total number of records in the files is: " + str(total_records) + "\n")
  output_file.writelines("The number of suspect IP addresses is: " + str(len(bad_ips)) + "\n")
  output_file.writelines("The percentage of suspect IP addresses is: " + f"{len(bad_ips) / total_records * 100:.2f}" + "\n\n")

  output_file.writelines("""
Suspect IP Addresses
--------------------
""")

  # Sort the bad IPs by IP address
  bad_ips.sort()

  # List of bad IPs
  for record in bad_ips:
    ip = record[:14]
    date = record[14:]
    output_file.writelines("IP address = " + ip + " Date and Time = " + date + "\n")
  
  # Close the output file
  output_file.close()

main()