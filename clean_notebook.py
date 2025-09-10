import nbformat

# Nom du notebook à nettoyer
input_nb = "Copie_de_distilbert_fine_tune2_GitHub.ipynb"
output_nb = "Copie_de_distilbert_fine_tune2_GitHub.ipynb"

# Charger le notebook
with open(input_nb, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer les widgets et nettoyer les outputs
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

for cell in nb.cells:
    if "outputs" in cell:
        # Garder les outputs pour qu’ils soient visibles
        cell.outputs = cell.outputs
    if "execution_count" in cell:
        cell.execution_count = cell.execution_count
    if "metadata" in cell:
        # Supprimer seulement les parties problématiques des métadonnées
        cell.metadata.pop("widgets", None)

# Sauvegarder le notebook nettoyé
with open(output_nb, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"✅ Notebook nettoyé et compatible GitHub : {output_nb}")
