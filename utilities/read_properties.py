import configparser
# from xdist.remote import config

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_url_page():
        page_url= config.get('admin login info', 'url')
        return page_url

    @staticmethod
    def get_username():
        username= config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password

    @staticmethod
    def get_name():
        name = config.get('admin login info', 'name')
        return name

    @staticmethod
    def get_lastname():
        lastname = config.get('admin login info', 'lastname')
        return lastname

    @staticmethod
    def get_code():
        code = config.get('admin login info', 'postal_code')
        return code

