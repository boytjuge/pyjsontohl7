import json

def create_hl7_from_json(json_data):
    hl7_message = ""

    # Create the MSH segment
    msh_segment = "MSH|^~\&|SenderApp|SenderFacility|ReceiverApp|ReceiverFacility|{timestamp}||ADT^A04|{message_control_id}|P|2.4"
    timestamp = "20230624120000"  # Replace with the actual timestamp
    message_control_id = "123456789"  # Replace with the actual message control ID
    msh_segment = msh_segment.format(timestamp=timestamp, message_control_id=message_control_id)
    hl7_message += msh_segment + "\r"

    # Create the PID segment
    pid_segment = "PID|||{patient_id}||{patient_name}||{birth_date}|{gender}|^{hn}"
    patient_id = json_data["patient_id"]  # Replace with the actual field name in your JSON data
    patient_name = json_data["patient_name"]  # Replace with the actual field name in your JSON data
    birth_date = json_data["birth_date"]  # Replace with the actual field name in your JSON data
    gender = json_data["gender"]  # Replace with the actual field name in your JSON data
    hn = json_data["hn"]
    pid_segment = pid_segment.format(patient_id=patient_id, patient_name=patient_name, birth_date=birth_date, gender=gender,hn=hn)
    hl7_message += pid_segment + "\n"

    # Add more segments and fields as needed, following the HL7 message structure

    return hl7_message

# Sample JSON data
json_data = [{
    "patient_id": "12345",
    "patient_name": "FSS DF",
    "birth_date": "19800101",
    "gender": "M",
    "hn":"36-15-005544"
},{
    "patient_id": "12345",
    "patient_name": "DFSS daw",
    "birth_date": "19800110",
    "gender": "M",
    "hn":"36-15-005512"
},]

# Create HL7 message from JSON data
hl7_message = ""
for i in range(len(json_data)):
    hl7_message +=create_hl7_from_json(json_data[i])

print(hl7_message)
    