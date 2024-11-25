import { Link } from "react-router-dom"
import { useEffect,useState } from "react"
import {Header} from "./Header"

export function Home(){

    const [coins,setCoins] = useState([])
    useEffect(() => {
        const fetchCoins = async () => {
            try {
              const response = await fetch('/get_coins'); // Replace with your API endpoint
              const data = await response.json();
              setCoins(data); // Update the state with the fetched data
            } catch (error) {
              console.error('Error fetching coins:', error);
            }
        };

        fetchCoins();
    },[])

    return (
        <div className="w-full row">
            <h2>Welcome to Home page.</h2>
            <Header/>
            <div className="col-12">
                <h1>Coins</h1>
                <ul>
                    {coins.map((coin, index) => (
                    <li key={index}>
                        {coin.name.toUpperCase()} ({coin.symbol})
                    </li>
                    ))}
                </ul>
            </div>
        </div>
    )
}