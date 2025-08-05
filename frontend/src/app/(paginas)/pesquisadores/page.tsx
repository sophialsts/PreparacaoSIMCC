import { use } from "react";
import { Pesquisador } from "@/core/pesquisadores";
import getPesquisadores from "@/services/pesquisadores";

export default function Pesquisadores() {
    const pesquisadores = use(getPesquisadores());

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-6">Pesquisadores</h1>
            <ul className="space-y-4">
                {pesquisadores.map((pesquisador: Pesquisador) => (
                    <li
                        className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow"
                        key={pesquisador.lattes_id}
                    >
                        <div className="space-y-3">
                            <h2 className="text-lg font-semibold text-gray-800">
                                {pesquisador.nome}
                            </h2>
                            
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-gray-600">
                                <div>
                                    <span className="font-medium">ID Pesquisador:</span> {pesquisador.pesquisadores_id}
                                </div>
                                <div>
                                    <span className="font-medium">ID Lattes:</span> {pesquisador.lattes_id}
                                </div>
                            </div>
                            
                            {pesquisador.abstract && (
                                <div className="pt-2">
                                    <p className="text-sm text-gray-700">
                                        <span className="font-medium">Sobre o pesquisador:</span> {pesquisador.abstract}
                                    </p>
                                </div>
                            )}
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}