import messages_functions as mf

new_messages = ['Hello!', 'How are you?', 'Hello World!']
sent_messages = []

mf.send_messages(new_messages, sent_messages)
mf.show_messages(sent_messages)
print(new_messages)
print(sent_messages)