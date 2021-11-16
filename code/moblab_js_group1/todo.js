const todoInput = document.querySelector(".todo-input")
const todoButton = document.querySelector(".todo-submit")
const todoList = document.querySelector(".todo-list")
const completeList = document.querySelector(".complete-list")

todoButton.addEventListener('click', function () {
    const todoDiv = document.createElement("div")
    todoDiv.classList.add("todo")
    const newTodo = document.createElement("li")
    newTodo.classList.add("list-item")
    newTodo.innerText = todoInput.value
    

    let deletebutton = document.createElement("button")
    deletebutton.innerText= 'Delete'
    deletebutton.addEventListener('click', function(){
        todoDiv.remove()
    })

   
    let completebutton = document.createElement("button")
    completebutton.innerText= 'Complete'
    completebutton.addEventListener('click', function(){
        completebutton.remove()
        completeList.appendChild(todoDiv)
    })


    todoDiv.appendChild(newTodo)
    todoDiv.appendChild(deletebutton)
    todoDiv.appendChild(completebutton)

    todoList.appendChild(todoDiv)
    


})