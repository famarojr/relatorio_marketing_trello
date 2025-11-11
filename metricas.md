# Metodologia e Métricas de Performance - Marketing

**Data da análise:** 11/11/2025 16:16:58

---

## 1. Metodologia de Cálculo

### 1.1 Definições

#### Criação de Card (Entrada)
```json
{
  "type": "createCard",
  "date": "2025-09-25T13:36:19.678Z"
}
```

#### Conclusão de Card (Saída)
```json
{
  "type": "updateCard",
  "data": {
    "listBefore": { "name": "SOCIAL MÍDIA ( GIORDANO )" },
    "listAfter": { "name": "Concluído" }
  },
  "date": "2025-11-10T12:11:11.336Z"
}
```

**Listas consideradas como conclusão:**
- Concluído
- Concluídos Desing Gráfico
- Concluídos Design Gráfico

### 1.2 Pesos por Complexidade

| Complexidade | Peso (Pontos) | Tempo Esperado |
|--------------|---------------|----------------|
| Baixa | 1 | 2-8 horas (média: 5h) |
| Média | 3 | 1-3 dias (média: 16h) |
| Alta | 5 | 3-10 dias (média: 56h) |

### 1.3 Fórmulas de Cálculo

#### Lead Time
```
Lead Time (horas) = Data de Conclusão - Data de Criação
Lead Time (dias úteis) = Lead Time (horas) / 8
```

#### Throughput
```
Throughput = Número de cards concluídos / Período (mês)
```

#### Taxa de Conclusão
```
Taxa de Conclusão (%) = (Cards Concluídos / Total de Cards) × 100
```

#### Produtividade (Pontos)
```
Pontos = Σ (Cards Concluídos × Peso da Complexidade)
```

#### Eficiência
```
Eficiência (%) = (Tempo Esperado / Tempo Real Médio) × 100
• >100% = Equipe entrega mais rápido que o esperado
• 100% = Equipe entrega no tempo esperado
• <100% = Equipe entrega mais lento que o esperado
```

---

## 2. Indicadores Executivos (KPIs)

### 2.1 Indicadores Gerais

| Indicador | Valor | Interpretação |
|-----------|-------|---------------|
| **Total de Demandas** | 267 | Volume total processado |
| **Demandas Concluídas** | 63 | 23.6% do total |
| **Demandas em Aberto** | 132 | Backlog atual |
| **Taxa de Conclusão** | 23.6% | Meta: >80% |
| **Lead Time Médio** | 282.2h (35.3 dias) | Tempo médio de entrega |
| **Lead Time Mediano** | 191.2h (23.9 dias) | 50% entregues neste tempo |
| **Throughput Médio** | 21.0 cards/mês | Capacidade de entrega |
| **Produtividade (Pontos)** | 197 pontos | Pontuação ponderada |

### 2.2 Performance por Complexidade

| Complexidade | Qtd | Tempo Real (h) | Tempo Esperado (h) | Eficiência | Status |
|--------------|-----|----------------|-------------------|------------|--------|
| Baixa | 15 | 348.8h | 5h | 1.4% | 🔴 Crítico |
| Média | 29 | 313.9h | 16h | 5.1% | 🔴 Crítico |
| Alta | 19 | 181.4h | 56h | 30.9% | 🔴 Crítico |

### 2.3 Performance por Categoria de Serviço

| Categoria | Concluídos | Abertos | Lead Time Médio | Pontos |
|-----------|------------|---------|-----------------|--------|
| Produção de Vídeo - Institucional | 12 | 18 | 163.3h | 60 pts |
| Outros Serviços | 14 | 33 | 313.4h | 42 pts |
| Design Gráfico - Apresentações | 7 | 15 | 271.2h | 21 pts |
| Design Gráfico - Branding e Identidade Visual | 3 | 12 | 281.5h | 15 pts |
| Produção de Vídeo - Cobertura de Eventos | 5 | 6 | 151.8h | 15 pts |
| Eventos e Ações Promocionais | 3 | 6 | 191.9h | 15 pts |
| Design Gráfico - Cards e Artes | 13 | 25 | 318.9h | 13 pts |
| Design Gráfico - Material Impresso | 2 | 4 | 477.7h | 6 pts |
| Planejamento Estratégico | 1 | 4 | 65.9h | 5 pts |
| Fotografia | 1 | 1 | 1102.6h | 3 pts |
| Formulários e Processos | 1 | 3 | 404.2h | 1 pts |
| Social Media - Copywriting | 1 | 1 | 681.3h | 1 pts |
| Produtos e Fichas Técnicas | 0 | 4 | 0.0h | 0 pts |

### 2.4 Performance por Demandante

