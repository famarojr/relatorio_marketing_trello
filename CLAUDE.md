# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Trello Marketing Analytics System that processes board exports to generate executive insights and performance metrics for the Marketing and Communication department.

## Core Commands

### Running Analysis Scripts
```bash
# Extract and analyze stakeholders/requesters from Trello data
python analyze_trello.py

# Classify services and categorize demands by complexity
python classify_services.py  

# Calculate performance metrics (Lead Time, Throughput, Efficiency)
python calculate_metrics.py
```

### Script Execution Order
Always run in this sequence: `analyze_trello.py` → `classify_services.py` → `calculate_metrics.py`

## Architecture

### Data Flow
1. **Input**: Trello board JSON export (`Vm10BDod - comunicacao-e-marketing.json`)
2. **Processing**: Three Python scripts analyze different aspects
3. **Output**: Markdown reports with metrics and catalogs

### Key Processing Logic

#### analyze_trello.py
- Extracts stakeholders from card labels
- Consolidates GOVONE as EQUANIMUS
- Excludes "Em Alteração" label from stakeholder analysis
- Generates `demandantes.md` with stakeholder statistics

#### classify_services.py  
- Categorizes cards into 14 service types
- Assigns complexity levels (Low=1pt, Medium=3pts, High=5pts)
- Maps complexity to time estimates (Low: 2-8hrs, Medium: 1-3 days, High: 3-10 days)
- Generates `catalogo_servicos_mkt.md` with service catalog

#### calculate_metrics.py
- Calculates Lead Time from card creation to completion
- Measures Throughput (completed cards per period)
- Computes Efficiency scores and productivity metrics
- Considers cards in "Concluído" or "Concluídos Design Gráfico" lists as completed
- Generates `metricas.md` with executive KPIs

## Data Structure

### Expected JSON Format
The Trello export must contain:
- `cards`: Array with card details (name, labels, closed status, dates)
- `lists`: Board columns/lists
- `labels`: Stakeholder/category identifiers  
- `actions`: Activity history for metric calculations
- `members`: Board collaborators

### Stakeholder Labels
Primary stakeholders identified through labels:
- MSB, KOGNI, EQUANIMUS (includes GOVONE), GRIX, SIMPLIFIXA, SE7TI, LSG business hub

## Important Notes

- JSON files are not versioned (see `.gitignore`)
- All scripts use Python standard library only - no external dependencies
- Scripts expect exact filename: `Vm10BDod - comunicacao-e-marketing.json`
- Metrics are based on card movements to completion lists