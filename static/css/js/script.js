document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const table = document.getElementById('tabelaRamais');
    const tr = table.getElementsByTagName('tr');

    searchInput.addEventListener('keyup', function() {
        const filter = searchInput.value.toLowerCase();

        // Começa do índice 1 para pular o cabeçalho (thead)
        for (let i = 1; i < tr.length; i++) {
            let tds = tr[i].getElementsByTagName('td');
            let found = false;

            // Verifica se o texto digitado existe em alguma das colunas da linha
            for (let j = 0; j < tds.length; j++) {
                if (tds[j]) {
                    if (tds[j].textContent.toLowerCase().indexOf(filter) > -1) {
                        found = true;
                        break;
                    }
                }
            }

            // Mostra ou esconde a linha
            if (found) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    });
});