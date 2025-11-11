import json
from collections import defaultdict
from datetime import datetime, timedelta
import statistics

# Carregar o JSON do Trello
with open('Vm10BDod - comunicacao-e-marketing.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Listas que indicam conclusão
LISTAS_CONCLUSAO = ['Concluído', 'Concluídos Desing Gráfico', 'Concluídos Design Gráfico']

# Mapeamento de complexidade para peso
PESO_COMPLEXIDADE = {
    'Baixa': 1,
    'Média': 3,
    'Alta': 5
}

# Mapeamento de complexidade para tempo esperado (em horas)
TEMPO_ESPERADO = {
    'Baixa': 5,      # 2-8 horas -> média 5
    'Média': 16,     # 1-3 dias -> média 2 dias = 16h
    'Alta': 56       # 3-10 dias -> média 7 dias = 56h (considerando 8h/dia)
}

# Mapear categorias (será importado da análise anterior)
categorias_keywords = {
    'Design Gráfico - Cards e Artes': {
        'keywords': ['card', 'arte', 'background', 'apoio', 'criação de card', 'design'],
        'complexidade': 'Baixa'
    },
    'Design Gráfico - Apresentações': {
        'keywords': ['apresentação', 'apresentacao', 'slides', 'ppt'],
        'complexidade': 'Média'
    },
    'Design Gráfico - Branding e Identidade Visual': {
        'keywords': ['logo', 'marca', 'identidade', 'branding', 'brand kit', 'uniforme'],
        'complexidade': 'Alta'
    },
    'Design Gráfico - Material Impresso': {
        'keywords': ['panfleto', 'placa', 'impressão', 'brinde', 'certificado', 'faixa'],
        'complexidade': 'Média'
    },
    'Produção de Vídeo - Institucional': {
        'keywords': ['vídeo', 'video', 'roteiro'],
        'complexidade': 'Alta'
    },
    'Produção de Vídeo - Cobertura de Eventos': {
        'keywords': ['cobertura', 'evento'],
        'complexidade': 'Média'
    },
    'Social Media - Copywriting': {
        'keywords': ['copy', 'copywriting', 'calendário'],
        'complexidade': 'Baixa'
    },
    'Eventos e Ações Promocionais': {
        'keywords': ['hackathon', 'hachathon', 'evento', 'capacitação', 'treinamento'],
        'complexidade': 'Alta'
    },
    'Planejamento Estratégico': {
        'keywords': ['planejamento', 'estratégico', 'estrategia', 'plano de ação'],
        'complexidade': 'Alta'
    },
    'Fotografia': {
        'keywords': ['foto', 'fotografia'],
        'complexidade': 'Média'
    },
    'Comunicação Interna': {
        'keywords': ['aniversariante', 'homenagem', 'divulgação interna', 'onboard'],
        'complexidade': 'Baixa'
    },
    'Produtos e Fichas Técnicas': {
        'keywords': ['produto', 'ficha técnica', 'construx'],
        'complexidade': 'Média'
    },
    'Formulários e Processos': {
        'keywords': ['formulário', 'formulario', 'avaliação'],
        'complexidade': 'Baixa'
    }
}

def classificar_card(card_name, card_desc):
    """Classifica um card em uma categoria baseado em palavras-chave"""
    texto_completo = f"{card_name} {card_desc}".lower()

    max_matches = 0
    categoria_encontrada = "Outros Serviços"
    complexidade = "Média"

    for categoria, info in categorias_keywords.items():
        matches = sum(1 for keyword in info['keywords'] if keyword in texto_completo)
        if matches > max_matches:
            max_matches = matches
            categoria_encontrada = categoria
            complexidade = info['complexidade']

    return categoria_encontrada, complexidade

# Mapear listas
lists_map = {}
if 'lists' in data:
    for lst in data['lists']:
        lists_map[lst['id']] = lst['name']

# Labels que não são demandantes
excluded_labels = ['Em Alteração']

# Consolidar demandantes
def get_demandante(labels):
    """Extrai o demandante principal de um card"""
    for label in labels:
        label_name = label.get('name', '')
        if label_name and label_name not in excluded_labels:
            # Consolidar GOVONE em EQUANIMUS
            if label_name == 'GOVONE':
                return 'EQUANIMUS'
            return label_name
    return 'Sem Demandante'

# Primeiro, criar um índice de actions por card
print("=" * 80)
print("ANÁLISE DE MÉTRICAS DE PERFORMANCE - MARKETING")
print("=" * 80)
print("\nProcessando actions...")

actions_por_card = defaultdict(list)
if 'actions' in data:
    for action in data['actions']:
        action_data = action.get('data', {})
        card_data = action_data.get('card', {})
        card_id = card_data.get('id')

        if card_id:
            actions_por_card[card_id].append(action)

print(f"Total de actions encontradas: {len(data.get('actions', []))}")
print(f"Cards com actions: {len(actions_por_card)}")

# Analisar cards e suas métricas
cards_metrics = []
lead_times = []
lead_times_por_complexidade = defaultdict(list)
lead_times_por_categoria = defaultdict(list)
throughput_mensal = defaultdict(int)
cards_por_demandante = defaultdict(lambda: {'concluidos': 0, 'abertos': 0, 'lead_time': []})
cards_por_categoria = defaultdict(lambda: {'concluidos': 0, 'abertos': 0, 'lead_time': [], 'pontos': 0})

print("\nProcessando cards...")

if 'cards' in data:
    for card in data['cards']:
        card_id = card['id']
        card_name = card.get('name', '')
        card_desc = card.get('desc', '')
        card_closed = card.get('closed', False)

        # Classificar o card
        categoria, complexidade = classificar_card(card_name, card_desc)

        # Identificar demandante
        demandante = get_demandante(card.get('labels', []))

        # Buscar data de criação e conclusão nas actions
        date_created = None
        date_completed = None

        # Analisar actions do card
        if card_id in actions_por_card:
            for action in actions_por_card[card_id]:
                action_type = action.get('type', '')
                action_date = action.get('date', '')

                # Identificar criação
                if action_type == 'createCard':
                    created_date = datetime.fromisoformat(action_date.replace('Z', '+00:00'))
                    if date_created is None or created_date < date_created:
                        date_created = created_date

                # Identificar conclusão (movimentação para lista de conclusão)
                if action_type == 'updateCard':
                    action_data = action.get('data', {})
                    list_after = action_data.get('listAfter', {})
                    list_after_name = list_after.get('name', '')

                    if list_after_name in LISTAS_CONCLUSAO:
                        # Pegar a data mais recente de conclusão
                        completed_date = datetime.fromisoformat(action_date.replace('Z', '+00:00'))
                        if date_completed is None or completed_date > date_completed:
                            date_completed = completed_date

        # Se não encontrou nas actions, tentar dateLastActivity para cards fechados
        if date_completed is None and card_closed:
            last_activity = card.get('dateLastActivity')
            if last_activity:
                date_completed = datetime.fromisoformat(last_activity.replace('Z', '+00:00'))

        # Calcular lead time
        lead_time_hours = None
        if date_created and date_completed:
            lead_time_delta = date_completed - date_created
            lead_time_hours = lead_time_delta.total_seconds() / 3600  # converter para horas
            lead_times.append(lead_time_hours)
            lead_times_por_complexidade[complexidade].append(lead_time_hours)
            lead_times_por_categoria[categoria].append(lead_time_hours)

            # Throughput mensal
            mes_conclusao = date_completed.strftime('%Y-%m')
            throughput_mensal[mes_conclusao] += 1

            # Métricas por demandante
            cards_por_demandante[demandante]['concluidos'] += 1
            cards_por_demandante[demandante]['lead_time'].append(lead_time_hours)

            # Métricas por categoria
            cards_por_categoria[categoria]['concluidos'] += 1
            cards_por_categoria[categoria]['lead_time'].append(lead_time_hours)
            cards_por_categoria[categoria]['pontos'] += PESO_COMPLEXIDADE.get(complexidade, 1)

        # Contar abertos
        if not card_closed:
            cards_por_demandante[demandante]['abertos'] += 1
            cards_por_categoria[categoria]['abertos'] += 1

        # Guardar métricas do card
        cards_metrics.append({
            'id': card_id,
            'name': card_name,
            'categoria': categoria,
            'complexidade': complexidade,
            'demandante': demandante,
            'date_created': date_created,
            'date_completed': date_completed,
            'lead_time_hours': lead_time_hours,
            'closed': card_closed
        })

print(f"Total de cards processados: {len(cards_metrics)}")
print(f"Cards com lead time calculado: {len(lead_times)}")

# Calcular estatísticas gerais
total_concluidos = len(lead_times)
total_abertos = sum(1 for c in cards_metrics if not c['closed'])
taxa_conclusao = (total_concluidos / len(cards_metrics) * 100) if cards_metrics else 0

# Lead time médio
lead_time_medio = statistics.mean(lead_times) if lead_times else 0
lead_time_mediano = statistics.median(lead_times) if lead_times else 0

# Throughput médio
throughput_medio = statistics.mean(throughput_mensal.values()) if throughput_mensal else 0

# Calcular eficiência (tempo real vs esperado)
eficiencia_por_complexidade = {}
for complexidade, tempos in lead_times_por_complexidade.items():
    tempo_medio_real = statistics.mean(tempos) if tempos else 0
    tempo_esperado = TEMPO_ESPERADO.get(complexidade, 16)
    eficiencia = (tempo_esperado / tempo_medio_real * 100) if tempo_medio_real > 0 else 0
    eficiencia_por_complexidade[complexidade] = {
        'tempo_medio_real': tempo_medio_real,
        'tempo_esperado': tempo_esperado,
        'eficiencia': eficiencia,
        'quantidade': len(tempos)
    }

# Pontuação total (produtividade ponderada)
pontos_totais = sum(cat['pontos'] for cat in cards_por_categoria.values())

print("\n" + "=" * 80)
print("MÉTRICAS CALCULADAS")
print("=" * 80)
print(f"\nLead Time Médio: {lead_time_medio:.1f} horas ({lead_time_medio/8:.1f} dias úteis)")
print(f"Lead Time Mediano: {lead_time_mediano:.1f} horas ({lead_time_mediano/8:.1f} dias úteis)")
print(f"Throughput Médio: {throughput_medio:.1f} cards/mês")
print(f"Taxa de Conclusão: {taxa_conclusao:.1f}%")
print(f"Pontuação Total (Produtividade): {pontos_totais} pontos")

# Gerar arquivo metricas.md
with open('metricas.md', 'w', encoding='utf-8') as f:
    f.write("# Metodologia e Métricas de Performance - Marketing\n\n")
    f.write(f"**Data da análise:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    f.write("---\n\n")

    # Seção 1: Metodologia
    f.write("## 1. Metodologia de Cálculo\n\n")
    f.write("### 1.1 Definições\n\n")

    f.write("#### Criação de Card (Entrada)\n")
    f.write("```json\n")
    f.write('{\n')
    f.write('  "type": "createCard",\n')
    f.write('  "date": "2025-09-25T13:36:19.678Z"\n')
    f.write('}\n')
    f.write("```\n\n")

    f.write("#### Conclusão de Card (Saída)\n")
    f.write("```json\n")
    f.write('{\n')
    f.write('  "type": "updateCard",\n')
    f.write('  "data": {\n')
    f.write('    "listBefore": { "name": "SOCIAL MÍDIA ( GIORDANO )" },\n')
    f.write('    "listAfter": { "name": "Concluído" }\n')
    f.write('  },\n')
    f.write('  "date": "2025-11-10T12:11:11.336Z"\n')
    f.write('}\n')
    f.write("```\n\n")

    f.write("**Listas consideradas como conclusão:**\n")
    f.write("- Concluído\n")
    f.write("- Concluídos Desing Gráfico\n")
    f.write("- Concluídos Design Gráfico\n\n")

    f.write("### 1.2 Pesos por Complexidade\n\n")
    f.write("| Complexidade | Peso (Pontos) | Tempo Esperado |\n")
    f.write("|--------------|---------------|----------------|\n")
    f.write("| Baixa | 1 | 2-8 horas (média: 5h) |\n")
    f.write("| Média | 3 | 1-3 dias (média: 16h) |\n")
    f.write("| Alta | 5 | 3-10 dias (média: 56h) |\n\n")

    f.write("### 1.3 Fórmulas de Cálculo\n\n")

    f.write("#### Lead Time\n")
    f.write("```\n")
    f.write("Lead Time (horas) = Data de Conclusão - Data de Criação\n")
    f.write("Lead Time (dias úteis) = Lead Time (horas) / 8\n")
    f.write("```\n\n")

    f.write("#### Throughput\n")
    f.write("```\n")
    f.write("Throughput = Número de cards concluídos / Período (mês)\n")
    f.write("```\n\n")

    f.write("#### Taxa de Conclusão\n")
    f.write("```\n")
    f.write("Taxa de Conclusão (%) = (Cards Concluídos / Total de Cards) × 100\n")
    f.write("```\n\n")

    f.write("#### Produtividade (Pontos)\n")
    f.write("```\n")
    f.write("Pontos = Σ (Cards Concluídos × Peso da Complexidade)\n")
    f.write("```\n\n")

    f.write("#### Eficiência\n")
    f.write("```\n")
    f.write("Eficiência (%) = (Tempo Esperado / Tempo Real Médio) × 100\n")
    f.write("• >100% = Equipe entrega mais rápido que o esperado\n")
    f.write("• 100% = Equipe entrega no tempo esperado\n")
    f.write("• <100% = Equipe entrega mais lento que o esperado\n")
    f.write("```\n\n")

    f.write("---\n\n")

    # Seção 2: Indicadores Executivos
    f.write("## 2. Indicadores Executivos (KPIs)\n\n")

    f.write("### 2.1 Indicadores Gerais\n\n")
    f.write("| Indicador | Valor | Interpretação |\n")
    f.write("|-----------|-------|---------------|\n")
    f.write(f"| **Total de Demandas** | {len(cards_metrics)} | Volume total processado |\n")
    f.write(f"| **Demandas Concluídas** | {total_concluidos} | {taxa_conclusao:.1f}% do total |\n")
    f.write(f"| **Demandas em Aberto** | {total_abertos} | Backlog atual |\n")
    f.write(f"| **Taxa de Conclusão** | {taxa_conclusao:.1f}% | Meta: >80% |\n")
    f.write(f"| **Lead Time Médio** | {lead_time_medio:.1f}h ({lead_time_medio/8:.1f} dias) | Tempo médio de entrega |\n")
    f.write(f"| **Lead Time Mediano** | {lead_time_mediano:.1f}h ({lead_time_mediano/8:.1f} dias) | 50% entregues neste tempo |\n")
    f.write(f"| **Throughput Médio** | {throughput_medio:.1f} cards/mês | Capacidade de entrega |\n")
    f.write(f"| **Produtividade (Pontos)** | {pontos_totais} pontos | Pontuação ponderada |\n\n")

    f.write("### 2.2 Performance por Complexidade\n\n")
    f.write("| Complexidade | Qtd | Tempo Real (h) | Tempo Esperado (h) | Eficiência | Status |\n")
    f.write("|--------------|-----|----------------|-------------------|------------|--------|\n")
    for complexidade in ['Baixa', 'Média', 'Alta']:
        if complexidade in eficiencia_por_complexidade:
            info = eficiencia_por_complexidade[complexidade]
            status = "✅ Excelente" if info['eficiencia'] >= 100 else "⚠️ Atenção" if info['eficiencia'] >= 70 else "🔴 Crítico"
            f.write(f"| {complexidade} | {info['quantidade']} | {info['tempo_medio_real']:.1f}h | {info['tempo_esperado']}h | {info['eficiencia']:.1f}% | {status} |\n")
    f.write("\n")

    f.write("### 2.3 Performance por Categoria de Serviço\n\n")
    f.write("| Categoria | Concluídos | Abertos | Lead Time Médio | Pontos |\n")
    f.write("|-----------|------------|---------|-----------------|--------|\n")
    # Ordenar por pontos (produtividade)
    categorias_ordenadas = sorted(cards_por_categoria.items(),
                                  key=lambda x: x[1]['pontos'], reverse=True)
    for categoria, stats in categorias_ordenadas:
        lead_time_cat = statistics.mean(stats['lead_time']) if stats['lead_time'] else 0
        f.write(f"| {categoria} | {stats['concluidos']} | {stats['abertos']} | {lead_time_cat:.1f}h | {stats['pontos']} pts |\n")
    f.write("\n")

    f.write("### 2.4 Performance por Demandante\n\n")
    f.write("| Demandante | Concluídos | Abertos | Lead Time Médio | Taxa de Conclusão |\n")
    f.write("|------------|------------|---------|-----------------|-------------------|\n")
    # Ordenar por total de demandas
    demandantes_ordenados = sorted(cards_por_demandante.items(),
                                   key=lambda x: x[1]['concluidos'] + x[1]['abertos'],
                                   reverse=True)
    for demandante, stats in demandantes_ordenados:
        if demandante == 'Sem Demandante':
            continue
        lead_time_dem = statistics.mean(stats['lead_time']) if stats['lead_time'] else 0
        total_dem = stats['concluidos'] + stats['abertos']
        taxa_dem = (stats['concluidos'] / total_dem * 100) if total_dem > 0 else 0
        f.write(f"| {demandante} | {stats['concluidos']} | {stats['abertos']} | {lead_time_dem:.1f}h | {taxa_dem:.1f}% |\n")
    f.write("\n")

    f.write("### 2.5 Throughput Mensal\n\n")
    f.write("| Mês | Cards Concluídos | Variação |\n")
    f.write("|-----|------------------|----------|\n")
    meses_ordenados = sorted(throughput_mensal.items())
    throughput_anterior = None
    for mes, quantidade in meses_ordenados:
        variacao = ""
        if throughput_anterior is not None:
            diff = quantidade - throughput_anterior
            pct = (diff / throughput_anterior * 100) if throughput_anterior > 0 else 0
            variacao = f"{diff:+d} ({pct:+.1f}%)"
        throughput_anterior = quantidade
        f.write(f"| {mes} | {quantidade} | {variacao} |\n")
    f.write("\n")

    f.write("---\n\n")

    # Seção 3: Análise e Recomendações
    f.write("## 3. Análise Executiva\n\n")

    f.write("### 3.1 Pontos Fortes\n\n")

    # Identificar pontos fortes
    pontos_fortes = []
    if taxa_conclusao >= 70:
        pontos_fortes.append(f"✅ **Alta taxa de conclusão** ({taxa_conclusao:.1f}%) - Equipe finaliza a maioria das demandas iniciadas")

    for complexidade, info in eficiencia_por_complexidade.items():
        if info['eficiencia'] >= 100:
            pontos_fortes.append(f"✅ **Excelente eficiência em demandas de complexidade {complexidade}** ({info['eficiencia']:.1f}%) - Entrega mais rápida que o esperado")

    if throughput_medio >= 20:
        pontos_fortes.append(f"✅ **Alto throughput** ({throughput_medio:.1f} cards/mês) - Boa capacidade de entrega")

    if pontos_fortes:
        for ponto in pontos_fortes:
            f.write(f"{ponto}\n\n")
    else:
        f.write("Análise em andamento - aguardando mais dados históricos.\n\n")

    f.write("### 3.2 Pontos de Atenção\n\n")

    # Identificar pontos de atenção
    pontos_atencao = []
    if taxa_conclusao < 70:
        pontos_atencao.append(f"⚠️ **Taxa de conclusão abaixo do ideal** ({taxa_conclusao:.1f}%) - Meta: >80%")

    if total_abertos > total_concluidos:
        pontos_atencao.append(f"⚠️ **Backlog crescente** ({total_abertos} abertos vs {total_concluidos} concluídos) - Avaliar capacidade da equipe")

    for complexidade, info in eficiencia_por_complexidade.items():
        if info['eficiencia'] < 70:
            pontos_atencao.append(f"🔴 **Baixa eficiência em demandas de complexidade {complexidade}** ({info['eficiencia']:.1f}%) - Tempo real muito superior ao esperado")

    if pontos_atencao:
        for ponto in pontos_atencao:
            f.write(f"{ponto}\n\n")
    else:
        f.write("Nenhum ponto crítico identificado no momento.\n\n")

    f.write("### 3.3 Recomendações Estratégicas\n\n")

    f.write("#### Curto Prazo (1-3 meses)\n\n")
    f.write("1. **Priorização de Backlog**\n")
    f.write("   - Revisar cards abertos e priorizar por impacto estratégico\n")
    f.write("   - Arquivar ou cancelar demandas obsoletas\n")
    f.write("   - Implementar sistema de priorização (Urgente/Importante)\n\n")

    f.write("2. **Otimização de Processos**\n")
    f.write("   - Criar templates para demandas de complexidade Baixa\n")
    f.write("   - Padronizar briefings para reduzir retrabalho\n")
    f.write("   - Implementar checklist de qualidade antes da conclusão\n\n")

    f.write("3. **Capacitação da Equipe**\n")
    f.write("   - Identificar gargalos em categorias com baixa eficiência\n")
    f.write("   - Treinamentos específicos para ferramentas e técnicas\n")
    f.write("   - Redistribuir demandas conforme especialização\n\n")

    f.write("#### Médio Prazo (3-6 meses)\n\n")
    f.write("1. **Gestão de Capacidade**\n")
    f.write("   - Avaliar necessidade de ampliação da equipe\n")
    f.write("   - Considerar parcerias com freelancers para picos de demanda\n")
    f.write("   - Implementar sistema de pontos para planejamento de sprints\n\n")

    f.write("2. **Automação e Ferramentas**\n")
    f.write("   - Automatizar tarefas repetitivas (redimensionamento de imagens, templates)\n")
    f.write("   - Investir em ferramentas que acelerem produção (bibliotecas de assets, IA)\n")
    f.write("   - Melhorar integração entre ferramentas de trabalho\n\n")

    f.write("3. **Cultura de Dados**\n")
    f.write("   - Implementar revisões mensais de KPIs com a equipe\n")
    f.write("   - Criar dashboard de acompanhamento em tempo real\n")
    f.write("   - Estabelecer metas individuais e coletivas baseadas em dados\n\n")

    f.write("#### Longo Prazo (6-12 meses)\n\n")
    f.write("1. **Estruturação Estratégica**\n")
    f.write("   - Revisar catálogo de serviços baseado em demanda real\n")
    f.write("   - Definir SLAs (Service Level Agreements) por tipo de serviço\n")
    f.write("   - Criar roadmap de evolução do setor\n\n")

    f.write("2. **Melhoria Contínua**\n")
    f.write("   - Implementar ciclos de retrospectiva e melhoria\n")
    f.write("   - Benchmarking com outras empresas do setor\n")
    f.write("   - Inovação em processos e metodologias\n\n")

    f.write("---\n\n")

    # Seção 4: Glossário
    f.write("## 4. Glossário de Termos\n\n")

    f.write("- **Lead Time**: Tempo total desde a criação até a conclusão de uma demanda\n")
    f.write("- **Throughput**: Quantidade de demandas concluídas em um período\n")
    f.write("- **Backlog**: Conjunto de demandas em aberto/pendentes\n")
    f.write("- **Taxa de Conclusão**: Percentual de demandas concluídas em relação ao total\n")
    f.write("- **Eficiência**: Relação entre tempo esperado e tempo real de entrega\n")
    f.write("- **Pontos de Produtividade**: Sistema de pontuação ponderada por complexidade\n")
    f.write("- **KPI**: Key Performance Indicator (Indicador-Chave de Performance)\n")
    f.write("- **SLA**: Service Level Agreement (Acordo de Nível de Serviço)\n\n")

    f.write("---\n\n")

    f.write("## 5. Como Utilizar Este Documento\n\n")

    f.write("### Para Gestores\n")
    f.write("- Revise os **Indicadores Executivos** mensalmente\n")
    f.write("- Analise tendências no **Throughput Mensal**\n")
    f.write("- Tome decisões estratégicas baseadas nas **Recomendações**\n")
    f.write("- Acompanhe a **Performance por Demandante** para gestão de relacionamento\n\n")

    f.write("### Para Equipe de Marketing\n")
    f.write("- Utilize a **Performance por Categoria** para identificar especializações\n")
    f.write("- Acompanhe o **Lead Time Médio** das suas demandas\n")
    f.write("- Busque melhorias nas categorias com baixa **Eficiência**\n")
    f.write("- Use os **Pontos de Produtividade** para auto-avaliação\n\n")

    f.write("### Para Demandantes\n")
    f.write("- Consulte o **Catálogo de Serviços** para prazos esperados\n")
    f.write("- Acompanhe sua **Performance individual** como demandante\n")
    f.write("- Planeje suas solicitações considerando o **Throughput** do time\n")
    f.write("- Entenda que demandas de alta complexidade têm lead times maiores\n\n")

print("\n" + "=" * 80)
print("Arquivo 'metricas.md' gerado com sucesso!")
print("=" * 80)
