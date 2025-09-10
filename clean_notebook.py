import nbformat

notebook_path = "Copie_de_distilbert_fine_tune2.ipynb"
clean_path = "Copie_de_distilbert_fine_tune2_GitHub.ipynb"

# Charger le notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer tous les widgets et métadonnées inutiles
for cell in nb.cells:
    if hasattr(cell, "metadata"):
        cell.metadata.pop("widgets", None)
        # Supprime d'autres metadata qui posent problème
        cell.metadata.pop("tags", None)
        cell.metadata.pop("execution", None)

# Sauvegarder le notebook nettoyé
with open(clean_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"✅ Notebook prêt pour GitHub : {clean_path}")
