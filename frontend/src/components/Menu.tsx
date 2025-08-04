import MenuItem from "./MenuItem";

export default function Menu() {
    return (
        <div
            className="
                bg-[#153050] h-screen
            "
        >
            <ul className="flex flex-col gap-3 mt-7">
                <MenuItem link="/">
                    Início
                </MenuItem>
                <MenuItem link="/pesquisadores">
                    Pesquisadores
                </MenuItem>
                <MenuItem link="/producoes">
                    Produções
                </MenuItem>
            </ul>

        </div>
    )
}