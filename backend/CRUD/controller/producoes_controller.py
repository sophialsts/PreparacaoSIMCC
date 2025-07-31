# controller/producoes_controller.py
from fastapi import APIRouter, HTTPException
from typing import List
from model.producoes import Producoes
from controller.dao.producoes_dao import (
    apagar_por_producoes_id,
    listar_todas,
    salvar_nova_producao,
    atualizar_por_id
)

# Criação de um router chamado 'producoes_router'
producoes_router = APIRouter()

# Rota para salvar uma nova produção
''' @producoes_router.get("/teste", response_model = str)
def oi(): return "teste" '''

@producoes_router.post("/producoes", response_model = Producoes)
def adicionar(producoes: Producoes):
    resposta = salvar_nova_producao(
        
        producoes_id= producoes.producoes_id,
        pesquisadores_id = producoes.pesquisadores_id,
        issn = producoes.issn,
        nomeartigo = producoes.nomeartigo,
        anoartigo = producoes.anoartigo
        
    )
    
    if 'duplicate' in resposta:
        raise HTTPException(status_code=409, detail=resposta)
    if 'Erro' in resposta:
        raise HTTPException(status_code=400, detail=resposta)
    
    return producoes

# Rota para listar todas as producoes
@producoes_router.get("/producoes", response_model = List[Producoes])
def listar():
    producoes = listar_todas()
    return producoes

# Rota para apagar uma produção com base no producoes_id
@producoes_router.delete("/producoes/{producoes_id}", response_model=str)
def apagar(producoes_id: str):
    resposta = apagar_por_producoes_id(producoes_id)
    
    if 'inválido' in resposta:
        raise HTTPException(status_code=400, detail=resposta)
    
    return resposta

# Rota para atualizar uma produção com base no producoes_id
@producoes_router.put("/producoes/{producoes_id}", response_model=Producoes)
def atualizar(producoes_id: str, producoes: Producoes):
    resposta = atualizar_por_id(
        nomeartigo = producoes.nomeartigo,
        issn = producoes.issn,
        anoartigo = producoes.anoartigo,
        pesquisadores_id = producoes.pesquisadores_id,
        producoes_id = producoes.producoes_id
    )
    
    if 'Erro' in resposta:
        raise HTTPException(status_code=400, detail=resposta)
    
    return producoes