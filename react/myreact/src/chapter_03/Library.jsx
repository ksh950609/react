import Book from "./Book";
import react from "react";

function Library(props) {
return (
    <div>
<Book name = "처음 만난 파이썬" numOfPage={300}/>
<Book name = "처음 만난 Aws" numOfPage={400}/>
<Book name = "처음 만난 JS" numOfPage={500}/>
    </div>
);
}
export default Library;