document.getElementById('uf').addEventListener('change', function() {
    var uf = this.value;
    var enteSelect = document.getElementById('ente');
    enteSelect.innerHTML = '<option value="">Selecione uma cidade</option>';
    document.getElementById('id_ente').value = ''; // Limpa o input IBGE

    var loadingText = document.getElementById('loading-text');
    loadingText.classList.remove('d-none'); // Mostra o texto de carregamento

    if (uf) {
        console.log('UF selecionada:', uf);

        fetch(`/get_cidades/${uf}`)
            .then(response => {
                console.log('Status da resposta:', response.status);
                return response.json();
            })
            .then(data => {
                console.log('Cidades recebidas:', data);

                data.forEach(item => {
                    var option = document.createElement('option');
                    option.value = item.cod_ibge; // Define cod_ibge como valor da opção
                    option.textContent = item.ente; // Define o nome da cidade como texto da opção
                    enteSelect.appendChild(option);
                });
                enteSelect.disabled = false; // Habilita o campo de cidades
                loadingText.classList.add('d-none'); // Oculta o texto de carregamento
            })
            .catch(error => {
                console.error('Erro ao buscar cidades:', error);
                loadingText.classList.add('d-none'); // Oculta o texto de carregamento em caso de erro
            });
    } else {
        enteSelect.disabled = true;
        loadingText.classList.add('d-none'); // Oculta o texto de carregamento se UF não for selecionada
    }
});

document.getElementById('ente').addEventListener('change', function() {
    var cod_ibge = this.value; // Obter o cod_ibge selecionado
    document.getElementById('id_ente').value = cod_ibge; // Definir o valor do input IBGE
});

// Envio do formulário
document.getElementById('enviar-formulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    // Obtém os valores dos campos necessários
    var id_ente = document.getElementById('id_ente').value;
    var an_referencia = document.getElementById('an_referencia').value; // Certifique-se de que este campo existe

    console.log('id_ente:', id_ente);
    console.log('an_referencia:', an_referencia);

    // Envia os dados ao backend
    fetch('/enviar_parans', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            id_ente: id_ente,
            an_referencia: an_referencia // Adiciona o ano de referência
        }),
    })
    .then(response => {
        console.log('Status da resposta ao enviar parâmetros:', response.status);
        if (response.ok) {
            window.location.href = '/dimensionii'; // Redireciona para a página dimensionii
        } else {
            console.error('Erro ao enviar parâmetros:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Erro ao enviar parâmetros:', error);
    });
});
