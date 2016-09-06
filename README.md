-----------------
Projeto Blog/Post
----------------- 

No projeto blog, o diretório **blog/** apresentará uma pasta **meu_blog** que é a aplicação do projeto, e uma outra pasta **blog**, onde estão as configurações criadas do projeto. 

##### Estrutura do diretório do projeto:
```
blog/
	manage.py
	blog/
		__init__.py
		settings.py
		urls.py
		wsgi.py
	meu_blog/
	README.md
```

##### Estrutura do diretório da aplicação:
```
meu_blog/
	__init__.py
	admin.py
	apps.py
	migrations/
		0001_initial.py
		__init__.py
	models.py
	tests.py
	templates/
		meu_blog/
			index.html
	urls.py
	views.py
```

#### Passos a seguir:

A configuração necessária será feita a partir do arquivo Makefile com o comando `make target_label`, onde `target_label` é um alvo presente no arquivo a ser executado. 

1. Instale as dependências do python para o projeto com o comando abaixo:

	```
	$ make setup
	```

2. Crie um banco de dados chamado `db_blog`. Para isso, é preciso que o servidor MySQL esteja executando na máquina. Execute o comando abaixo:

	```
	$ make create-db
	```

3. É preciso criar tabelas no banco de dados antes de ser usado. Para fazer isso, execute o comando a seguir:

	```
	$ make db-migrate
	```

4. Crie um usuário admin onde será criado um nome para usuário, um e-mail e uma senha (mínimo de 8 caracteres e que seja diferente do nome e e-mail). Execute o comando a seguir:

	```
	$ make create-superuser-admin
	```

5. Agora rode o servidor admin do Django com o comando abaixo:

	```
	$ make run
	```

	Ao entrar na página do administrador `http://localhost:8000/admin`, será pedido o nome e a senha. Basta entrar com os dados criados no passo anterior.

6. Este item é opcional. Caso queira entrar na shell do python, execute o comando abaixo:

	```
	$ make python-shell
	```

7. Este item é opcional. Caso queira testar as operações do seu código, execute o comando abaixo:

	```
	$ make test
	```
