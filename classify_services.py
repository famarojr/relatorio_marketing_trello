import json
import re
from collections import defaultdict
from datetime import datetime

# Carregar o JSON do Trello
with open('Vm10BDod - comunicacao-e-marketing.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Definir categorias e palavras-chave para classificação
categorias = {
    'Design Gráfico - Cards e Artes': {
        'keywords': ['card', 'arte', 'background', 'apoio', 'criação de card', 'design'],
        'exemplos': [],
        'complexidade': 'Baixa'
    },
    'Design Gráfico - Apresentações': {
        'keywords': ['apresentação', 'apresentacao', 'slides', 'ppt'],
        'exemplos': [],
        'complexidade': 'Média'
    },
    'Design Gráfico - Branding e Identidade Visual': {
        'keywords': ['logo', 'marca', 'identidade', 'branding', 'brand kit', 'uniforme'],
        'exemplos': [],
        'complexidade': 'Alta'
    },
    'Design Gráfico - Material Impresso': {
        'keywords': ['panfleto', 'placa', 'impressão', 'brinde', 'certificado', 'faixa'],
        'exemplos': [],
        'complexidade': 'Média'
    },
    'Produção de Vídeo - Institucional': {
        'keywords': ['vídeo', 'video', 'roteiro'],
        'exemplos': [],
        'complexidade': 'Alta'
    },
    'Produção de Vídeo - Cobertura de Eventos': {
        'keywords': ['cobertura', 'evento'],
        'exemplos': [],
        'complexidade': 'Média'
    },
    'Social Media - Copywriting': {
        'keywords': ['copy', 'copywriting', 'calendário'],
        'exemplos': [],
        'complexidade': 'Baixa'
    },
    'Eventos e Ações Promocionais': {
        'keywords': ['hackathon', 'hachathon', 'evento', 'capacitação', 'treinamento'],
        'exemplos': [],
        'complexidade': 'Alta'
    },
    'Planejamento Estratégico': {
        'keywords': ['planejamento', 'estratégico', 'estrategia', 'plano de ação'],
        'exemplos': [],
        'complexidade': 'Alta'
    },
    'Fotografia': {
        'keywords': ['foto', 'fotografia'],
        'exemplos': [],
        'complexidade': 'Média'
    },
    'Comunicação Interna': {
        'keywords': ['aniversariante', 'homenagem', 'divulgação interna', 'onboard'],
        'exemplos': [],
        'complexidade': 'Baixa'
    },
    'Produtos e Fichas Técnicas': {
        'keywords': ['produto', 'ficha técnica', 'construx'],
        'exemplos': [],
        'complexidade': 'Média'
    },
    'Formulários e Processos': {
        'keywords': ['formulário', 'formulario', 'avaliação'],
        'exemplos': [],
        'complexidade': 'Baixa'
    }
}

# Estatísticas por categoria
stats_por_categoria = defaultdict(lambda: {
    'total': 0,
    'abertos': 0,
    'fechados': 0,
    'exemplos': []
})

# Classificar cada card
cards_classificados = []

if 'cards' in data:
    for card in data['cards']:
        card_name = card.get('name', '').lower()
        card_desc = card.get('desc', '').lower()
        texto_completo = f"{card_name} {card_desc}"

        # Tentar classificar em uma categoria
        categoria_encontrada = None
        max_matches = 0

        for categoria, info in categorias.items():
            matches = sum(1 for keyword in info['keywords'] if keyword in texto_completo)
            if matches > max_matches:
                max_matches = matches
                categoria_encontrada = categoria

        # Se não encontrou nenhuma palavra-chave, classificar como "Outros"
        if max_matches == 0:
            categoria_encontrada = "Outros Serviços"

        # Adicionar aos stats
        stats_por_categoria[categoria_encontrada]['total'] += 1
        if card.get('closed', False):
            stats_por_categoria[categoria_encontrada]['fechados'] += 1
        else:
            stats_por_categoria[categoria_encontrada]['abertos'] += 1

        # Guardar exemplos (máximo 3 por categoria)
        if len(stats_por_categoria[categoria_encontrada]['exemplos']) < 3:
            stats_por_categoria[categoria_encontrada]['exemplos'].append(card.get('name', ''))

        cards_classificados.append({
            'nome': card.get('name', ''),
            'categoria': categoria_encontrada,
            'closed': card.get('closed', False)
        })

# Ordenar categorias por total de demandas
categorias_ordenadas = sorted(stats_por_categoria.items(), key=lambda x: x[1]['total'], reverse=True)

# Gerar relatório no console
print("=" * 80)
print("ANÁLISE DE CLASSIFICAÇÃO DE SERVIÇOS - BOARD TRELLO")
print("=" * 80)
print(f"\nTotal de cards analisados: {len(cards_classificados)}")
print(f"Total de categorias identificadas: {len(categorias_ordenadas)}")

print("\n" + "=" * 80)
print("DISTRIBUIÇÃO POR CATEGORIA:")
print("=" * 80)

for categoria, stats in categorias_ordenadas:
    print(f"\n{categoria}")
    print(f"  - Total: {stats['total']} demandas")
    print(f"  - Abertos: {stats['abertos']}")
    print(f"  - Fechados: {stats['fechados']}")

# Gerar arquivo markdown do catálogo
with open('catalogo_servicos_mkt.md', 'w', encoding='utf-8') as f:
    f.write("# Catálogo de Serviços - Marketing e Comunicação\n\n")
    f.write(f"**Data da análise:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")
    f.write("---\n\n")

    f.write("## Resumo Executivo\n\n")
    f.write(f"Este catálogo foi gerado através da análise de **{len(cards_classificados)} demandas** ")
    f.write(f"do board Trello \"Comunicação e Marketing\", identificando padrões e categorizando os serviços prestados.\n\n")

    f.write("### Distribuição de Demandas por Categoria\n\n")
    f.write("| Categoria | Total de Demandas | % do Total |\n")
    f.write("|-----------|-------------------|------------|\n")
    for categoria, stats in categorias_ordenadas:
        percentual = (stats['total'] / len(cards_classificados)) * 100
        f.write(f"| {categoria} | {stats['total']} | {percentual:.1f}% |\n")

    f.write("\n---\n\n")

    # Seção detalhada de cada categoria
    f.write("## Catálogo Detalhado de Serviços\n\n")

    for categoria, stats in categorias_ordenadas:
        f.write(f"### {categoria}\n\n")

        # Buscar complexidade se estiver nas categorias predefinidas
        complexidade = "Não definida"
        tempo_estimado = "Variável"

        if categoria in categorias:
            complexidade = categorias[categoria]['complexidade']

            # Estimar tempo baseado na complexidade
            if complexidade == "Baixa":
                tempo_estimado = "2-8 horas"
            elif complexidade == "Média":
                tempo_estimado = "1-3 dias"
            elif complexidade == "Alta":
                tempo_estimado = "3-10 dias"

        f.write(f"**Complexidade:** {complexidade}  \n")
        f.write(f"**Tempo Estimado:** {tempo_estimado}  \n")
        f.write(f"**Volume de Demandas:** {stats['total']} ({stats['abertos']} abertos, {stats['fechados']} concluídos)\n\n")

        # Descrição baseada na categoria
        descricoes = {
            'Design Gráfico - Cards e Artes':
                "Criação de artes gráficas para redes sociais, cards informativos, backgrounds para reuniões e materiais de apoio visual. "
                "Inclui peças comemorativas, divulgações internas e comunicados visuais.",

            'Design Gráfico - Apresentações':
                "Desenvolvimento de apresentações corporativas, slides para reuniões comerciais, atas, onboarding e apresentações estratégicas. "
                "Inclui diagramação, aplicação de identidade visual e organização de conteúdo.",

            'Design Gráfico - Branding e Identidade Visual':
                "Criação e desenvolvimento de marcas, logotipos, identidade visual corporativa, manuais de marca (brand kits) e aplicações em diversos materiais. "
                "Serviço estratégico que define a presença visual da empresa.",

            'Design Gráfico - Material Impresso':
                "Criação de materiais para impressão física incluindo panfletos, placas, certificados, brindes corporativos, uniformes e faixas. "
                "Inclui preparação de arquivos para gráficas e fornecedores.",

            'Produção de Vídeo - Institucional':
                "Produção de vídeos institucionais, divulgação de produtos/serviços, capacitação tecnológica e conteúdo estratégico. "
                "Inclui roteirização, gravação, edição e pós-produção.",

            'Produção de Vídeo - Cobertura de Eventos':
                "Registro audiovisual de eventos corporativos, capacitações, hackathons, celebrações e ações internas. "
                "Inclui captação de imagens, edição e entrega de material final.",

            'Social Media - Copywriting':
                "Produção de textos para redes sociais, calendário editorial, planejamento de conteúdo e redação publicitária. "
                "Foco em engajamento e comunicação efetiva com o público-alvo.",

            'Eventos e Ações Promocionais':
                "Planejamento e execução de eventos corporativos, hackathons, capacitações, treinamentos e ações promocionais. "
                "Inclui logística, divulgação, cobertura e pós-evento.",

            'Planejamento Estratégico':
                "Desenvolvimento de planejamento estratégico de marketing, definição de planos de ação, levantamento de demandas e estruturação de processos. "
                "Serviço consultivo e de alto nível estratégico.",

            'Fotografia':
                "Serviços de fotografia profissional para eventos, produtos, equipes e materiais institucionais. "
                "Inclui tratamento e entrega de imagens em alta qualidade.",

            'Comunicação Interna':
                "Ações de endomarketing incluindo comunicados para aniversariantes, homenagens, divulgações internas e materiais de onboarding. "
                "Foco no engajamento e valorização da equipe interna.",

            'Produtos e Fichas Técnicas':
                "Desenvolvimento de materiais técnicos de produtos, fichas descritivas, catálogos e documentação comercial. "
                "Inclui levantamento de informações e diagramação profissional.",

            'Formulários e Processos':
                "Criação de formulários de avaliação, solicitação e processos estruturados para coleta de informações e gestão de demandas.",

            'Outros Serviços':
                "Demandas que não se enquadram nas categorias principais ou serviços específicos não catalogados."
        }

        if categoria in descricoes:
            f.write(f"**Descrição:**  \n{descricoes[categoria]}\n\n")

        # Adicionar exemplos reais
        if stats['exemplos']:
            f.write(f"**Exemplos de Demandas:**\n\n")
            for exemplo in stats['exemplos']:
                f.write(f"- {exemplo}\n")
            f.write("\n")

        # Adicionar diretrizes de entrega
        f.write(f"**Diretrizes de Entrega:**\n\n")

        if 'Design Gráfico' in categoria:
            f.write("- Arquivos em alta resolução (PNG, JPG) e editáveis (AI, PSD, FIGMA)\n")
            f.write("- Aplicação correta da identidade visual\n")
            f.write("- Revisão de textos e ortografia\n")
            f.write("- Até 2 rodadas de ajustes incluídas\n")
        elif 'Vídeo' in categoria:
            f.write("- Formato MP4 em resolução Full HD (1080p) ou 4K\n")
            f.write("- Legendas quando aplicável\n")
            f.write("- Versões para diferentes plataformas (Instagram, YouTube, LinkedIn)\n")
            f.write("- Até 1 rodada de ajustes incluída\n")
        elif 'Copywriting' in categoria:
            f.write("- Textos revisados e alinhados com o tom de voz da marca\n")
            f.write("- Sugestões de hashtags quando aplicável\n")
            f.write("- Calendário organizado por datas e temas\n")
        elif 'Eventos' in categoria:
            f.write("- Planejamento detalhado com cronograma\n")
            f.write("- Materiais de divulgação completos\n")
            f.write("- Cobertura fotográfica e/ou audiovisual\n")
            f.write("- Relatório pós-evento\n")
        elif 'Planejamento' in categoria:
            f.write("- Documento estruturado com diagnóstico e ações\n")
            f.write("- Cronograma de implementação\n")
            f.write("- Definição de KPIs e métricas de sucesso\n")
            f.write("- Apresentação executiva para gestores\n")
        else:
            f.write("- Entrega conforme briefing acordado\n")
            f.write("- Materiais em formatos apropriados\n")
            f.write("- Revisões conforme necessário\n")

        f.write("\n---\n\n")

    # Adicionar seção de observações
    f.write("## Observações Importantes\n\n")
    f.write("### Processo de Solicitação\n\n")
    f.write("1. **Briefing:** Toda demanda deve ser acompanhada de briefing detalhado\n")
    f.write("2. **Priorização:** Demandas são priorizadas conforme urgência e impacto estratégico\n")
    f.write("3. **Prazos:** Os tempos estimados são baseados na complexidade e disponibilidade da equipe\n")
    f.write("4. **Aprovações:** Todas as entregas passam por aprovação do solicitante\n\n")

    f.write("### Níveis de Complexidade\n\n")
    f.write("- **Baixa:** Demandas simples e rápidas, geralmente com templates predefinidos\n")
    f.write("- **Média:** Demandas que exigem criação customizada e pesquisa prévia\n")
    f.write("- **Alta:** Demandas estratégicas que demandam planejamento extenso e múltiplas etapas\n\n")

    f.write("### Demandantes Ativos\n\n")
    f.write("Os principais demandantes identificados no board são:\n\n")
    f.write("1. MSB (82 demandas)\n")
    f.write("2. KOGNI (45 demandas)\n")
    f.write("3. EQUANIMUS (31 demandas)\n")
    f.write("4. GRIX (21 demandas)\n")
    f.write("5. SIMPLIFIXA (13 demandas)\n")
    f.write("6. SE7TI (12 demandas)\n")
    f.write("7. LSG business hub (1 demanda)\n\n")

print("\n" + "=" * 80)
print("Arquivo 'catalogo_servicos_mkt.md' gerado com sucesso!")
print("=" * 80)
