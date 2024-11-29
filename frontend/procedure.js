// End da API
const API_PROCEDURE = "http://127.0.0.1:5000/produtos/procedure";

// Função para enviar os dados para a procedure
async function addProdutoViaProcedure(produto) {

    try {
        const response = await fetch(API_PROCEDURE, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(produto) // Converte o objeto JS para JSON
        });

        if (!response.ok) {
            console.error("Erro ao inserir produto via procedure", response.status);
            return;
        }

        const result = await response.json();
        console.log(result.message); // Exibe a mensagem de sucesso
    } catch (error) {
        console.error("Erro ao chamar a procedure:", error);
    }
}
// aqui acaba a função


const formProduto = document.querySelector("#formProduto");
    

formProduto.addEventListener("submit", async (e) => {
    e.preventDefault();

    const produto = {
        nome: document.querySelector("#nome").value,
        marca: document.querySelector("#marca").value,
        valor: parseFloat(document.querySelector("#valor").value)
    };

    await addProdutoViaProcedure(produto);
    formProduto.reset(); // Limpa o formulário após a inserção
});

