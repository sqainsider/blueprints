#forms.py

from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField, SelectField, PasswordField
from wtforms.validators import DataRequired,Length, EqualTo
 

class AddTaskForm(Form):
	task_id = IntegerField()
	name = StringField('Task Name', validators=[DataRequired()])
	due_date = DateField('Date Due (mm/dd/yyyy)',
		validators = [DataRequired()], format = '%m/%d/%Y'
	)
	priority = SelectField('Priority',
		validators = [DataRequired()],
		choices= [
			('1','1'),('2','2'),('3','3'),('4','4'), ('5','5')
		]
	)
	status = IntegerField('Status')


class RegistrationForm(Form):
	name = StringField('Username:', validators=[DataRequired(), Length(min=6, max=25)])
	email = StringField('Email:', validators=[DataRequired(), Length(min=6, max=40)])
	password = PasswordField('Password:', validators=[DataRequired(), Length(min=6, max=40)])
	confirm = PasswordField('Repeat Password:', validators=[DataRequired(), EqualTo('password', message='Password not match, Please try again')]
)


class LoginForm(Form):
	name = StringField(
		'Username', validators=[DataRequired()]
	)
	password = PasswordField(
		'Password', validators=[DataRequired()]
	)
