from django import forms
# from django.forms  import ModelForm
from movie.models import User

class RegisterForm(forms.ModelForm):
    '''注册用的表单'''
    pwd_repeat=forms.CharField(max_length=256)
    def get_errors(self):
        errors=self.errors.get_json_data()
        errors_lst=[]
        for messages in errors.values():
            for message_dict in messages:
                for key,message in message_dict.items():
                    if key=='message':
                        errors_lst.append(message)
        return errors_lst


    # 普通验证之后的最后一层验证
    # 验证密码
    def clean(self):
        cleaned_data=super(RegisterForm,self).clean()
        pwd=cleaned_data.get('password')
        pwd_repeat=cleaned_data.get('pwd_repeat')
        if pwd != pwd_repeat:
            raise forms.ValidationError(message='两次密码输入不一致！')

        return cleaned_data
    class Meta:
        model = User
        fields=['name','password','email']

class LoginForm(forms.ModelForm):
    '''用于登录的表单'''

    def get_error(self):
        # 返回错误信息
        pass

    class Meta:
        model=User
        fields=['name','password']