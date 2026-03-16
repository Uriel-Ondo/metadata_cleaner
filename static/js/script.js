document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("upload-form");
    const fileInput = document.getElementById("file-input");
    const fileNameDisplay = document.getElementById("file-name");
    const submitBtn = document.getElementById("submit-btn");
    const loadingIndicator = document.getElementById("loading");

    // Afficher le nom du fichier sélectionné
    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = fileInput.files[0].name;
        } else {
            fileNameDisplay.textContent = "";
        }
    });

    // Gestion de la soumission : afficher le spinner et désactiver le bouton
    form.addEventListener("submit", function(e) {
        if (!fileInput.files.length) {
            e.preventDefault();
            alert("Veuillez sélectionner un fichier.");
            return;
        }

        // Afficher l'indicateur de chargement
        loadingIndicator.style.display = "flex";
        submitBtn.disabled = true;

        // ❌ NE PAS désactiver l'input file, sinon le fichier ne sera pas envoyé !
        // fileInput.disabled = true;  ← à supprimer
    });
});