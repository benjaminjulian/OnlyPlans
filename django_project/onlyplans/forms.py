from django import forms as d_forms

class FriendMgmtForm(d_forms.Form):
    """
        Manages friends connections
    """
    friend = d_forms.CharField(max_length=100,required=False)
