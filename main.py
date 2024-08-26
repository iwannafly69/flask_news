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


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    news = db.relationship('News', back_populates='category')

    def __repr__(self):
        return f'Category {self.id}: ({self.title})'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', back_populates='news')

    def __repr__(self):
        return f'News {self.id}: ({self.title})'


db.create_all()


# class FeedbackForm(FlaskForm):
#     name = StringField('Имя', validators=[DataRequired(message="Поле не должно быть пустым")])
#     text = TextAreaField('Текст отзыва', validators=[DataRequired(message="Поле не должно быть пустым")])
#     email = EmailField('Ваш email', validators=[Optional()])
#     rating = SelectField('Ваша оценка?', choices=[1, 2, 3, 4, 5])
#     submit = SubmitField('Добавить')


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок длиной до 255 символов')]
    )
    text = TextAreaField(
        'Текст',
        validators=[DataRequired(message="Поле не должно быть пустым")])
    category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')


@app.route('/')
def index():
    news_list = News.query.all()
    categories = Category.query.all()
    return render_template('index.html',
                           news=news_list,
                           categories=categories)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    news = News.query.get(id)
    categories = Category.query.all()
    return render_template('news_detail.html',
                           news=news,
                           categories=categories)


@app.route('/add_news/', methods=['GET', 'POST'])
def add_news():
    form = NewsForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        news.category_id = form.category.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('news_detail', id=news.id))
    return render_template('add_news.html', form=form, categories=categories)


@app.route('/category/<int:id>')
def news_in_category(id):
    category = Category.query.get(id)
    news = category.news
    category_name = category.title
    categories = Category.query.all()
    return render_template('category.html',
                           news=news,
                           category_name=category_name,
                           categories=categories)


if __name__ == '__main__':
    app.run(debug=True)
