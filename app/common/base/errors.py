class Errors:

    @staticmethod
    def getMessage(code):
        for attribute in Errors.__dict__:
            if attribute.islower():
                continue
            if Errors.__dict__[attribute] == code:
                return attribute.replace('_', ' ').capitalize()
        return ''

    SUCCESS = 0
    SEVER_ERROR = 1000
