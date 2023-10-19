# Part of Business P9.24:
# Test program for the Message class:

def message_test():
    from message import Message
    import argparse
    import textwrap
    parser = argparse.ArgumentParser(prog = "Customer test program", 
                                    formatter_class = argparse.RawDescriptionHelpFormatter, 
                                    description = textwrap.dedent('''\
                                                Message
                                    --------------------------------
                                    A simulated message between two people. The class also hold history about number of messages\n
                                    and a log of all messages sent.
                                    
                                    Methods:
                                    1) append: 
                                    @param new_text the new string/text that the sender sends to the recipent.
                                    
                                    2) log_messages: updates the number of messages sent, and adds the message to the log.

                                    3) toString(): prints sender, recipent and the message body
                                    '''),
                                    epilog=textwrap.dedent('''\
                                                Usage
                                    --------------------------------
                                    m = Message("Bob", "Simon")                     # Initialize a Message object
                                    print(m.toString())                             # print the message with the sender and recipent
                                    m.append("Hello Mister, how ya doin?")          # Append a text to the message
                                    print(m.toString())                             # print the message with the sender and recipent
                                    m.append("Also how the dating life going?")     # Append a text to the message
                                    print(m.toString())                             # print the message with the sender and recipent
                                    print(Message._no_messages)                     # prints the number of messages                
                                    print(Message._log)                             # prints a dictionary with all the senders as keys, alle the recievers as value, but also a key to the message sent. 
                                    '''))
    parser.add_argument('--run_test', action='store_true', help='runs Message test')

    args = parser.parse_args()

    if args.run_test:
        m = Message("Bob", "Simon")
        print(m.toString())
        m.append("Hello Mister, how ya doin?")
        print()
        print(m.toString())
        m.append("Also how the dating life going?")
        print()
        print(m.toString())

        print()
        print(Message._no_messages)
        print("Expected: 2")
        print()
        print(Message._log)
        print("Expected: {'Bob': {'Simon': 'Hello Mister, how ya doin?\nAlso how the dating life going?'}")

if __name__ == '__main__':
 message_test()