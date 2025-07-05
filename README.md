# Alzheimer Prediction App

## 📖 Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação **Full Stack em Flask** para **previsão da propensão ao Alzheimer** em pacientes idosos, utilizando um modelo de classificação treinado com dados públicos.

O projeto utiliza o dataset disponível no Kaggle:\
🔗 [Alzheimer's Disease Dataset](https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset)

A aplicação permite:

- Entrada de novos dados de pacientes por meio de um formulário.
- Classificação em tempo real para verificar propensão ou não ao Alzheimer.
- Visualização clara e organizada dos resultados.

---

## 🗂️ Estrutura do Projeto

```text
alzheimer-app/
│
├── app.py                # API Backend: gerencia o fluxo da aplicação Flask e executa as predições
├── requirements.txt      # Lista de dependências do projeto Flask e bibliotecas Python
│
├── templates/            # Arquivos HTML (interface do usuário)
│   ├── index.html        # Formulário para entrada de dados do paciente
│   ├── result.html       # Tela de exibição do resultado da predição
│
├── ML/                   # Diretório de Machine Learning
│   ├── data/             # Arquivos de dados utilizados para treino e teste do modelo
│   ├── models/           # Modelos treinados salvos em formato .pkl
│   ├── notebook/         # Cadernos Jupyter utilizados para desenvolvimento e testes do modelo
│
├── tests/                # Scripts de testes automatizados para validação de desempenho dos modelos
```

---

## ⚙️ Instruções de Instalação e Configuração

### ✔️ Pré-requisitos:

- Python 3.8 ou superior
- Flask
- Scikit-learn
- Pandas
- Pytest

### ✔️ Instalação das Dependências

Execute:

```bash
pip install -r requirements.txt
```

### ✔️ Executando o Projeto Flask

Para iniciar a aplicação no modo debug:

```bash
flask --app app.py --debug run
```

Isso iniciará o servidor Flask local e permitirá atualização automática a cada mudança de código.

### ✔️ Executando os Testes com Pytest

Para rodar os testes automatizados e visualizar as saídas no terminal:

```bash
pytest -s
```

O parâmetro `-s` é utilizado para **exibir as mensagens **`` durante a execução dos testes, pois o `pytest` oculta as saídas padrão por padrão.

---

## 📊 Teste Automatizado de Avaliação do Modelo

O projeto utiliza um **teste automatizado com Pytest** para garantir que o modelo de machine learning continue atendendo a requisitos mínimos de desempenho antes de ser implantado.

### 📂 Estrutura do Teste

O teste avalia o modelo a partir de:

- Dados de teste separados.
- Requisitos de desempenho definidos para classificação.

### 📊 Métricas Avaliadas:

| Métrica  | Valor Mínimo | Descrição Técnica                                                                                                                                                          |
| -------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accuracy | 0.64         | Mede a proporção total de classificações corretas sobre o total de amostras. Indicada para datasets balanceados.                                                           |
| Recall   | 0.80         | Mede a capacidade do modelo de encontrar corretamente os pacientes com Alzheimer (sensibilidade). Alta importância para não deixar casos positivos passarem despercebidos. |
| F1-Score | 0.80         | Média harmônica entre precisão e recall. Equilibra o risco de falsos positivos e falsos negativos.                                                                         |
| AUC-ROC  | 0.85         | Área sob a curva ROC. Mede a capacidade do modelo de separar corretamente as classes. Quanto mais próximo de 1, melhor a separação.                                        |

> ⚙️ O teste automatizado utiliza o comando:

```bash
pytest -s
```

O parâmetro `-s` permite visualizar no terminal as métricas calculadas durante a execução, como `Accuracy`, `Recall` e `F1-Score`.

### ✔️ Objetivo do Teste

Esse teste é essencial para:

- Garantir qualidade contínua.
- Impedir a implantação de modelos que não atendam aos padrões mínimos.
- Facilitar a comparação entre diferentes modelos no mesmo projeto.

---

## 💻 Interface do Usuário

### 📋 Tela Principal - Formulário (`index.html`)

O usuário preenche os dados do paciente por meio de um formulário dividido por seções:

- Informações do paciente
- Detalhes demográficos
- Fatores de estilo de vida
- Histórico médico
- Medidas clínicas
- Avaliações cognitivas
- Sintomas

### 📊 Tela de Resultado (`result.html`)

Após o envio do formulário, o resultado da predição é exibido com:

- Destaque visual (cor e ícone de alerta ou sucesso)
- Resumo completo dos dados inseridos

Se desejar, é possível incluir imagens de exemplo das telas para complementar o documento.

