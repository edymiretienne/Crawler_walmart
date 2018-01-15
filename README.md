# Crawler_walmart
Crawler Walmart's site

## Getting Started
Run the script file "run_crawler"

All products stored in MongoDB:

Data_base: "walmart"

Collection: "products"

Campos:

url: (string) Url do produto sendo extraído

nome: (string) Nome do produto

descricao: (string) Texto contendo a descrição do produto

categoria: (string) Categoria em que o produto se enquadra

marca: (string) Marca do produto

navegacao: (string list) Lista de categorias e subcategorias de navegação, indo do mais geral para mais específico

nome_vendedor: (string) Nome do vendedor do produto

valor: (float) Valor atual do produto

valor_antigo: (float) Valor do produto sem desconto, se houver

imagem_principal: (string) URL da imagem do produto

imagens_secundarias: (string list) Lista de URL das imagens secundárias

caracteristicas: (list dict) Lista de dicionários contendo as caracteristicas do produto Ex.: [{'name': 'Cor', 'value': 'Preto'}]

dimensoes: (dict) Dicionário com as dimensões do produto Ex.: {'altura': '2,00 cm', 'largura': '40,00 cm', 'peso': '2,59 kg'}

### Prerequisites

Scrapy 1.4.0

MongoDB
