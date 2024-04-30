def send_messages(new_messages, sent_messages):
    """simulate sending messages"""
    while new_messages:
        sent_message = new_messages.pop()
        sent_messages.append(sent_message)

def show_messages(sent_messages):
    """Print out messages"""
    for sent_message in sent_messages:
        print(f'User said "{sent_message}"')