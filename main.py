from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, Optional
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)


db.create_all()


class FeedbackForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
    text = TextAreaField('Текст отзыва', validators=[DataRequired(message="Поле не должно быть пустым")])
    email = EmailField('Ваш email', validators=[Optional()])
    rating = SelectField('Ваша оценка?', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Добавить')


class NewsForm(FlaskForm):
    title = StringField('Название',
                        validators=[DataRequired(message="Поле не должно быть пустым"),
                                    Length(max=255, message='Введите заголовок длинной до 255 символов')])
    text = TextAreaField('Текст',
                         validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField('Добавить')


@app.route('/')
def index():
    news_list = News.query.all()
    return render_template('index.html',
                           news=news_list)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news_detail = News.query.get(id)
    return render_template('news_detail.html',
                           item=news_detail)


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        text = form.text.data
        email = form.email.data
        rating = form.rating.data
        print(name, text, email, rating)
        return redirect('/')
    return render_template('feedback.html', form=form)


@app.route('/add_news/', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('index', id=news.id))
    return render_template('add_news.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
