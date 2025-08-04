const url: string =
  "http://localhost:8000/producoes";

const getProducoes = async () => {
  const resposta = await fetch(url, {
    method: "GET",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!resposta.ok) {
    throw new Error("Não foi possível buscar as produções.");
  }

  return resposta.json();
};

export default getProducoes;
