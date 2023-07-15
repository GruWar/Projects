from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///film-collection.db"
db = SQLAlchemy()
db.init_app(app)


class AddForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    year = StringField(label='Year', validators=[DataRequired()])
    description = StringField(label='Description',  validators=[DataRequired()])
    rating = StringField(label='Rating', validators=[DataRequired()])
    review = StringField(label='Review', validators=[DataRequired()])
    img_url = StringField(label='Img',  validators=[DataRequired()])
    submit = SubmitField(label='Add Film')


class RateMovieForm(FlaskForm):
    title = StringField("Your Title")
    year = StringField("Your Year")
    description = StringField("Your Description")
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    img_url = StringField("Your Img")
    submit = SubmitField("Done")


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Film).order_by(Film.title))
    films = result.scalars()
    return render_template("index.html", films=films)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if request.method == "POST":
        with app.app_context():
            new_book = Film(title=add_form.title.data,
                            year=add_form.year.data,
                            description=add_form.description.data,
                            rating=add_form.rating.data,
                            review=add_form.review.data,
                            img_url=add_form.img_url.data
                            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=add_form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    film_id = request.args.get("id")
    film = db.get_or_404(Film, film_id)
    if form.validate_on_submit():
        film.title = form.title.data
        film.year = form.year.data
        film.description = form.description.data
        film.rating = form.rating.data
        film.review = form.review.data
        film.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", film=film, form=form)


@app.route("/delete")
def delete():
    film_id = request.args.get('id')

    # DELETE A RECORD BY ID
    film_to_delete = db.get_or_404(Film, film_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(film_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
