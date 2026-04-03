from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField(
    'Property Type',
    choices=[
        ('', 'Select Property Type'),
        ('House', 'House'),
        ('Apartment', 'Apartment')
    ],
    validators=[DataRequired()]
)
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired()])