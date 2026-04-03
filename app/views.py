"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, db
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash
import os


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()

    if form.validate_on_submit():
        file = form.photo.data
        filename = secure_filename(file.filename)

        upload_folder = os.path.join(app.root_path, 'static', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))

        new_property = Property(
            title=form.title.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            location=form.location.data,
            price=form.price.data,
            property_type=form.property_type.data,
            description=form.description.data,
            photo=filename
        )

        db.session.add(new_property)
        db.session.commit()

        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))

    if request.method == 'POST':
        print("FORM ERRORS:", form.errors, flush=True)
        flash_errors(form)

    return render_template('create_property.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                "Error in the {} field - {}".format(
                    getattr(form, field).label.text,
                    error
                ),
                'danger'
            )


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route('/properties')
def properties():
    all_properties = Property.query.all()
    return render_template('properties.html', properties=all_properties)

@app.route('/properties/<int:propertyid>')
def property_details(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('property.html', property=property)