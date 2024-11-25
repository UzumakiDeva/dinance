import { Link } from "react-router-dom"

export function Header(){

    return (
        <div className="row col-12">
            <Link className="mr-2" to="/">Home</Link>
            <Link className="mr-2" to="/add-coin">Add Coin</Link>
            <Link className="mr-2" to="/add-trade-pair">Add Trade Pair</Link>
        </div>
    )
}