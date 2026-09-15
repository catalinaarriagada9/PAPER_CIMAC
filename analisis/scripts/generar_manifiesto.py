from __future__ import annotations

import csv
import hashlib
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "documentacion" / "MANIFIESTO_ARCHIVOS.csv"
EXCLUIR = {".git", ".venv", "__pycache__"}


def sha256(ruta: Path) -> str:
    resumen = hashlib.sha256()
    with ruta.open("rb") as archivo:
        for bloque in iter(lambda: archivo.read(1024 * 1024), b""):
            resumen.update(bloque)
    return resumen.hexdigest()


def main() -> None:
    archivos = []
    for ruta in sorted(RAIZ.rglob("*")):
        if not ruta.is_file() or any(parte in EXCLUIR for parte in ruta.parts):
            continue
        if ruta == SALIDA or ruta.suffix.lower() in {".aux", ".log", ".out"}:
            continue
        archivos.append((ruta.relative_to(RAIZ).as_posix(), ruta.stat().st_size, sha256(ruta)))

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with SALIDA.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ruta", "tamano_bytes", "sha256"])
        escritor.writerows(archivos)
    print(f"Manifiesto generado con {len(archivos)} archivos: {SALIDA}")


if __name__ == "__main__":
    main()
