# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Trello analysis project that works with Trello board exports. The repository contains Trello board data in JSON format exported from the Trello API.

## Data Structure

### Trello Board JSON Format

The primary data file is a Trello board export containing:
- **Board metadata**: id, name, description, organization details, URL
- **Board preferences**: permissions, background settings, view configurations
- **Lists**: Board columns/lists with their cards
- **Cards**: Individual task cards with details, attachments, checklists, members, labels
- **Members**: Board collaborators and their permissions
- **Labels**: Color-coded categories (e.g., "MSB", "GRIX", "SE7TI", "EQUANIMUS", "KOGNI", "LSG business hub")
- **Checklists**: Task checklists within cards
- **Actions**: Activity history and card movements
- **Custom fields**: Additional metadata fields

### File Naming Convention

Trello export files follow the pattern: `{boardId} - {board-name}.json`
- Example: `Vm10BDod - comunicacao-e-marketing.json`

## Working with Trello Data

When analyzing or processing Trello exports:
1. The JSON is typically a single-line file (no pretty-printing) and can be very large (2MB+)
2. Parse the entire JSON structure to understand board organization
3. Key entities to focus on: `lists` (columns), `cards` (tasks), `actions` (history), `members` (people), `labels` (categories)
4. Card relationships: cards belong to lists, contain checklists/attachments, and have activity tracked in actions

## Future Development Considerations

This codebase will likely evolve to include:
- Python scripts for parsing and analyzing Trello data
- Data visualization tools
- Reporting and analytics functionality
- Potentially database integration for structured querying
