from flask import Flask, render_template

app = Flask(__name__)

# Новости
news = [
    {
        'title': 'Учёные обнаружили новый вид морских существ в глубинах Тихого океана',
        'text': 'Группа международных учёных провела успешную экспедицию в отдалённые районы Тихого океана,'
                ' где были обнаружены ранее неизвестные виды морских существ. Исследователи уверены, что их открытие'
                ' может пролить свет на процессы эволюции и адаптации в экстремальных условиях глубин океана.',
        'category': 'Наука'
    },
    {
        'title': 'Удивительное событие в школе',
        'text': 'Вчера в местной школе произошло удивительное событие - все'
                'ученики одновременно зевнули на уроке математики. '
                'Преподаватель был так поражен этим коллективным зевком, '
                'что решил отменить контрольную работу.',
        'category': 'Образование'
    },
    {
        'title': 'В Москве состоялся крупнейший музыкальный фестиваль года',
        'text': 'В столице России завершился масштабный музыкальный фестиваль,'
                ' который собрал десятки тысяч зрителей. В течение трёх дней на'
                ' сцене выступили как известные мировые звёзды, так и начинающие артисты.'
                ' Организаторы уже подтвердили проведение следующего фестиваля в следующем году,'
                ' обещая ещё больше ярких выступлений.',
        'category': 'Культура'
    },
    {
        'title': 'Учебный год начнётся с новых правил для школьников и учителей',
        'text': 'В новом учебном году школы России введут несколько нововведений,'
                ' касающихся как учеников, так и преподавателей. Среди изменений — обновлённая'
                ' система оценивания, новые образовательные стандарты, а также улучшенные меры '
                'безопасности в связи с пандемией. Родителям рекомендовано ознакомиться с новыми правилами,'
                ' чтобы подготовить детей к учебному процессу.',
        'category': 'Образование'
    }
]

# Главная страница
categories = ['Наука', 'Культура', 'Образование']


@app.route('/')
def index():
    context = {
        'title': 'Новостной сайт',
        'text': 'Скоро тут будут новости!',
        'categories': categories
    }
    return render_template('index.html', **context)


# Новости
@app.route('/news/')
def news_list():
    return render_template('news.html', title='Новости', news=news)


# Подробное описание новости
@app.route('/news_detail/<int:id>')
def news_detail(id):
    if id < 0 or id >= len(news):
        return "Новость не найдена", 404
    title = news[id]['title']
    text = news[id]['text']
    return render_template('news_detail.html', title=title, text=text)


# Категории
@app.route('/category/<category_name>')
def show_category(category_name):
    if category_name == 'Все новости':
        category_news = news
    else:
        category_news = [item for item in news if item['category'] == category_name]
    return render_template('category.html', category_name=category_name, news=category_news)


if __name__ == '__main__':
    app.run(debug=True)