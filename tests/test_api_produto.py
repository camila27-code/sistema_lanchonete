import pytest

def test_put_produto_atualiza_valor(client):
   
    client.post("/produtos", json={"codigo": 1, "valor": 10.0, "tipo": 1, "desconto_percentual": 0})
   
    r = client.put("/produtos/1/valor", json={"valor": 25.0})

    assert r.status_code == 200
    assert r.json() == {"alterou": True}
