import { use } from "react";
import { Producoes } from "@/core/producoes";
import getProducoes from "@/services/producoes";

export default function Pesquisadores() {
    const pesquisadores = use(getProducoes());

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-6">Produções</h1>
            <ul className="space-y-4">
                {pesquisadores.map((producao: Producoes) => (
                    <li
                        className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow"
                        key={producao.producoes_id}
                    >
                        <div className="space-y-3">
                            <h2 className="text-lg font-semibold text-gray-800">
                                {producao.nomeartigo}
                            </h2>
                            
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm text-gray-600">
                                <div>
                                    <span className="font-medium">ID Pesquisador:</span> {producao.pesquisadores_id}
                                </div>
                                {producao.producoes_id && (
                                    <div>
                                        <span className="font-medium">ID Produção:</span> {producao.producoes_id}
                                    </div>
                                )}
                                <div>
                                    <span className="font-medium">ISSN:</span> {producao.issn}
                                </div>
                                <div>
                                    <span className="font-medium">Ano:</span> {producao.anoartigo}
                                </div>
                            </div>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}