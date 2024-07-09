function enviarFormulario() {
    document.getElementById("carregandoMsg").style.display = "block";
    document.getElementById("carregando").style.display = "block";

    var formData = {
        materia: parseInt(document.getElementById("materia").value),
        tipo_prova: parseInt(document.getElementById("tipoProva").value),
        dificuldade: parseInt(document.getElementById("dificuldade").value),
        num_questoes: parseInt(document.getElementById("numQuestoes").value)
    };

    fetch('/resource', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById("carregandoMsg").style.display = "none";
        document.getElementById("carregando").style.display = "none";
        document.getElementById("resultado").innerHTML = data;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}