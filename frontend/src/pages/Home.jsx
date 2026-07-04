import InputBar from "../container/InputBar.jsx";
import "./Home.css"

function Home(){


    return (
        <>
            <div className="home-wrapper">
            <h1> Url-Shortener </h1>
                <InputBar/>
            </div>
        </>
    )
}

export default Home;