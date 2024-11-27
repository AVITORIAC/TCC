<!-- 
* Sobre nosso projeto:

Este projeto foi realizado para noss TCC, projeto de conclusão do curso de Desenvolvimento de Sistemas em conjunto com o Senai e a Bosch

O Meinung é uma plataforma para realização e gerenciamento de feedbacks realizados com os aprendiz da ETS na Bosch

Nele é possível automatizar alguns processos, ter a centralização de dados, além de dashboards com rendimento dos alunos e das turmas durante os semestres.

Esse repo contém o backend da nossa plataforma que está sendo feito com Django Rest Framework do python, nele há nosso banco de dados, os modelos necessários, além das rotas precisas, como cadastros, login e autweticação com authtoken, um token que o próprio Django Rest fornece, facilitando o desenvolvimento, além da segurança.

-->

<h1 align="center" style="font-weight: bold;">Meinung BackEnd💻</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> •
 <a href="#colab">Collaborators</a> •
 <a href="#contribute">Contribute</a>
</p>

<p align="center">
    <b>Meinung is a platform for managing feedback with ETS trainees at Bosch in Campinas.</b>
     <br>
   <b>It automates processes, centralizes data, and provides performance dashboards.</b>
</p>

<h2 id="tech">💻 Technologies</h2>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

<!--  https://ileriayo.github.io/markdown-badges/ -->


<h2 id="started">🚀 Getting started</h2>

To better understand how to run the project, you can refer to the file `setup_env.sh`. 

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project. For example:

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

<h3>Cloning</h3>

How to clone your project

```bash
git clone https://github.com/MeinungTCC/Back-End.git
```

<h3>Config .env variables</h2>

Use the `.env.example` as reference to create your configuration file `.env` with your SECRET_KEY, DEBUG and FERNET_KEY configs

```yaml
SECRET_KEY={YOUR_FERNET_KEY}
DEBUG={YOUR_DEBUG_CONFIG}
FERNET_KEY={YOUR_SECRET_KEY}
```

<h3>Starting</h3>

How to start your project

```bash
python -m venv .venv

.venv\Scripts\activate

# new file .env
cd C:\caminho\para\seu\diretorio
type nul > .env

pip install -r requirements.txt

python post_install.py

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```

<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>     | authenticate user into the api see [request details](#post-auth-detail)

<h3 id="get-auth-detail">GET /authenticate</h3>

**RESPONSE**
```json
{
  "edv": 12345678,
  "email": "julia@gmail.com",
  "nome": "Julia Roberta",
  "cargo": "aprendiz",
  "idTurma": 1,
  "logado": false,
  "status": "aprovado"
}
```

<h3 id="post-auth-detail">POST /authenticate</h3>

**REQUEST**
```json
{
  "edv": "12345678",
  "password": "222222222222"
}
```

**RESPONSE**
```json
{
  "message": "Login feito com sucesso",
  "id": 1,
  "token": "OwoMRHsaQwyAgVoc3OXmL1JhMVUYXGGBbCTK0GBgiYitwQwjf0gVoBmkbuyy0pSi",
  "cargo": "aprendiz",
  "curso": "Digital Solutions"
}
```

<h2 id="colab">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="" width="100px;" alt="devE"/><br>
        <sub>
          <b>Eduarda Rabelo</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="" width="100px;" alt="devJ"/><br>
        <sub>
          <b>Julia Roberta</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

Here you will explain how other developers can contribute to your project. For example, explaining how can create their branches, which patterns to follow and how to open an pull request

1. `git clone [https://github.com/Fernanda-Kipper/text-editor.git](https://github.com/MeinungTCC/Back-End.git)`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)