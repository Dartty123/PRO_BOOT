from flask_wtf import FlaskForm
import wtforms


class LoginForm(FlaskForm):
    username = wtforms.StringField("Введіть логін або email", validators=[wtforms.validators.DataRequired()])
    password = wtforms.PasswordField("Введіть свій пароль", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Увійти")


class SingUpForm(FlaskForm):
    username = wtforms.StringField("Введіть свій логін", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Введіть електтрону пошту", validators=[wtforms.validators.Email()])
    password = wtforms.PasswordField("Введіть пароль", validators=[wtforms.validators.DataRequired(), wtforms.validators.len(6)])
    submit = wtforms.SubmitField("Зареєструватись")
