import { useState } from "react";
import { Header } from "./Header";
import axios from "axios"

export function AddTradePair(){
    const [formData,setFormData] = useState({
        symbol: "",
        price: 0
    })

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        })
    }

    const handleSubmit = async function(e){
        e.preventDefault()
        axios.post("http://127.0.0.1:5000/add_trade_pair",JSON.stringify(formData),{
            "headers":{
            "Content-Type":"application/json"
            }
        }).then((res)=>{
            console.log(res.data)
        })
    }
    return (
        <div className="row">
           <Header/> 
           <div className="col-12">
                <form onSubmit={handleSubmit}>
                    <lable>Enter Symbol:</lable>
                    <input
                        name="symbol"
                        value={formData.symbol}
                        type="text"
                        onChange={handleChange}
                    />

                    <lable>Enter price:</lable>
                    <input
                        name="price"
                        value={formData.price}
                        type="number"
                    />
                    <button type="submit">Add</button>
                </form>
           </div>
        </div>
    )
}