# Prompt: Relatório Executivo do Setor de Marketing

## Contexto

Você é um analista de dados especializado em gestão de marketing e performance de equipes. Sua tarefa é produzir um **relatório executivo completo** sobre o desempenho do setor de Marketing e Comunicação, baseado nos dados extraídos do board Trello e nas análises já realizadas.

## Dados Disponíveis

### 1. Board Trello (JSON)
- **Arquivo:** `Vm10BDod - comunicacao-e-marketing.json`
- **Conteúdo:** Dados completos do board incluindo:
  - 267 cards (demandas)
  - 13 listas (colunas do board)
  - Actions (histórico de atividades)
  - Labels (demandantes)
  - Membros da equipe
  - Datas de criação e movimentação

### 2. Análise de Demandantes
- **Arquivo:** `demandantes.md`
- **Conteúdo:**
  - 7 demandantes identificados (MSB, KOGNI, EQUANIMUS, GRIX, SIMPLIFIXA, SE7TI, LSG business hub)
  - Volume de demandas por demandante
  - Distribuição de cards abertos vs fechados
  - Percentuais de conclusão por demandante

### 3. Catálogo de Serviços
- **Arquivo:** `catalogo_servicos_mkt.md`
- **Conteúdo:**
  - 14 categorias de serviços identificadas
  - Complexidade de cada categoria (Baixa/Média/Alta)
  - Tempo estimado de entrega por categoria
  - Volume de demandas por categoria
  - Descrições detalhadas dos serviços
  - Exemplos reais de demandas
  - Diretrizes de entrega

### 4. Métricas e KPIs
- **Arquivo:** `metricas.md`
- **Conteúdo:**
  - Metodologia de cálculo (Lead Time, Throughput, Eficiência, Produtividade)
  - Indicadores executivos (taxa de conclusão, backlog, pontuação)
  - Performance por complexidade
  - Performance por categoria de serviço
  - Performance por demandante
  - Throughput mensal e tendências
  - Análise de eficiência (tempo real vs esperado)
  - Recomendações estratégicas

### 5. Scripts de Análise
- **Arquivos:** `analyze_trello.py`, `classify_services.py`, `calculate_metrics.py`
- **Conteúdo:** Lógica de processamento e algoritmos utilizados

## Objetivo do Relatório

Produzir um **relatório executivo estratégico** para apresentação à alta gestão, que permita:

1. **Compreender** o estado atual do setor de Marketing
2. **Avaliar** o desempenho da equipe e processos
3. **Identificar** gargalos, oportunidades e riscos
4. **Decidir** sobre investimentos, prioridades e ações corretivas
5. **Planejar** o futuro do setor com base em dados concretos

## Estrutura do Relatório

### Capa e Sumário Executivo (1 página)
- Título do relatório
- Período de análise
- Principais indicadores em destaque (3-5 números-chave)
- Conclusão de uma linha sobre o status geral

### 1. Visão Geral do Setor (1-2 páginas)
- Missão e escopo do setor de Marketing
- Composição da equipe (baseada nos membros identificados no Trello)
- Estrutura de trabalho (listas/colunas do board)
- Volume total de demandas processadas

### 2. Análise de Demandantes (1-2 páginas)
- Quem são os principais demandantes (clientes internos)
- Distribuição de demandas por demandante
- Análise de priorização e balanceamento
- Relação demandante vs taxa de conclusão
- Insights sobre dependência e diversificação

### 3. Portfólio de Serviços (2-3 páginas)
- Categorização completa dos serviços prestados
- Distribuição percentual por categoria
- Análise de complexidade do portfólio
- Serviços mais demandados vs mais concluídos
- Gaps e oportunidades no catálogo de serviços
- Recomendações sobre especialização ou expansão

### 4. Performance e Produtividade (3-4 páginas)

#### 4.1 Indicadores-Chave (KPIs)
- Taxa de conclusão e interpretação
- Lead Time médio e mediano
- Throughput e capacidade de entrega
- Pontuação de produtividade ponderada
- Backlog atual e tendência

#### 4.2 Eficiência Operacional
- Análise de eficiência por complexidade
- Tempo real vs tempo esperado
- Identificação de desvios críticos
- Causas prováveis de ineficiências

