import { use } from "react";

import { Pesquisador } from "@/core/pesquisadores";
import getPesquisadores from "@/services/pesquisadores";

export default function Pesquisadores() {
    const pesquisadores = use(getPesquisadores());

    return (
        <div>
            <h1 className="text-2xl font-bold">Pesquisadores</h1>
            <ul className="flex flex-col gap-3 mt-7">
                {pesquisadores.map((pesquisador: Pesquisador) => (
                    <li
                        className="flex flex-col gap-3 bg-slate-300 px-3 py-2 rounded-md transition-all text-white"
                        key={pesquisador.lattes_id}
                    >
                        <p className="flex justify-between items-center bg-slate-400 rounded-md p-2 mt-2">
                            <span className="text-lg font-semibold">Pesquisador: {pesquisador.nome}</span>
                            <span className="text-lg font-semibold">Pesquisador_id: {pesquisador.pesquisadores_id}</span>
                            <span className="text-lg font-semibold">ID Lattes: {pesquisador.lattes_id}</span>
                        </p>
                        <p className="indent-5 text-black">Sobre o pesquisador: {pesquisador.abstract}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}