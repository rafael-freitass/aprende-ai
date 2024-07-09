# README.md

## Projeto: Geração de Provas com Google Generative AI

Este projeto utiliza a API do Google Generative AI para gerar provas com questões baseadas em diferentes matérias, tipos de prova e níveis de dificuldade. A aplicação é construída usando Flask e permite a criação de provas personalizadas através de uma interface web.

### Pré-requisitos

1. **Python 3.x**
2. **Flask**
3. **Biblioteca `google-generativeai`**
4. **Biblioteca `python-dotenv`**
5. **Conta no Google Cloud com acesso à API do Google Generative AI**
6. **Chave API do Google Generative AI**

### Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API:
   ```env
   api_key=YOUR_GOOGLE_API_KEY
   ```

### Uso

1. Execute a aplicação Flask:
   ```bash
   python app.py
   ```

2. Acesse `http://127.0.0.1:5000` no seu navegador para visualizar a interface web.

### Estrutura do Projeto

- `app.py`: Arquivo principal que contém a lógica da aplicação Flask e integração com a API do Google Generative AI.
- `templates/index.html`: Template HTML para a interface web.

### Endpoints

- **GET /**: Rota principal que renderiza a página inicial.
- **POST /resource**: Rota que processa os dados do formulário e gera a prova com base nas opções selecionadas.

### Exemplos de Uso da API

O payload enviado para a geração de provas contém as seguintes informações:
```json
{
    "materia": "Matemática",
    "tipo_prova": "questões objetivas",
    "dificuldade": "Médio",
    "num_questoes": 5
}
```

O prompt gerado será:
```
Crie 5 questões objetivas de Matemática nível Médio. Utilize contextos e histórias no enunciado, coisas que fazem o estudante pensar e juntar informações para responder. Não utilize ** para indicar a questão ou a resposta, faça do seguinte modelo: 1) questao.. Resposta: a) b) c) d)... Gabarito:
```

### Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

### Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

### Contato

Para mais informações, entre em contato com [seu email@example.com].

---

### Notas

- Certifique-se de ter permissões adequadas para usar a API do Google Generative AI.
- Verifique os custos associados ao uso da API no [Google Cloud Pricing](https://cloud.google.com/pricing).
