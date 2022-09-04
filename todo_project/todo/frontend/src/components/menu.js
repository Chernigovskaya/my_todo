import React from 'react'

const MenuList = ({users}) => {
    return (
    <div>
    <h1>
        Тo Do
    </h1>
      <ul>
    <li><a href="#">Главная</a></li>
    <li><a href="#">Мои задачи</a>
        <ul>
            <li><a href="#">Задача 1</a></li>
            <li><a href="#">Задача 2</a></li>
            <li><a href="#">задача 3</a></li>
        </ul>
    </li>
    <li><a href="#">Создать новую задачу</a></li>

    </ul>
</div>

    )
}


export default MenuList