#### 4.3 Tendências Temporais
- Evolução do throughput mensal
- Sazonalidade e picos de demanda
- Previsão para os próximos meses

#### 4.4 Análise Comparativa
- Performance por categoria de serviço
- Performance por demandante
- Benchmarks internos e oportunidades de melhoria

### 5. Diagnóstico Crítico (2-3 páginas)

#### 5.1 Pontos Fortes
- O que está funcionando bem
- Competências destacadas da equipe
- Processos eficientes

#### 5.2 Pontos Fracos
- Gargalos identificados
- Categorias ou demandantes com baixa performance
- Processos ineficientes
- Gaps de capacidade ou competência

#### 5.3 Oportunidades
- Áreas de crescimento
- Automações possíveis
- Novos serviços a serem oferecidos
- Parcerias estratégicas

#### 5.4 Ameaças e Riscos
- Backlog insustentável
- Burnout da equipe
- Perda de qualidade
- Desalinhamento com expectativas dos demandantes

### 6. Recomendações Estratégicas (2-3 páginas)

#### 6.1 Ações Imediatas (1-3 meses)
- Priorização de backlog
- Otimização de processos críticos
- Quick wins identificados

#### 6.2 Iniciativas de Médio Prazo (3-6 meses)
- Capacitação da equipe
- Implementação de ferramentas
- Revisão de estrutura

#### 6.3 Visão de Longo Prazo (6-12 meses)
- Transformação estratégica
- Investimentos necessários
- Roadmap de evolução do setor

### 7. Plano de Ação (1 página)
- Lista consolidada de ações prioritárias
- Responsáveis sugeridos
- Prazos estimados
- Indicadores de sucesso para cada ação
- Budget estimado (se aplicável)

### 8. Anexos
- Tabelas detalhadas de dados
- Gráficos complementares
- Glossário de termos técnicos
- Metodologia completa de cálculo

## Diretrizes de Elaboração

### Tom e Linguagem
- **Executivo e objetivo**: Foco em insights, não em dados brutos
- **Data-driven**: Todas as afirmações devem ser respaldadas por números
- **Acionável**: Cada conclusão deve levar a uma recomendação clara
- **Equilibrado**: Reconhecer pontos fortes e fracos com imparcialidade
- **Estratégico**: Conectar operações do dia-a-dia com objetivos de negócio

### Visualizações Sugeridas
- Gráfico de pizza: Distribuição de demandas por demandante
- Gráfico de barras: Volume de demandas por categoria de serviço
- Gráfico de barras: Performance por complexidade (tempo real vs esperado)
- Gráfico de linha: Throughput mensal com tendência
- Gráfico de barras horizontais: Top 10 categorias por pontuação de produtividade
- Heatmap: Taxa de conclusão por demandante vs categoria
- Gráfico de funil: Pipeline de demandas (Backlog → Em Progresso → Concluído)
- Dashboard de KPIs: Cards destacando indicadores principais

### Formatação
- Uso de cores para indicar status (verde/amarelo/vermelho)
- Ícones para facilitar leitura rápida (✅ ⚠️ 🔴 📈 📉)
- Boxes destacados para insights-chave
- Numeração clara de seções e subseções
- Headers e footers com título do relatório e página

### Público-Alvo
- **Primário**: C-Level (CEO, COO, CMO)
- **Secundário**: Gestores intermediários e coordenadores
- **Terciário**: Equipe de marketing (para feedback e engajamento)

### Considerações Especiais

#### Contexto Organizacional
- Considere que o setor atende múltiplas empresas do grupo (MSB, KOGNI, EQUANIMUS, GRIX, etc.)
- A equipe aparenta ter 2-3 pessoas principais (baseado nas listas: Giordano, Guilherme)
- O board reflete um sistema de trabalho já em operação (não é um piloto)

#### Sensibilidade dos Dados
- Seja franco sobre problemas identificados, mas construtivo
- Evite culpabilizar indivíduos ou demandantes específicos
- Foque em processos e sistemas, não em pessoas

#### Comparações e Benchmarks
- Se possível, compare com padrões da indústria de marketing
- Use os próprios dados históricos como benchmark (mês a mês)
- Estabeleça metas realistas baseadas em capacidade demonstrada

