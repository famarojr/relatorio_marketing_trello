import json
from collections import defaultdict
from datetime import datetime

# Carregar o JSON do Trello
with open('Vm10BDod - comunicacao-e-marketing.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extrair informações sobre labels
labels_info = {}
if 'labels' in data:
    for label in data['labels']:
        labels_info[label['id']] = {
            'name': label['name'],
            'color': label['color']
        }

# Se não houver labels separadas, extrair de labelNames
if not labels_info and 'labelNames' in data:
    for color, name in data['labelNames'].items():
        if name:  # Apenas labels com nome
            labels_info[color] = {
                'name': name,
                'color': color
            }

# Analisar cards por demandante
demandantes_stats = defaultdict(lambda: {
    'total_cards': 0,
    'cards_abertos': 0,
    'cards_fechados': 0,
    'cards': []
})

# Labels que não são demandantes
excluded_labels = ['Em Alteração']

if 'cards' in data:
    for card in data['cards']:
        # Identificar labels do card
        card_labels = []
        if 'labels' in card:
            for label in card['labels']:
                label_name = label.get('name', '')
                if label_name:
                    # Consolidar GOVONE e EQUANIMUS como o mesmo demandante
                    if label_name == 'GOVONE':
                        label_name = 'EQUANIMUS'
                    # Ignorar labels que não são demandantes
                    if label_name not in excluded_labels:
                        card_labels.append(label_name)

        # Para cada label, adicionar estatísticas
        if card_labels:
            for label_name in card_labels:
                demandantes_stats[label_name]['total_cards'] += 1
                if card.get('closed', False):
                    demandantes_stats[label_name]['cards_fechados'] += 1
                else:
                    demandantes_stats[label_name]['cards_abertos'] += 1

                demandantes_stats[label_name]['cards'].append({
                    'name': card['name'],
                    'url': card.get('shortUrl', ''),
                    'closed': card.get('closed', False),
                    'list': card.get('idList', '')
                })

# Mapear listas
lists_map = {}
if 'lists' in data:
    for lst in data['lists']:
        lists_map[lst['id']] = lst['name']

# Adicionar nome da lista aos cards
for demandante in demandantes_stats:
    for card in demandantes_stats[demandante]['cards']:
        list_id = card['list']
        card['list_name'] = lists_map.get(list_id, 'Desconhecida')

# Ordenar demandantes por número de cards (decrescente)
sorted_demandantes = sorted(demandantes_stats.items(), key=lambda x: x[1]['total_cards'], reverse=True)

# Gerar relatório
print("=" * 80)
print("ANÁLISE DE DEMANDANTES - BOARD TRELLO: Comunicação e Marketing")
print("=" * 80)
print(f"\nTotal de demandantes identificados: {len(sorted_demandantes)}")
print(f"Total de cards no board: {len(data.get('cards', []))}")
print(f"Total de listas: {len(data.get('lists', []))}")

print("\n" + "=" * 80)
print("DEMANDANTES IDENTIFICADOS:")
print("=" * 80)

for demandante, stats in sorted_demandantes:
    print(f"\n{demandante}")
    print(f"  - Total de cards: {stats['total_cards']}")
    print(f"  - Cards abertos: {stats['cards_abertos']}")
    print(f"  - Cards fechados: {stats['cards_fechados']}")

# Gerar arquivo markdown
with open('demandantes.md', 'w', encoding='utf-8') as f:
    f.write("# Análise de Demandantes - Trello Board: Comunicação e Marketing\n\n")
    f.write(f"**Data da análise:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    f.write("---\n\n")

    f.write("## Resumo Geral\n\n")
    f.write(f"- **Total de demandantes identificados:** {len(sorted_demandantes)}\n")
    f.write(f"- **Total de cards no board:** {len(data.get('cards', []))}\n")
    f.write(f"- **Total de listas:** {len(data.get('lists', []))}\n\n")

    f.write("---\n\n")
    f.write("## Lista Completa de Demandantes\n\n")

    for demandante, stats in sorted_demandantes:
        f.write(f"### {demandante}\n\n")
        f.write(f"- **Total de cards:** {stats['total_cards']}\n")
        f.write(f"- **Cards abertos:** {stats['cards_abertos']}\n")
        f.write(f"- **Cards fechados:** {stats['cards_fechados']}\n")

        if stats['cards_abertos'] > 0:
            percentual = (stats['cards_abertos'] / stats['total_cards']) * 100
            f.write(f"- **Percentual de cards abertos:** {percentual:.1f}%\n")

        f.write("\n")

print("\n" + "=" * 80)
print("Arquivo 'demandantes.md' gerado com sucesso!")
print("=" * 80)
