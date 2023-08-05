class BaseWeaslException(Exception):
    pass


class LoginRequired(BaseWeaslException):
    pass


class AttrRequired(LoginRequired):
    pass


class WeaslAPIException(BaseWeaslException):
    def __init__(self, status_code, error):
        self.status_code = status_code
        self.error = error

    def __repr__(self):
        return '<WeaslAPIException(status_code={}, error={})>'.format(self.status_code, self.error)