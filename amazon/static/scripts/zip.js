document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.querySelector('input[name="zip_code"]');

    if (cepInput) {
        cepInput.addEventListener("input", function (e) {
            let value = cepInput.value.replace(/\D/g, ''); // Remove tudo que não é número

            if (value.length > 5) {
                value = value.slice(0, 5) + '-' + value.slice(5, 8);
            }

            cepInput.value = value.slice(0, 9);
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.querySelector('input[name="zip_code"]');
    const cityInput = document.querySelector('input[name="city"]');
    const stateSelect = document.querySelector('select[name="state"]');
    const addressInput = document.querySelector('input[name="address"]');

    cepInput.addEventListener("blur", function () {
        const cep = cepInput.value.replace(/\D/g, '');
        if (cep.length !== 8) return;

        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(res => res.json())
            .then(data => {
                if (data.erro) {
                    alert("CEP não encontrado.");
                    return;
                }

                cityInput.value = data.localidade || "";
                addressInput.value = data.logradouro || "";

                // Seleciona o estado na <select>
                for (const option of stateSelect.options) {
                    if (option.value === data.uf) {
                        option.selected = true;
                        break;
                    }
                }
            })
            .catch(() => alert("Erro ao buscar o CEP."));
    });
});

