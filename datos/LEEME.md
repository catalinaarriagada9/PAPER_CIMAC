# Datos

## Archivo vigente

`procesados/Datos_CIMAC_procesados.xlsx` es el único libro de cálculo vigente para reproducir el manuscrito.

El archivo contiene nueve hojas:

- `Metas_REP`: metas normativas utilizadas en IC_REP_est.
- `Emisiones`: factores de emisión para PET, PP y PE.
- `Actualizado`: series agregadas, población y tratamientos anuales.
- `Resinas`: material gestionado e insumos vírgenes por resina.
- `Desarrollo de indicadores`: fórmulas de TR, Tgr, IC_REP_est, eC e IRP.
- `Trazabilidad_ASIPLA`: procedencia y tratamiento de datos sectoriales.
- `Indicadores_validados`: resultados consolidados.
- `Validacion_paper`: contraste con valores reportados en el manuscrito.
- `Notas_validacion`: decisiones metodológicas y límites de interpretación.

## Reglas de interpretación

- MCI figura como no calculado; no existe una serie MCI válida en este repositorio.
- eC se calcula como material gestionado dividido por insumo virgen de la misma resina y año.
- IRP se calcula para PET, PP y PE con factores constantes por resina y se interpreta como potencial teórico.
- PS no forma parte de los indicadores publicados.
- Los valores 2025 que dependen de traslado conservador no constituyen observaciones anuales independientes.

No sobrescriba este archivo. Cualquier transformación debe generar un archivo nuevo dentro de una rama o propuesta de cambio y quedar documentada.
