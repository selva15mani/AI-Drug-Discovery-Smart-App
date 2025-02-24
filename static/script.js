async function predictDrug() {
    const smiles = document.getElementById("smiles").value;
    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ smiles: smiles })
    });
    const result = await response.json();
    document.getElementById("result").innerHTML = JSON.stringify(result, null, 2);
}