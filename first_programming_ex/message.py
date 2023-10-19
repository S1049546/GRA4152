# First programming exercise:
# Task Business P9.24:

# # A class that simulates a message between two people.
#
class Message:
    # # Class variables that represents the total number of messages sent, and the log of all messages sent.
    #
    _no_messages = 0
    _log = {}

    # # Constructor that initiatez a Message object. Takes in the sender and recipent
    #
    def __init__(self, sender, reciever):
        self._sender = sender
        self._reciever = reciever
        self._text = ""
        
    # # adds a message/tekst to the message string
    # @param new_text the new string that is added
    def append(self, new_tekst):
        if len(self._text) == 0:
            self._text = new_tekst
        else:
            self._text = self._text + "\n" + new_tekst
        self.log_messages()

    
    # # Returns the sender, recipent and message
    # return String with sender, redipent and message
    def toString(self):
        if len(self._text) == 0:
            return f"From {self._sender}\nTo: {self._reciever}"
        else:
            return f"From {self._sender}\nTo: {self._reciever}\n{self._text}"
     

    # # Method that updates the class variables _log and _no_messages
    #
    def log_messages(self):
        Message._no_messages += 1
        Message._log[self._sender] = {self._reciever : self._text}