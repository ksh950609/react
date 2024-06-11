import React, {useState} from "react"

function ConfirmButtonFunction(props) {
    const[isConfirmed, setIsconfirmed] = useState(false);

    const handleConfirm = () => {
        setIsconfirmed((prevIsConfirmed) => !prevIsConfirmed );

    };
    return(
        <button
        onClick={handleConfirm}
        disabled={isConfirmed}
    >
        {isConfirmed ? "확인됨":"확인하기"}
    </button>
    );
}
export default ConfirmButtonFunction  