import re

MIN_NAME = 0
MAX_NAME = 128
MIN_DOMAIN = 3
MAX_DOMAIN = 256

class EmailChecker:
    def __init__(self, email = ''):
        self.email = email

    def check_domain(self, domain):
        '''
        Checking domain of an E-mail address
        Args:
            domain - string to check
        Return:
            True - if domain format is correct
            False - if domain format is incorrect
        '''
        if len(domain) >= MIN_DOMAIN and len(domain) <= MAX_DOMAIN:
            domain = domain.split('.')
            if len(domain) > 1:
                for sub_domain in domain:
                    if re.search(r'^[-]|[-]$', sub_domain) or \
                    not re.search(r'^[a-z0-9_-]+$', sub_domain):
                        return False
            else:
                return False
        else:
            return False
        return True

    def check_name(self, name):
        '''
        Checking name of an E-mail address
        Args:
            name - string to check
        Return:
            True - if name format is correct
            False - if name format is incorrect
        '''
        if len(name) > MIN_NAME and len(name) <= MAX_NAME:
            if not re.search(r'^[a-z0-9"._!,:-]+$', name):
                return False
            if len(name.split('"')) % 2 == 0:
                return False
            between_quotes = ''.join(name.split('\"')[::2])
            if re.search(r'[!,:]',  between_quotes):
                return False
            if '..' in name:
                return False
        else:
            return False
        return True

    def check_email(self, email = ''):
        '''
        Checking E-mail based on check_domain() and check_name()
        Args:
            email - string to check
        Return:
            True - if email format is correct
            False - if email format is incorrect
        '''
        if email != '':
            self.email = email
        try:
            name, domain = self.email.split('@')
        except ValueError:
            return False
        return self.check_name(name) and self.check_domain(domain)

if __name__ == '__main__':
    email = 'diabramo@yandex.ru'
    email_checker = EmailChecker(email)
    print email_checker.check_email()
