# exercise 8-9-10-11
messages = ['hello world','do not call me', 'good bye']

def show_messages(list):
    """print messages in a list"""
    for message in messages:
        print(message)

show_messages(messages)

def sending_messages(messages,sent_message):
    """print a message and stoee the sent message in a separate list"""
    while messages:
        current_message= messages.pop()
        print(current_message)
        sent_message.append(current_message)

already_sent_message= []

message_list = ['hi there','whatssup', 'miss you']
sending_messages(message_list[:],already_sent_message)

print(already_sent_message)
print(message_list)
