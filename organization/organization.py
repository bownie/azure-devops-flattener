

class Organization:
    org_name: str

    def __init__(self, name):
        self.org_name = name

    def get_name(self) -> str:
        return self.org_name
