from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    """
    Custom signup form to remove username
    """

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']