import { useState } from "react";
import axios from "axios"
import { Header } from "./Header";

export function AddCoin(){
    const [formData,setFormData] = useState({
        name:"",
        symbol:""
    })
    const handleChange = function(e){
        setFormData({
            ...formData,
            [e.target.name]:e.target.value
        })
    }

    const handleSubmit = async function(e){
        e.preventDefault()

        axios.post("http://127.0.0.1:5000/add_coin",JSON.stringify(formData),{
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
            <h2>Welcome to AddCoin page.</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                ></input>
                <input
                    type="text"
                    name="symbol"
                    value={formData.symbol}
                    onChange={handleChange}
                ></input>
                <button type="submit">Add</button>
            </form>
        </div>
    )
}