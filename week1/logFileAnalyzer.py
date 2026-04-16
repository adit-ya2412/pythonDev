with open("logs.txt","r") as file:
    lines=file.readlines()

total_lines=len(lines)
warning_messages_count=0
info_messages_count=0
error_message_count=0
unknown_message_count=0
error_messages=[]
logs={
    "INFO":[],
    "WARNING":[],
    "ERROR":[],
    "UNKNOWN":[]
}
for line in lines:
    if "ERROR" in line:
        error_message_count+=1
        _,message=line.split(":",1)
        logs["ERROR"].append(message.strip())
    elif "INFO" in line:
        info_messages_count+=1
        _,message=line.split(":",1)
        logs["INFO"].append(message.strip())

    elif "WARNING" in line:
        warning_messages_count+=1
        _,message=line.split(":",1)
        logs["WARNING"].append(message.strip())
    else:
        unknown_message_count+=1
        logs["UNKNOWN"].append(message.strip())
log_counts={
    "INFO":info_messages_count,
    "WARNING":warning_messages_count,
    "ERROR":error_message_count,
    "UNKNOWN":unknown_message_count
}

most_frequent_log_type=max(log_counts,key=log_counts.get)

print(total_lines)
print(f"Most frequent in logs :{most_frequent_log_type}")
print(f"Info message count {info_messages_count}")
print(f"Warning message count {warning_messages_count}")
print(f"Unknown Error count is {unknown_message_count}")
print(f"Error messages count is {len(error_messages)}")

for key,value in logs.items():
    print(f" \n {key}")
    for v in value:
        print(f"- {v}")
    