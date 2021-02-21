# calculator-library

Aula de integração contínua utilizando python realizada durante as aulas do curso "Continuous Integration With Python" na [Real Python](https://realpython.com/).

Neste curso é ensinado como realizar testes, integração e automatização dos testes on-line.

## Requerimentos:
- Ter a versão 3 do python instalada no notebook ou pc.
- Criar o ambiente virtual na pasta do projeto e instalar os requirements:
```console
pip install virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Verificar qualidade de código:
```console
flake8 --exclude=venv* --statistics
```

## Realizar testes:
```
pytest -v --cov=calculator
```
## Ferramentas utilizadas:
1. [Git](https://git-scm.com/)
2. [Virtualenv](https://pypi.org/project/virtualenv/)
3. [Pip](https://pypi.org/project/pip/)
4. [PyTest](https://docs.pytest.org/en/stable/)
5. [PyTest-Cov](https://pytest-cov.readthedocs.io/en/latest/readme.html#installation)
6. [CircleCI](https://circleci.com/)

## Licença

Este projeto é licenciado sobre a licença MIT - veja [LICENSE](https://github.com/lipegomes/calculator-library/blob/main/LICENSE) para mais informações.