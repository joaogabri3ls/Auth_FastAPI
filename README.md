# Simple API with FastAPI

## Descrição

Este projeto é uma API completa para gerenciamento de usuários, incluindo manipulação de imagens de perfil. A API é construída com FastAPI e utiliza SQLAlchemy, SQLModel, PostgreSQL, Alembic, e Docker para fornecer uma solução robusta e escalável.

## Tecnologias

- **FastAPI**: Framework web moderno para construir APIs de alto desempenho.
- **SQLAlchemy**: ORM para interagir com o banco de dados PostgreSQL.
- **SQLModel**: ORM e Pydantic para fácil definição de modelos e validação de dados.
- **PostgreSQL**: Banco de dados relacional usado para armazenar dados da API.
- **Alembic**: Ferramenta para migrações de banco de dados.
- **Docker**: Containerização para simplificar a execução do projeto.
- **JWT (JSON Web Tokens)**: Utilizado para autenticação e autorização.

## Instalação e Configuração

### Docker Downloads

- **Docker**: [Download Docker](https://www.docker.com/get-started)
- **Docker Compose**: [Download Docker Compose](https://docs.docker.com/compose/install/)

### Inicialização do Projeto com Docker

1. **Construa o projeto**

    ```bash
    docker-compose build
    ```

2. **Inicie o projeto**

    ```bash
    docker-compose up
    ```

    O Docker iniciará os containers para a API e o banco de dados. A API estará disponível em `http://0.0.0.0:8000`.

## Documentação da API

A documentação interativa da API está disponível em [Swagger UI](http://0.0.0.0:8000/docs) e pode ser acessada para explorar e testar os endpoints da API.

## Exemplos de Uso da API

### 1. Adicionar um Usuário

- **Método**: `POST`
- **Rota**: `/users`
- **Descrição**: Adiciona um novo usuário. A senha deve ser incluída na requisição e será criptografada antes de ser armazenada.
- **Exemplo de Request**:

    ```bash
    curl -d '{"name":"Thiago Cruz", "email":"thiagoaugustocruz@gmail.com", "password":"strongpassword123"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:8000/users
    ```

- **Resposta**:

    ```json
    {
        "msg": "User created successfully"
    }
    ```

### 2. Obter Todos os Usuários

- **Método**: `GET`
- **Rota**: `/users`
- **Descrição**: Obtém uma lista de todos os usuários registrados.
- **Exemplo de Request**:

    ```bash
    curl -X GET http://0.0.0.0:8000/users
    ```

- **Resposta**:

    ```json
    [
        {
            "id": 1,
            "name": "Thiago Cruz",
            "email": "thiagoaugustocruz@gmail.com"
        }
    ]
    ```

### 3. Login de Usuário

- **Método**: `POST`
- **Rota**: `/login`
- **Descrição**: Autentica um usuário e retorna um token JWT se a autenticação for bem-sucedida.
- **Exemplo de Request**:

    ```bash
    curl -d 'username=thiagoaugustocruz@gmail.com&password=strongpassword123' -H "Content-Type: application/x-www-form-urlencoded" -X POST http://0.0.0.0:8000/login
    ```

- **Resposta**:

    ```json
    {
        "access_token": "<TOKEN_JWT>",
        "token_type": "bearer"
    }
    ```

### 4. Atualizar Imagem de Perfil

- **Método**: `PUT`
- **Rota**: `/users/{user_id}/profile-image`
- **Descrição**: Atualiza a imagem de perfil do usuário especificado.
- **Exemplo de Request**:

    ```bash
    curl -F "file=@/path/to/image.jpg" -H "Authorization: Bearer <TOKEN_JWT>" -X PUT http://0.0.0.0:8000/users/1/profile-image
    ```

- **Resposta**:

    ```json
    {
        "msg": "Profile image updated successfully"
    }
    ```

## Configuração para AWS

No futuro, a API será implantada na AWS. Para mais informações sobre a configuração e implantação na AWS, consulte a documentação específica da AWS.

## Contribuição

Se você deseja contribuir para este projeto, por favor, faça um fork do repositório e envie um pull request com suas melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
