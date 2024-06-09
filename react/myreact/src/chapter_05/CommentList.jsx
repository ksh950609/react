import React from "react";
import Commnet from "./comment";
const comments = [
{
    name: "김상훈",
    comment : "안녕"
},
{
    name: "이상훈",
    comment : "안녕"
},
{
    name: "최상훈",
    comment : ""
},
{
    name: "민상훈",
    comment : ""
},
{
    name: "하상훈",
    comment : ""
}

]
function CommentList(props) {
    return (
            <div>
                {comments.map((comment) => {
                    return (
                        <Commnet name = {comment.name} comment={comment.comment}></Commnet>

                    );

                })}

            </div>
        );
    }
    export default CommentList;