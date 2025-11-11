# Relatório de Marketing - Análise Trello

Sistema completo de análise de desempenho do setor de Marketing e Comunicação baseado em dados do Trello.

## 📋 Sobre o Projeto

Este projeto analisa dados exportados do Trello para gerar insights executivos sobre:
- Performance da equipe de marketing
- Produtividade por categoria de serviço
- Análise de demandantes e priorização
- Métricas de Lead Time, Throughput e Eficiência
- Catálogo estruturado de serviços

## 🚀 Como Usar

### 1. Exportar Dados do Trello

Exporte seu board do Trello em formato JSON e coloque na pasta raiz do projeto com o nome:
```
Vm10BDod - comunicacao-e-marketing.json
```

### 2. Executar Análises

```bash
# Análise de demandantes
python analyze_trello.py

# Classificação de serviços
python classify_services.py

# Cálculo de métricas
python calculate_metrics.py
```

### 3. Resultados Gerados

Os scripts geram automaticamente:
- `demandantes.md` - Lista de demandantes identificados
- `catalogo_servicos_mkt.md` - Catálogo completo de serviços
- `metricas.md` - Métricas e KPIs de performance

## 📊 Arquivos do Projeto

### Scripts Python
- `analyze_trello.py` - Identifica e analisa demandantes
- `classify_services.py` - Classifica demandas por categoria de serviço
- `calculate_metrics.py` - Calcula métricas de performance e produtividade

### Documentação
- `CLAUDE.md` - Guia para Claude Code trabalhar no projeto
- `README.md` - Este arquivo
- `prompt.md` - Prompt completo para gerar relatórios executivos

### Relatórios Gerados
- `demandantes.md` - 7 demandantes identificados com estatísticas
- `catalogo_servicos_mkt.md` - 14 categorias de serviços catalogadas
- `metricas.md` - Metodologia e indicadores executivos

## 📈 Principais Métricas

O sistema calcula automaticamente:

- **Lead Time**: Tempo desde criação até conclusão de demandas
- **Throughput**: Quantidade de demandas concluídas por período
- **Taxa de Conclusão**: Percentual de demandas finalizadas
- **Eficiência**: Tempo real vs tempo esperado por complexidade
- **Produtividade**: Pontuação ponderada por complexidade

## 🎯 Demandantes Identificados

1. MSB
2. KOGNI
3. EQUANIMUS (inclui GOVONE)
4. GRIX
5. SIMPLIFIXA
6. SE7TI
7. LSG business hub

## 📦 Categorias de Serviços

1. Design Gráfico - Cards e Artes (Baixa complexidade)
2. Design Gráfico - Apresentações (Média complexidade)
3. Design Gráfico - Branding e Identidade Visual (Alta complexidade)
4. Design Gráfico - Material Impresso (Média complexidade)
5. Produção de Vídeo - Institucional (Alta complexidade)
6. Produção de Vídeo - Cobertura de Eventos (Média complexidade)
7. Social Media - Copywriting (Baixa complexidade)
8. Eventos e Ações Promocionais (Alta complexidade)
9. Planejamento Estratégico (Alta complexidade)
10. Fotografia (Média complexidade)
11. Comunicação Interna (Baixa complexidade)
12. Produtos e Fichas Técnicas (Média complexidade)
13. Formulários e Processos (Baixa complexidade)
14. Outros Serviços (Variável)

## 🎨 Sistema de Pontuação

- **Complexidade Baixa**: 1 ponto (2-8 horas)
- **Complexidade Média**: 3 pontos (1-3 dias)
- **Complexidade Alta**: 5 pontos (3-10 dias)

## 📝 Gerando Relatórios Executivos

Use o arquivo `prompt.md` com um LLM (Claude, GPT-4) para gerar relatórios executivos completos. O prompt inclui:

- Estrutura de 8 seções
- Diretrizes de elaboração
- Visualizações sugeridas
- Perguntas-chave a responder
- Checklist de qualidade

## 🔄 Atualizações Periódicas

Recomenda-se executar as análises mensalmente para:
- Acompanhar evolução de KPIs
- Identificar tendências
- Ajustar estratégias
- Manter relatórios atualizados

## 📌 Observações Importantes

- O arquivo JSON do Trello não é versionado (`.gitignore`) devido ao tamanho
- Dados sensíveis devem ser tratados com confidencialidade
- Métricas são calculadas baseadas em movimentações para listas "Concluído" e "Concluídos Design Gráfico"
- Labels "Em Alteração" não são consideradas como demandantes

## 🛠️ Requisitos

- Python 3.7+
- Bibliotecas padrão do Python (json, collections, datetime, statistics)
- Arquivo JSON exportado do Trello

## 📄 Licença

Este projeto foi desenvolvido para uso interno de análise de performance de marketing.

## 👥 Contato

Para dúvidas ou sugestões sobre o projeto, entre em contato com a equipe de análise de dados.

---

**Última atualização:** 11/11/2025
**Versão:** 1.0
