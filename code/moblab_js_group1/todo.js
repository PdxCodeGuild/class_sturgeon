const todoInput = document.querySelector("todo-input")
const todoButton = document.querySelector("todo-submit")
const todoList = document.querySelector("todo-list")

todoButton.addEventListener('click', function addTodo() {
    const todoDiv = document.createElement("div")
    todoDiv.classList.add("todo")
    const newTodo = document.createElement("li")
    newTodo.classList.add("list-item")
    newTodo.innerText = todoInput.value
    todoDiv.appendChild(newTodo)
})


