# FILE NAME - firewall_traffic_analyzer.py

# NAME: William Storrs
# DATE: February 16, 2026
# BRIEF DESCRIPTION:  Firewall Traffic Analyzer



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print("=== Network Traffic Security Analyzer ===\n")

# Inputs
port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
size = float(input("Enter the data transfer size in megabytes (MB): "))

# Risk Logic
# Assumptions
# - 80 = HTTP (unencrypted)
# - 443 = HTTPS (encrypted)
# - 22 = SSH (generally encrypted)
# - 3389 = RDP (can be risk if exposed)

port = int(input("Enter the port number (e.g. 80, 22, 443, 3389): "))
data_size = int(input("Enter data transfer size in megabytes (MB): "))

# Check for HIGH RISK ports (remote access)
if port == 22 or port == 3389:
    risk = "HIGH RISK: Potential unauthorized remote access detected!"
# Check for LOW RISK ports (secure/encrypted)
elif port == 443:
    risk = "LOW RISK: Secure encrypted transfer detected."
# Check for MEDIUM RISK ports (unencrypted data transfer)
elif port == 80:
    if data_size > 100:
        risk = "MEDIUM RISK: Large unencrypted data transfer detected."
    else:
        risk = "LOW RISK: Secure encrypted transfer detected."
# Unknown port
else:
    risk = "UNKNOWN: Unrecognized traffic pattern."

print(f"Risk Assessment: {risk}")

# Output
print("\nFIREWALL LOG:")
print(f"Port: {port}, Transfer Size: {size:g} MB")
print(f"Risk Assessment: {risk}")
print("-" * 25)



########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 1200

FIREWALL LOG:
Port: 22, Transfer Size: 1200 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?

I did not. 


'''
