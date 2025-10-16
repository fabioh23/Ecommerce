import mercadopago

public_key = 'APP_USR-41b7fcb5-8739-416c-ada1-fdfc448837f6'
token = 'APP_USR-5145113925314765-100909-3443289cf9169791f642e9f47b3e2c91-2915372244'

def criar_pagamento(itens_pedido, link):
    #configure as credenciais
    sdk = mercadopago.SDK(token)
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = item.item_estoque.produto.preco
        itens.append(
            {
                "title": nome_produto,
                "quantity": quantidade,
                "unit_price": float(preco_unitario),
            }
        )

    #cria um item na preferencia
    preference_data = {
        "items": itens,
        # "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }

    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    return(link_pagamento, id_pagamento)