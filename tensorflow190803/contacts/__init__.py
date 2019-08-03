from contacts.controller import ContactsController

if __name__ == '__main__':
        ctrl = ContactsController()
        name = input('이름')
        phone = input('전화번호')
        addr = input('주소')
        email = input('이메일')

        print('이름 : %s' %name)
        print('전화번호 : %s' % phone)
        print('주소 : %s' % addr)
        print('이메일 : %s' % email)