# 📊 RESUMEN DE GRÁFICOS DISPONIBLES EN EL PROYECTO

## ✅ **GRÁFICOS QUE YA ESTÁN IMPLEMENTADOS:**

### 1. **PARTE 1 - Priscilla (Preprocesamiento):**

#### ✅ Forma de onda (Cell 4)
- **Archivo**: `waveform_example.png`
- **Ubicación**: `/content/waveform_example.png`
- **Descripción**: Muestra la señal de audio en el dominio temporal
- **Propósito**: Visualizar la estructura temporal del audio original

#### ✅ Espectrograma lineal (Cell 4)
- **Archivo**: `spectrogram_linear_example.png`
- **Ubicación**: `/content/spectrogram_linear_example.png`
- **Descripción**: Espectrograma logarítmico (STFT) con escala de frecuencias logarítmica
- **Propósito**: Visualizar energía en dominio tiempo-frecuencia antes de Mel

#### ✅ Espectrograma Mel (Cell 4)
- **Archivo**: `spectrogram_mel_example.png`
- **Ubicación**: `/content/spectrogram_mel_example.png`
- **Descripción**: Espectrograma con escala Mel (128 bandas)
- **Propósito**: Representación usada para entrenar los modelos CNN

#### ✅ Comparativa original vs aumentado (Cell 6)
- **Archivo**: `comparativa_espectrogramas_from_disk.png`
- **Ubicación**: `/content/comparativa_espectrogramas_from_disk.png`
- **Descripción**: Comparación lado a lado de espectrograma crudo vs aumentado
- **Propósito**: Demostrar el efecto de las técnicas de data augmentation

### 2. **PARTE 2 - Fabián (Entrenamiento):**

#### ✅ Curvas de aprendizaje por escenario
- **Archivos**: `A_crudo_specaug-off_curvas.png`, `A_aumentado_specaug-on_curvas.png`, etc.
- **Ubicación**: `runs/curvas_aprendizaje/*.png`
- **Descripción**: Curvas de loss y accuracy para train/val de cada uno de los 4 escenarios
- **Nota**: ✅ **AHORA SE GUARDAN AUTOMÁTICAMENTE**

### 3. **PARTE 3 - David (Evaluación):**

#### ✅ Gráfico comparativo de Accuracy (Cell 14)
- **Archivo**: `comparative_results.png`
- **Ubicación**: `/content/comparative_results.png`
- **Descripción**: Gráfico de barras comparando accuracy de los 4 escenarios

#### ✅ Gráfico comparativo de Loss (Cell 14)
- **Archivo**: `comparative_results.png`
- **Ubicación**: `/content/comparative_results.png`
- **Descripción**: Gráfico de barras comparando loss de los 4 escenarios

---

## 📋 **GRÁFICOS TOTALES GENERADOS:**

### **Para el Informe IEEE:**

| # | Gráfico | Uso en Documento | Celda |
|---|---------|------------------|-------|
| 1 | Forma de onda | Figura 1 - Visualización temporal | Cell 4 |
| 2 | Espectrograma lineal | Figura 2 - STFT logarítmico | Cell 4 |
| 3 | Espectrograma Mel | Figura 3 - Mel con escala humana | Cell 4 |
| 4 | Comparativa crudo/aug | Figura 4 - Efecto de augmentación | Cell 6 |
| 5-8 | Curvas de aprendizaje | Figura 5 - Curvas por escenario | Cell 11 (ahora automático) |
| 9 | Comparativa de resultados | Figura 6 - Accuracy y Loss comparativos | Cell 14 |

---

## ✅ **RESUMEN:**

**TOTAL DE GRÁFICOS: 9+**
- ✅ 4 gráficos de preprocesamiento (Parte 1)
- ✅ 4 curvas de aprendizaje individuales (Parte 2) - **AHORA AUTOMÁTICO**
- ✅ 1 gráfico comparativo final (Parte 3)

### **Lo que hace automático ahora:**

1. **Ejecutas `run_all_scenarios()`**
2. **Se entrenan los 4 modelos**
3. **Se generan Y GUARDAN automáticamente** las 4 curvas de aprendizaje
4. **Se ejecuta el análisis comparativo**
5. **Se generan los gráficos comparativos finales**

### **Ubicaciones de archivos:**

```
📁 Archivos en /content/:
  - waveform_example.png
  - spectrogram_linear_example.png
  - spectrogram_mel_example.png
  - comparativa_espectrogramas_from_disk.png
  - comparative_results.png

📁 Archivos en runs/:
  - A_crudo_specaug-off.pt
  - A_aumentado_specaug-on.pt
  - B_crudo_specaug-off.pt
  - B_aumentado_specaug-on.pt

📁 Archivos en runs/curvas_aprendizaje/:
  - A_crudo_specaug-off_curvas.png
  - A_aumentado_specaug-on_curvas.png
  - B_crudo_specaug-off_curvas.png
  - B_aumentado_specaug-on_curvas.png
```

---

## ✅ **CONCLUSIÓN:**

**SÍ, el proyecto tiene TODOS los gráficos necesarios** según lo requerido en el PDF del proyecto. 

Ahora con el cambio realizado, **las curvas de aprendizaje se guardan automáticamente** cada vez que entrenas un modelo, lo que es perfecto para el informe.