| Demandante | Concluídos | Abertos | Lead Time Médio | Taxa de Conclusão |
|------------|------------|---------|-----------------|-------------------|
| MSB | 30 | 37 | 266.3h | 44.8% |
| KOGNI | 9 | 24 | 320.4h | 27.3% |
| EQUANIMUS | 4 | 9 | 304.8h | 30.8% |
| GRIX | 2 | 1 | 369.2h | 66.7% |
| LSG business hub | 1 | 1 | 0.0h | 50.0% |
| SE7TI | 0 | 1 | 0.0h | 0.0% |

### 2.5 Throughput Mensal

| Mês | Cards Concluídos | Variação |
|-----|------------------|----------|
| 2025-09 | 17 |  |
| 2025-10 | 34 | +17 (+100.0%) |
| 2025-11 | 12 | -22 (-64.7%) |

---

## 3. Análise Executiva

### 3.1 Pontos Fortes

✅ **Alto throughput** (21.0 cards/mês) - Boa capacidade de entrega

### 3.2 Pontos de Atenção

⚠️ **Taxa de conclusão abaixo do ideal** (23.6%) - Meta: >80%

⚠️ **Backlog crescente** (132 abertos vs 63 concluídos) - Avaliar capacidade da equipe

🔴 **Baixa eficiência em demandas de complexidade Média** (5.1%) - Tempo real muito superior ao esperado

🔴 **Baixa eficiência em demandas de complexidade Alta** (30.9%) - Tempo real muito superior ao esperado

🔴 **Baixa eficiência em demandas de complexidade Baixa** (1.4%) - Tempo real muito superior ao esperado

### 3.3 Recomendações Estratégicas

#### Curto Prazo (1-3 meses)

1. **Priorização de Backlog**
   - Revisar cards abertos e priorizar por impacto estratégico
   - Arquivar ou cancelar demandas obsoletas
   - Implementar sistema de priorização (Urgente/Importante)

2. **Otimização de Processos**
   - Criar templates para demandas de complexidade Baixa
   - Padronizar briefings para reduzir retrabalho
   - Implementar checklist de qualidade antes da conclusão

3. **Capacitação da Equipe**
   - Identificar gargalos em categorias com baixa eficiência
   - Treinamentos específicos para ferramentas e técnicas
   - Redistribuir demandas conforme especialização

#### Médio Prazo (3-6 meses)

1. **Gestão de Capacidade**
   - Avaliar necessidade de ampliação da equipe
   - Considerar parcerias com freelancers para picos de demanda
   - Implementar sistema de pontos para planejamento de sprints

2. **Automação e Ferramentas**
   - Automatizar tarefas repetitivas (redimensionamento de imagens, templates)
   - Investir em ferramentas que acelerem produção (bibliotecas de assets, IA)
   - Melhorar integração entre ferramentas de trabalho

3. **Cultura de Dados**
   - Implementar revisões mensais de KPIs com a equipe
   - Criar dashboard de acompanhamento em tempo real
   - Estabelecer metas individuais e coletivas baseadas em dados

#### Longo Prazo (6-12 meses)

1. **Estruturação Estratégica**
   - Revisar catálogo de serviços baseado em demanda real
   - Definir SLAs (Service Level Agreements) por tipo de serviço
   - Criar roadmap de evolução do setor

2. **Melhoria Contínua**
   - Implementar ciclos de retrospectiva e melhoria
   - Benchmarking com outras empresas do setor
   - Inovação em processos e metodologias

---

## 4. Glossário de Termos

- **Lead Time**: Tempo total desde a criação até a conclusão de uma demanda
- **Throughput**: Quantidade de demandas concluídas em um período
- **Backlog**: Conjunto de demandas em aberto/pendentes
- **Taxa de Conclusão**: Percentual de demandas concluídas em relação ao total
- **Eficiência**: Relação entre tempo esperado e tempo real de entrega
- **Pontos de Produtividade**: Sistema de pontuação ponderada por complexidade
- **KPI**: Key Performance Indicator (Indicador-Chave de Performance)
- **SLA**: Service Level Agreement (Acordo de Nível de Serviço)

---

## 5. Como Utilizar Este Documento

### Para Gestores
- Revise os **Indicadores Executivos** mensalmente
- Analise tendências no **Throughput Mensal**
- Tome decisões estratégicas baseadas nas **Recomendações**
- Acompanhe a **Performance por Demandante** para gestão de relacionamento

### Para Equipe de Marketing
- Utilize a **Performance por Categoria** para identificar especializações
- Acompanhe o **Lead Time Médio** das suas demandas
- Busque melhorias nas categorias com baixa **Eficiência**
- Use os **Pontos de Produtividade** para auto-avaliação

### Para Demandantes
- Consulte o **Catálogo de Serviços** para prazos esperados
- Acompanhe sua **Performance individual** como demandante
- Planeje suas solicitações considerando o **Throughput** do time
- Entenda que demandas de alta complexidade têm lead times maiores

