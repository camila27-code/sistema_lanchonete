def test_deve_adicionar_observacao(client):

    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})
    client.post("/produtos", json={"codigo": 1, "valor": 10.0, "tipo": 1, "desconto_percentual": 0})
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 5})

    response = client.post(
        "/lanchonete/pedidos/1/observacao",
        json={"observacao": "Sem cebola"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["ok"] == True
    assert data["mensagem"] == "Observação adicionada com sucesso"


def test_nao_deve_aceitar_observacao_vazia(client):
    response = client.post(
        "/lanchonete/pedidos/1/observacao",
        json={"observacao": ""}
    )

    assert response.status_code == 400


def test_nao_deve_adicionar_observacao_em_pedido_finalizado(client):
 
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})
    client.post("/produtos", json={"codigo": 1, "valor": 10.0, "tipo": 1, "desconto_percentual": 0})
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 5})
    client.post("/lanchonete/pedidos/1/finalizar")

    response = client.post(
        "/lanchonete/pedidos/1/observacao",
        json={"observacao": "Sem molho"}
    )

    assert response.status_code == 400


def test_deve_buscar_observacao_pedido(client):
   
    client.post("/clientes", json={"cpf": "11122233344", "nome": "Cliente X"})
    client.post("/produtos", json={"codigo": 1, "valor": 10.0, "tipo": 1, "desconto_percentual": 0})
    client.post("/lanchonete/pedidos", json={"cpf": "11122233344", "cod_produto": 1, "qtd_max_produtos": 5})
    client.post("/lanchonete/pedidos/1/observacao", json={"observacao": "Sem cebola"})
    
    response = client.get("/lanchonete/pedidos/1/observacao")

    assert response.status_code == 200
    data = response.json()
    assert data["codigo"] == 1
    assert data["observacao"] == "Sem cebola"
