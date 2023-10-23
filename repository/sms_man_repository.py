from smsactivate.api import SMSActivateAPI


class SmsManRepository:
    token = "_SMCfsVVlcdF3lxvy8ZZNQjppBEsBN19"
    sa = SMSActivateAPI(token)

    def get_balance(self):
        balance = self.sa.getBalance()
