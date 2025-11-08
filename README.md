# FinancialDash - Backend API 🚀

API REST em FastAPI para análise financeira com modelos de volatilidade (GARCH), Hidden Markov Models (HMM) e cotações de mercado.

> **Repositório Original**: [BackendAlphaTrading](https://github.com/thales700/BackendAlphaTrading)

## 📝 Sobre

O backend do FinancialDash fornece uma API REST robusta para análise de dados financeiros, incluindo:

- **Cotações de Mercado**: Coleta e processamento de dados históricos via yfinance
- **Análise de Volatilidade**: Modelos GARCH/ARCH para estimativa de volatilidade
- **Regimes de Mercado**: Identificação de estados de mercado usando Hidden Markov Models
- **Múltiplos Símbolos**: Suporte para diversos ativos financeiros
- **Granularidade Flexível**: Dados em diferentes intervalos de tempo

## 🛠️ Tecnologias

- **Python 3.12**
- **FastAPI**: Framework web moderno e assíncrono
- **yfinance**: Coleta de dados do Yahoo Finance
- **pandas**: Manipulação e análise de dados
- **numpy**: Computação numérica
- **hmmlearn**: Implementação de Hidden Markov Models
- **arch**: Modelos ARCH/GARCH para volatilidade
- **Pydantic**: Validação de dados
- **Uvicorn**: Servidor ASGI

## 📁 Estrutura do Projeto

```
backend/
│
├── API/                        # Camada de API
│   └── routers/               # Rotas da API
│       ├── symbol_data.py     # Endpoints de cotações
│       ├── symbol_hmm.py      # Endpoints de Markov
│       └── symbol_volatility.py  # Endpoints de volatilidade
│
├── entities/                   # Entidades de domínio
│   ├── ArchModels.py          # Tipos de modelos ARCH/GARCH
│   ├── Distribution.py        # Tipos de distribuição
│   ├── Granularity.py         # Intervalos de tempo
│   └── Symbols.py             # Símbolos financeiros suportados
│
├── schemas/                    # Schemas Pydantic
│   └── symbol_properties.py   # Schema de propriedades de símbolos
│
├── services/                   # Lógica de negócio
│   ├── Quotations.py          # Serviço de cotações
│   ├── HiddenMarkovModel.py   # Serviço de HMM
│   └── GarchLevels.py         # Serviço de volatilidade GARCH
│
├── mock_data/                  # Dados mockados para desenvolvimento
│   ├── quotations.json
│   ├── hidden_markov_model.json
│   └── garch_levels.json
│
├── tests/                      # Testes da API
│   ├── GetQuotations.py
│   ├── GetMarkovRegime.py
│   └── GetVolatilityLevels.py
│
├── main.py                     # Ponto de entrada da aplicação
├── requirements.txt            # Dependências Python
├── Dockerfile                  # Container Docker
└── GenerateMockData.py         # Script para gerar dados mockados
```

## 🚀 Como Rodar

### Opção 1: Com Docker (Recomendado)

```bash
# Na raiz do projeto
docker-compose up backend

# Ou apenas o backend
cd backend
docker build -t financialdash-backend .
docker run -p 8000:8000 financialdash-backend
```

### Opção 2: Ambiente Local

#### 1. Criar ambiente virtual

```bash
cd backend

# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### 2. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 3. Executar a aplicação

```bash
# Modo desenvolvimento (com reload automático)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Modo produção
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### 4. Acessar a API

- **API**: http://localhost:8000
- **Documentação Interativa (Swagger)**: http://localhost:8000/docs
- **Documentação Alternativa (ReDoc)**: http://localhost:8000/redoc

## 📡 API Endpoints

### 1. Health Check

```http
GET /
```

Verifica se a API está funcionando.

**Resposta:**
```json
{
  "Hello": "World"
}
```

### 2. Cotações de Mercado

```http
POST /data
```

Retorna cotações históricas de um símbolo financeiro.

**Body:**
```json
{
  "symbol": "AAPL",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "granularity": "1d"
}
```

**Parâmetros:**
- `symbol`: Símbolo do ativo (ex: AAPL, MSFT, GOOGL)
- `start_date`: Data inicial (formato: YYYY-MM-DD)
- `end_date`: Data final (formato: YYYY-MM-DD)
- `granularity`: Intervalo de tempo (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)

**Resposta:**
```json
{
  "symbol": "AAPL",
  "data": [
    {
      "Date": "2024-01-01",
      "Open": 150.5,
      "High": 152.0,
      "Low": 149.0,
      "Close": 151.5,
      "Volume": 1000000
    }
  ]
}
```

### 3. Regimes de Markov

```http
POST /markov_regimes?n_regimes=3
```

Identifica regimes de mercado usando Hidden Markov Models.

**Query Params:**
- `n_regimes`: Número de regimes a identificar (ex: 2, 3, 4)

**Body:**
```json
{
  "symbol": "AAPL",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "granularity": "1d"
}
```

**Resposta:**
```json
{
  "symbol": "AAPL",
  "regimes": [
    {
      "Date": "2024-01-01",
      "Regime": 0,
      "Return": 0.05
    }
  ]
}
```

### 4. Níveis de Volatilidade GARCH

```http
POST /garch_levels?modelType=GARCH&distribution=normal&levels=5
```

Estima níveis de volatilidade usando modelos GARCH/ARCH.

**Query Params:**
- `modelType`: Tipo de modelo (GARCH, ARCH, EGARCH, etc.)
- `distribution`: Tipo de distribuição (normal, t, skewt, etc.)
- `levels`: Número de níveis de volatilidade (ex: 3, 5, 7)

**Body:**
```json
{
  "symbol": "AAPL",
  "start_date": "2024-01-01",
  "end_date": "2024-12-31",
  "granularity": "1d"
}
```

**Resposta:**
```json
{
  "symbol": "AAPL",
  "garch_levels": [
    {
      "Date": "2024-01-01",
      "Volatility": 0.02,
      "Level": 1
    }
  ]
}
```

## 🔧 Desenvolvimento

### Gerar Dados Mockados

Para desenvolvimento e testes sem dependência de APIs externas:

```bash
python GenerateMockData.py
```

Isso gerará arquivos JSON em `mock_data/` com dados simulados.

### Executar Testes

```bash
# Executar scripts de teste individuais
python tests/GetQuotations.py
python tests/GetMarkovRegime.py
python tests/GetVolatilityLevels.py
```

### Adicionar Novos Símbolos

Edite o arquivo `entities/Symbols.py` e adicione o novo símbolo:

```python
class Symbols(Enum):
    AAPL = "AAPL"
    NOVO_SIMBOLO = "NOVO"  # Adicione aqui
```

### Adicionar Novas Granularidades

Edite o arquivo `entities/Granularity.py`:

```python
class Granularity(Enum):
    ONE_DAY = "1d"
    NOVA_GRANULARIDADE = "1h"  # Adicione aqui
```

## 📦 Dependências Principais

```
fastapi[standard]  # Framework web com dependências extras
yfinance          # Coleta de dados financeiros
pandas            # Manipulação de dados
numpy             # Computação numérica
hmmlearn          # Hidden Markov Models
arch              # Modelos GARCH/ARCH
```

## 🔒 Variáveis de Ambiente

Atualmente a aplicação não requer variáveis de ambiente específicas, mas você pode configurar:

```bash
# Porta do servidor (padrão: 8000)
export PORT=8000

# Modo de debug
export PYTHONUNBUFFERED=1
```

## 🐛 Troubleshooting

### Erro ao instalar hmmlearn

```bash
# Instalar dependências do sistema (Linux)
sudo apt-get install gcc g++ git

# Instalar dependências do sistema (Mac)
brew install gcc git

# Windows: Instalar Visual C++ Build Tools
```

### Erro ao coletar dados do yfinance

```bash
# Verificar conexão com internet
# Verificar se o símbolo é válido
# Verificar se as datas estão corretas
```

### Porta 8000 já em uso

```bash
# Usar outra porta
uvicorn main:app --reload --port 8080

# Ou matar o processo usando a porta (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

## 📚 Documentação Adicional

- **FastAPI**: https://fastapi.tiangolo.com
- **yfinance**: https://github.com/ranaroussi/yfinance
- **hmmlearn**: https://hmmlearn.readthedocs.io
- **arch**: https://arch.readthedocs.io

## 📄 Licença

Consulte o arquivo LICENSE para mais informações.

---

**Desenvolvido para análise financeira avançada** 📈
