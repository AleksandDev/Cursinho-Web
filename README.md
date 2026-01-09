# Cursinho Web

Um sistema web educacional desenvolvido em Flask para oferecer cursos online em desenvolvimento web, programação orientada a objetos e ciência de dados.

## 📋 Descrição

O Cursinho Web é uma plataforma educacional que permite aos usuários se cadastrarem, fazerem login e acessar informações sobre diversos cursos. O sistema inclui funcionalidades de autenticação de usuários, visualização de cursos e um formulário de contato.

## ✨ Funcionalidades

- **Autenticação de Usuários**: Cadastro, login e recuperação de senha
- **Sistema de Cursos**: Visualização de cursos disponíveis com descrições e habilidades
- **Página de Disciplinas**: Lista de disciplinas oferecidas
- **Formulário de Contato**: Permite aos usuários enviar mensagens
- **Interface Responsiva**: Design moderno com CSS personalizado
- **Banco de Dados**: Persistência de dados usando SQLite e SQLAlchemy

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.11, Flask
- **Banco de Dados**: SQLite com SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Templates**: Jinja2

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Git

### Passos para Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/AleksandDev/Cursinho-Web.git
   cd Cursinho-Web
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requeriments.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra [http://localhost:5000](http://localhost:5000)

## 🚀 Uso

### Primeiro Acesso

- O sistema cria automaticamente um usuário administrador:
  - **Usuário**: admin
  - **Senha**: mudar123

### Funcionalidades Principais

1. **Login**: Acesse com suas credenciais
2. **Cadastro**: Crie uma nova conta
3. **Cursos**: Navegue pelas disciplinas disponíveis
4. **Contato**: Entre em contato através do formulário

## 📁 Estrutura do Projeto

```
Cursinho-Web/
├── app.py                 # Arquivo principal da aplicação Flask
├── requeriments.txt       # Dependências do projeto
├── README.md             # Este arquivo
├── models/
│   ├── bd.py            # Configuração do banco de dados
│   ├── user.py          # Modelo de usuário
│   └── curso.py         # Modelo de curso
├── static/
│   ├── src/
│   │   ├── images/      # Imagens do projeto
│   │   └── scripts/     # Arquivos JavaScript
│   └── styles/          # Arquivos CSS
└── templates/           # Templates HTML
    ├── base.html        # Template base
    ├── index.html       # Página inicial
    ├── login.html       # Página de login
    ├── cadastro.html    # Página de cadastro
    ├── curso.html       # Página de detalhes do curso
    ├── disciplinas.html # Página de disciplinas
    └── contato.html     # Página de contato
```

## 🔧 Configuração

### Banco de Dados

O projeto utiliza SQLite como banco de dados. As tabelas são criadas automaticamente na primeira execução.

### Chave Secreta

Para produção, altere a `app.secret_key` no arquivo `app.py` para uma chave segura.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através do formulário na página de contato da aplicação.