# Financial Fraud Detection

Este projeto utiliza o conjunto de dados "PaySim1" disponível sob a licença CC BY-SA 4.0. Agradecimentos ao criador do conjunto de dados [link para a fonte](https://www.kaggle.com/datasets/ealaxi/paysim1).

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um modelo de inteligência artificial para detectar fraudes em transações financeiras utilizando o conjunto de dados simulado PaySim. O modelo será treinado para classificar transações como fraudulentas ou não fraudulentas, ajudando a identificar comportamentos suspeitos.

## 🛠️ Tecnologias Utilizadas

-   Python
-   scikit-learn
-   pandas
-   Jupyter Notebook

## 📦 Como Instalar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seuusuario/Financial-Fraud-Detection.git
    cd Financial-Fraud-Detection
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 👨‍💻 Como Usar

### Jupyter

1. Execute o Jupyter Notebook:

    ```bash
    jupyter notebook
    ```

2. Abra o arquivo `model.ipynb` e siga as instruções para treinar e testar o modelo.


### Código Python

1. Execute o arquivo python `create_model.py` e espere criar o modelo.

    ```bash
    python create_model.py
    ```

2. Verifique se na pasta `model\` se o arquivo `model.pkl` foi criado

3. Teste o `arquivo` example.py

    ```bash
    python example.py
    ```

## 🧩 Estrutura do Projeto

```
financial-fraud-detection/
│
├── database/
│   └── database.csv
├── model/
│   └── __init__.py
├── .gitignore
├── create_model.py
├── example.py
├── model.ipynb
├── README.md
└── requirements.txt
```
