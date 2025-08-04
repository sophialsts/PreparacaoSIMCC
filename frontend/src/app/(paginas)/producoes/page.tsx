import { use } from "react";

import { Producoes } from "@/core/producoes";
import getProducoes from "@/services/producoes";

export default function Pesquisadores() {
    const pesquisadores = use(getProducoes());

    return (
        <div>
            <h1 className="text-2xl font-bold">Produções</h1>
            <ul className="flex flex-col gap-3 mt-7">
                {pesquisadores.map((producao: Producoes) => (
                    <li
                        className="flex flex-col gap-3 bg-slate-300 px-3 py-2 rounded-md transition-all text-white"
                        key={producao.producoes_id}
                    >
                        <p className="flex justify-between items-center bg-slate-400 rounded-md p-2 mt-2">
                            <span className="text-lg font-semibold">Nome do artigo: {producao.nomeartigo}</span>
                            <span className="text-lg font-semibold">Pesquisador_id: {producao.pesquisadores_id}</span>
                            <span className="text-lg font-semibold">ISSN: {producao.issn}</span>
                            <span className="text-lg font-semibold">ID Produção: {producao.producoes_id}</span>
                            <span className="text-lg font-semibold">Ano do artigo: {producao.anoartigo}</span>
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    );
}