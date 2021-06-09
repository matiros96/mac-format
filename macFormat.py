import sys
# passing args
first_arg=sys.argv[1]
second_arg=sys.argv[2]

mac_not_formated = first_arg

mac_sanitized = ''.join(filter(str.isalnum, mac_not_formated)) #remove all non-alpanumerical

# formating pre for xxxx-xxxx format
first_four_chars = mac_sanitized[:4]
middle_four_chars = mac_sanitized[4:8]
last_four_chars = mac_sanitized[8:]

# formating pre for xx:xx format
first_two = mac_sanitized[:2]
second_two = mac_sanitized[2:4]
third_two = mac_sanitized[4:6]
fourth_two = mac_sanitized[6:8]
fifth_two = mac_sanitized[8:10]
sixth_two = mac_sanitized[10:]

choice = int(second_arg)
if choice == 1:
    print(mac_sanitized)
elif choice == 2:
    print(f"{first_four_chars}-{middle_four_chars}-{last_four_chars}") #formatting x
elif choice == 3:
    print(f"{first_two}:{second_two}:{third_two}:{fourth_two}:{fifth_two}:{sixth_two}") #
else:
    ("error")
