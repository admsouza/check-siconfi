// Função para extrair o valor do parâmetro "id_ente" da URL
function getIdEnteFromURL() {
    const params = new URLSearchParams(window.location.search); // Pega os parâmetros da URL
    return params.get('id_ente'); // Retorna o valor de id_ente
}

// Função para buscar o nome da cidade e UF com base no ID Ente
async function buscarCidade(idEnte) {
    if (!idEnte) {
        document.getElementById('resultado').innerText = 'ID Ente não fornecido na URL.';
        return;
    }

    try {
        // Tenta carregar o arquivo fallback de cidades
        const fallbackData = await fetch('/static/json/cidades_ibge.json').then(response => response.json());

        // Busca o nome da cidade e UF no arquivo fallback local
        const cidadeInfo = fallbackData[idEnte];
        if (cidadeInfo) {
            const cidade = cidadeInfo.cidade;
            const uf = cidadeInfo.uf;
            document.getElementById('resultado').innerText = 
            ` ${cidade} - ${uf}`;
        } else {
            document.getElementById('resultado').innerText = 'Cidade não encontrada nos dados locais.';
        }
    } catch (error) {
        console.error('Erro ao carregar os dados locais:', error);
        document.getElementById('resultado').innerText = 'Erro ao buscar a cidade nos dados locais.';
    }
}

// Função que será executada automaticamente quando a página carregar
window.onload = function() {
    const idEnte = getIdEnteFromURL(); // Captura o id_ente da URL
    buscarCidade(idEnte); // Faz a busca da cidade e UF com o id_ente capturado
}
