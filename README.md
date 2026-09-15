# PAPER CIMAC

Repositorio reproducible del manuscrito **Assessing Plastic-Packaging Circularity in Chile: EPR Performance, Data Gaps, and Measurement Readiness**, preparado para evaluación en *Journal of Cleaner Production*.

El estudio examina dos preguntas relacionadas: qué indicadores de circularidad de envases plásticos pueden estimarse con las fuentes públicamente accesibles auditadas en Chile y si dichas fuentes poseen la disponibilidad, granularidad, continuidad y compatibilidad necesarias para una evaluación nacional defendible. El año de referencia es 2024; 2025 se conserva como extensión provisional.

## Contenido

```text
manuscrito/       Manuscrito principal en LaTeX
suplemento/       Material suplementario en LaTeX
datos/            Libro de cálculo procesado y documentación de variables
analisis/         Scripts de verificación y generación de resultados
figuras/          Figuras utilizadas por el manuscrito
fuentes/          Inventario de fuentes externas y política de redistribución
documentacion/    Matriz de estrategia y decisiones de reproducibilidad
```

## Resultados de referencia para 2024

- Tasa total de reciclaje de plásticos: 10,3 %.
- Tasa estimada de reciclaje de envases plásticos: 13,0 %.
- IC_REP_est: 82,0 %. Es una estimación del estudio, no una certificación oficial de cumplimiento.
- eC, interpretado como material gestionado respecto del insumo de resina virgen: PET 21,9 %, PP 31,9 % y PE 16,9 %.
- IRP agregado: 0,174775 Mt CO2eq. Es un potencial teórico condicionado por los factores de emisión y el supuesto de desplazamiento, no una reducción observada.
- MCI: no calculado por falta de variables compatibles para residuos no recuperados, pérdidas de proceso y utilidad del producto.

## Reproducción

Se requiere Python 3.10 o posterior.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requisitos.txt
python3 analisis/scripts/verificar_indicadores.py
python3 analisis/scripts/generar_figura_disponibilidad.py
python3 analisis/scripts/generar_manifiesto.py
```

El script de verificación escribe resultados tabulares en `analisis/resultados/` y termina con un código distinto de cero cuando encuentra diferencias respecto de los valores declarados para 2024.

## Compilación del manuscrito

Desde la raíz del repositorio:

```bash
cd manuscrito
pdflatex main.tex
pdflatex main.tex
cd ../suplemento
pdflatex material_suplementario.tex
pdflatex material_suplementario.tex
```

La plantilla usa la clase Elsevier `elsarticle`. La instalación de LaTeX debe incluir `elsarticle`, `booktabs`, `longtable`, `graphicx`, `hyperref`, `url`, `array`, `ragged2e` y los demás paquetes declarados en cada archivo.

## Alcance de los datos

El libro publicado en `datos/procesados/` contiene valores reportados, derivados e imputados. Cada tratamiento debe interpretarse según sus hojas de trazabilidad y validación. Las imputaciones no son observaciones y los escenarios de sensibilidad no son intervalos de confianza.

Los documentos externos no se redistribuyen automáticamente. `fuentes/inventario_fuentes.csv` conserva los enlaces y el estado de acceso utilizados en la auditoría.

## Cita y licencia

La forma provisional de cita está en `CITATION.cff`. Debe actualizarse con el DOI y los metadatos editoriales cuando estén disponibles.

El contenido permanece bajo derechos de sus autores hasta que el equipo investigador apruebe una licencia pública específica. Véase `LICENCIA.md`.
