import React, {useState, useEffect} from "react";
import useCounter from "./useCounter";

const Max_CAPACITY = 10;

function Accommodate(props) {
    const [isfull, setIsfull] = useState(false);
    const[count, increseCount, decreseCount] = useCounter(0);

    useEffect(()=>{
            console.log("==============")
            console.log("useEffect() is called")
            console.log(`isFull: ${isfull}`)

        });
    useEffect(() => {
        setIsfull(count >= Max_CAPACITY);
        console.log(`Current count value : ${count}`);
    },[count]);
    
    return (
        <div style = {{padding :16}}>
            <p>{` 총 ${count}명 수용했습니다.`}</p>
            <button onClick={increseCount} disabled={isfull}> 입장</button>
            <button onClick={decreseCount}> 퇴장</button>

            {isfull && <p style={{color : "red"}}> 정원이 가득 찼습니다. </p>}

        </div>

    );
}
export default Accommodate