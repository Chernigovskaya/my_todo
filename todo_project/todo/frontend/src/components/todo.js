import React from 'react'


const TodoItem= ({todo}) => {
    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.note}</td>
            <td>{todo.text_note}</td>
            <td>{todo.create_date}</td>
            <td>{todo.author}</td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    //console.log(users)
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Note</th>
                <th>Text</th>
                <th>Create</th>
                <th>Author</th>
            </tr>
            {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList
