# jpdm
## Jurassic Park Dinosaur Management  

Um sistema de gerenciamento de dinossauros para o trabalho de Banco de Dados II.  
Recursos utilizados: Python (com o Framework Django), MySQL, Sublime Text.  
Tarefa: criar um sistema que utilize no mínimo três tabelas em um banco de dados relacional, sendo que uma precisa ter as outras como chave estrangeira.  

### Utilização
E necessário ter instalado:  
1. Django (versão 1.10);  
2. mysqlclient (no linux) ou pymysql (no windows, também é preciso inserir no arquivo manage.py "import pymysql" e "pymysql.install_as_MySQLdb")  
3. MySQL instalado com um schema de nome 'jpdm', no entanto as configurações podem ser alteradas no arquivo settings.py  
Após instalar é necessário executar "python manage.py runserver" e testar o webapp.
