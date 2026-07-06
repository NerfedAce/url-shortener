import {useState} from "react";
import "./InputBar.css"
const Api = import.meta.env.VITE_API_URl;

function InputBar(){
    const [url , setUrl] = useState("");
    const [shorturl, setShorturl] = useState("No Update");
    const [state, setState] = useState(null)
    const generateUrl = async () => {
        const response = await fetch(`${Api}/api/short_url`) // change url
        const data = await response.json();
        setShorturl(data)
    }
    const submitUrl = async () => {
        const response = await fetch(`${Api}/api/submit_url`,
            {method: "POST" , headers:{"content-type": "application/json"} , body: JSON.stringify({short_url: shorturl.short_url,long_url:url,clicks:0,region:""} )});
        const x = await response.json();
        console.log(response.status);
        setState(x.message);

    }


    return (
        <>
            <div className="input-bar">
                <input placeholder="enter the url" value={url} onChange={(e) => setUrl(e.target.value)} />
                <button className="enter" onClick={() => generateUrl()}>Enter</button>
                <button className="submit" onClick={() => {submitUrl()}} > Submit </button>
                <button className="reset" onClick={() => {setUrl("") , setShorturl("")}}>Reset</button>
                <div className="short-url">
                    <h2> Suggested Url </h2>
                    {shorturl &&
                        (<h2>{shorturl.short_url}</h2>)
                    }
                </div>
                <div className="submitUpdate">
                    <h2> Status : </h2>
                    {state &&
                        (<h2>{state}</h2>)
                    }
                </div>
            </div>
        </>
    )
}

export default InputBar;