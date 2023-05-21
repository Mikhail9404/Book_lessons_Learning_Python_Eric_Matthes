def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message.title())
        sent_messages.append(current_message)



messages = ['cuca coorage', 'haloo hitara', 'shalom', 'gangbang']
sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

