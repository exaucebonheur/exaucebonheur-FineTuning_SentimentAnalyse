import nbformat

# Chemin du notebook original
notebook_path = "Copie_de_distilbert_fine_tune2.ipynb"
# Chemin du notebook nettoyé pour GitHub
clean_path = "Copie_de_distilbert_fine_tune2_GitHub.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Supprimer les widgets
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell.metadata:
        del cell.metadata["widgets"]

# Sauvegarder le notebook nettoyé
with open(clean_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print(f"✅ Notebook prêt pour GitHub : {clean_path}")
