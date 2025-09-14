class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def __repr__(self):
        return f"<Member {self.name} ({self.member_id})>"
