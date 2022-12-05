from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, InputRequired, Length, regexp

class CompanyForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(),Length(1,60)])
    address = StringField("Address", validators=[InputRequired(),Length(1,100)])
    city = StringField("City", validators=[InputRequired(),Length(1,20)])
    zip = StringField("Zip", validators=[DataRequired(), InputRequired(), Length(5)], render_kw={"pattern": '[0-9]*', "title": "Enter at least 5 digits"})
    website = StringField("Website")
    submit = SubmitField("Add Company")

class EmployeeForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(),Length(1,20)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(1,20)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
