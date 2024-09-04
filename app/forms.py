from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, Email, EqualTo

from .models import Category


class CategoryForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(message="Поле не должно быть пустым"),
                                                Length(max=255, message='Введите заголовок длиной до 255 символов')])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email(message='Некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите пароль",
                              validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class NewsForm(FlaskForm):
    title = StringField(
        'Название',
        validators=[DataRequired(message="Поле не должно быть пустым"),
                    Length(max=255, message='Введите заголовок до 255 символов')]
    )
    text = TextAreaField(
        'TekcT',
        validators=[DataRequired(message="Поле не должно быть пустым")]
    )
    category = SelectField('Категории', choices=get_categories(), validators=[Optional()])
    # category = SelectField(choices=get_categories())
    submit = SubmitField('Добавить')

