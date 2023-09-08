import React from "react";
import ProfItem from "./ProfItem";


const Prof = () => {
    return (
        <div>
            <ProfItem 
                name="山田 太郎" 
                userName="yamada" 
                birthday="2000/01/01" 
                image="https://avatars.githubusercontent.com/u/30373425?v=4"
            />
        </div>
    );
}

export default Prof;