document.getElementById('uf').addEventListener('change', function() {
    var uf = this.value;
    var enteSelect = document.getElementById('ente');
    enteSelect.innerHTML = '<option value="">Selecione uma cidade</option>';
    document.getElementById('id_ente').value = ''; // Limpa o input IBGE

    var loadingText = document.getElementById('loading-text');
    loadingText.classList.remove('d-none'); // Mostra o texto de carregamento

    if (uf) {
        // Adicionando log para depuração
        console.log('UF selecionada:', uf);

        fetch(`/get_cidades/${uf}`)
            .then(response => {
                // Adicionando log para depuração do status da resposta
                console.log('Status da resposta:', response.status);
                return response.json();
            })
            .then(data => {
                // Adicionando log para depuração dos dados recebidos
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
                // Adiciona log para possíveis erros na chamada fetch
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
