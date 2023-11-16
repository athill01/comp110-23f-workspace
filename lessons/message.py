"""Class to store a message (operator overload, union types, default parameters)"""

from typing import Union

class Email:

    to: str 
    message: str
    flag: bool

    def __init__(self, recipient: str, message: str = "", importance_flag: bool = False):
        """Constructor of an email."""
        self.to = recipient
        self.message = message
        self.flag = importance_flag

    def __str__(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.flag} \n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int):
        self.message *= factor
    
email_to_chiara: Email = Email("chiara", "You're a great TA! ", False)
email_to_chiara * 100
print(email_to_chiara)
email_to_lauren: Email = Email("lauren")
print(email_to_lauren)