## Entregáveis Esperados

1. **Relatório principal** (PDF/MD): 12-20 páginas
2. **Apresentação executiva** (slides): 10-15 slides para apresentação de 30 minutos
3. **Dashboard one-page**: Resumo visual em uma única página
4. **Plano de ação detalhado** (planilha): Lista de ações com timelines e responsáveis

## Perguntas-Chave a Responder

O relatório deve responder claramente:

1. **Desempenho**: O setor de marketing está cumprindo seu papel? Como sabemos?
2. **Capacidade**: A equipe atual tem capacidade para atender a demanda? Há necessidade de expansão?
3. **Eficiência**: Os processos atuais são eficientes? Onde há desperdício?
4. **Qualidade**: As entregas atendem às expectativas dos demandantes?
5. **Priorização**: As prioridades estão corretas? Há desalinhamento estratégico?
6. **Tendência**: A situação está melhorando ou piorando? Qual a trajetória?
7. **Investimento**: Onde investir para melhorar resultados? ROI esperado?
8. **Risco**: Quais os principais riscos ao não agir? Timeline de criticidade?

## Exemplo de Insight Esperado

❌ **Não fazer**: "A taxa de conclusão é 23.6%"

✅ **Fazer**:
> "**ALERTA CRÍTICO**: Com apenas 23.6% de taxa de conclusão, o setor está 56 pontos percentuais abaixo da meta saudável de 80%. Isso significa que a cada 4 demandas iniciadas, apenas 1 é concluída.
>
> **Impacto no Negócio**: 132 demandas em backlog representam aproximadamente 6 meses de trabalho ao ritmo atual (21 cards/mês), criando frustração nos demandantes e risco de perda de credibilidade do setor.
>
> **Causa Raiz Provável**: Análise de eficiência mostra que demandas simples (complexidade baixa) levam 70x mais tempo que o esperado (348h vs 5h), indicando gargalos de processo, não de volume.
>
> **Recomendação**: Implementar triagem de demandas com templates pré-aprovados para demandas simples, podendo reduzir lead time em 80% e liberar 40% da capacidade da equipe para demandas complexas de maior valor estratégico."

## Checklist de Qualidade

Antes de finalizar o relatório, verifique:

- [ ] Todos os números citados têm fonte identificável nos dados
- [ ] Cada gráfico tem título, eixos rotulados e legenda clara
- [ ] Insights principais estão destacados visualmente
- [ ] Não há jargão técnico sem explicação
- [ ] Cada seção tem uma conclusão mini-executiva
- [ ] Recomendações são específicas (não genéricas tipo "melhorar processos")
- [ ] Há equilíbrio entre dados quantitativos e interpretação qualitativa
- [ ] O relatório conta uma história coerente do início ao fim
- [ ] Executivos ocupados podem ler apenas o sumário e entender a situação
- [ ] Há um call-to-action claro ao final

## Como Utilizar Este Prompt

### Para Análise Inicial
```
Use este prompt completo junto com os arquivos de dados para gerar
o relatório executivo completo do setor de marketing.
```

### Para Atualizações Mensais
```
Atualize o relatório executivo do setor de marketing com os dados
mais recentes do Trello. Mantenha a estrutura anterior e adicione
uma seção "Evolução desde o último relatório" comparando KPIs
mês a mês.
```

### Para Análise Focada
```
Gere apenas a seção [X] do relatório executivo de marketing,
com profundidade adicional em [tópico específico].
```

### Para Apresentação para Stakeholders Específicos
```
Adapte o relatório executivo de marketing para apresentação ao
[demandante específico - ex: MSB], focando nas demandas deles
e na performance do setor em atendê-los.
```

## Notas Finais

- Este prompt pode ser usado com LLMs (Claude, GPT-4, etc.) ou como guia para analistas humanos
- Os dados devem ser exportados do Trello regularmente (mensal ou trimestral)
- A metodologia de cálculo deve ser mantida consistente para comparabilidade temporal
- Feedback dos stakeholders deve ser incorporado para refinar análises futuras

---

**Versão:** 1.0
**Data de criação:** 11/11/2025
**Última atualização:** 11/11/2025
**Autor:** Sistema de Análise Trello
