#!/usr/bin/env python3
"""
Script para arreglar el notebook eliminando el return innecesario
"""
import json

# Leer el notebook
with open('Proyecto01_RedesNeuronales_Espectrogramas.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Buscar y arreglar
for cell in nb['cells']:
    if 'source' in cell:
        source = ''.join(cell['source'])
        
        # Arreglar el return en analyze_results
        if 'return best_acc, best_loss' in source:
            cell['source'] = [line.replace('return best_acc, best_loss', '# No retornar nada') for line in cell['source']]
        
        # Arreglar la llamada en execute_complete_pipeline
        if 'best_acc, best_loss = analyze_results(results)' in source:
            cell['source'] = [line.replace('best_acc, best_loss = analyze_results(results)', 'analyze_results(results)') for line in cell['source']]

# Guardar
with open('Proyecto01_RedesNeuronales_Espectrogramas.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook arreglado")

