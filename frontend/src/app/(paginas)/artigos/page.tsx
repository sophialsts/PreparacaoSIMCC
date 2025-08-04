import { Artigo } from "@/core/artigos";
import getArtigos from "@/services/artigos"
import { use } from "react"

export default function Artigos() {

    const artigos = use(getArtigos());

    return (
        <div>
            <h1 className="text-2xl font-bold">Artigos</h1>

            <ul>
                {artigos.map((artigo: Artigo) => (
                    <li
                        className="flex flex-col gap-3 bg-slate-300 px-3 py-2 rounded-md transition-all text-white mt-7"
                        key={artigo.doi}
                    >
                        <p className="bg-slate-400 rounded-md p-2 mt-2">Título: {artigo.title}</p>
                        <p className="flex justify-between items-center text-black">
                            <p>Autor: {artigo.researcher}</p>
                            <p>Qualis: {artigo.qualis}</p>
                            <p>Ano de publicação: {artigo.year}</p>
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    )
}