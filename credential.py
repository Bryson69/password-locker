class Credential:
    """
    a class that generates new credential for users 
    """
    pass
    credentials_array = []

    def __init__(self,user_name,password,email):
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credential(self):
        """
        save_contact method saves credential object into credential array
        """

        Credential.credentials_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credentialarray
        """

        return cls.credentials_array