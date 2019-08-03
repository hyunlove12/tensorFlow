class ContactsModel:
    def __init__(self, name, phone, addr, email):
        self.name_ = name
        self.phone_ = phone
        self.addr_ = addr
        self.email_ = email

    def set_contact(self, name, phone, addr, email):
        contact = ContactsModel(name, phone, addr, email)
        return contact

    def print_info(self):
        str = '이름 : {} \n 전화번호 : {} \n 주소 : {} \n 이메일 : {} '\
                .format(self.name, self.phone, self.email, self.addr)
    def get_contacts(self):
        for i in list:
            print(i.print_info)

