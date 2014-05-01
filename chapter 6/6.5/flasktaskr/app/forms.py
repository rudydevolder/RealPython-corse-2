# forms.py


from flask.ext.wtf import Form, TextField, PasswordField, DateField, IntegerField, SelectField
from flask.ext.wtf import Required, Email, EqualTo, Length

class RegisterForm(Form):
    name = TextField('Username', validators=[Required(), Length(min=6, max=25)])
    email = TextField('Email', validators=[Required(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[Required(), Length(min=6, max=40)])         
    confirm = PasswordField('Repeat Password',[Required(), EqualTo('password', message='Passwords must match')])

class LoginForm(Form):
    name = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])

class AddTask(Form):
    task_id = IntegerField('Priority')
    name = TextField('Task Name', validators=[Required()])
    due_date = DateField('Date Due (mm/dd/yyyy)', validators=[Required()],format='%m/%d/%Y')
    priority = SelectField('Priority', validators=[Required()],choices=[('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5')])
    status = IntegerField('Status')