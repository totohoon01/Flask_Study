# Flask Tutorials

### Settings

- pip install flask
- app을 함수로 만들자(중복 호출 방지!)
- html : /templates
- css, js, ... : /static/{each}
- 라우팅 : views

### API 생성

- @app.route("/")

### url_for()

- 경로를 동적으로 구성, 유지보수에 편리하다.

### BootStrap

- getbootstrap.com
- bootstrap.min.css -> css폴더에
- <link rel="stylesheet" href="{{url_for('static', filename='bootstrap.min.css')}}">
- 미리 정의된 스타일 느낌? 편한지는 아직 잘 모르겠다.

### 템플릿 상속

<code>
{% extends 'base.html' %}   
{% block content %}   
...   
{% endblock %}   
</code>

### 폼 모듈

- pip install Flask-WTF
- CSRF(사용자의 요청 위조) 공격 방지
