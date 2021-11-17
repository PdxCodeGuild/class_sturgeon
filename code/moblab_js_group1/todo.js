const todoInput = document.querySelector(".todo-input")
const todoButton = document.querySelector(".todo-submit")
const todoList = document.querySelector(".todo-list")
const completeList = document.querySelector(".complete-list")
const storageList = []


todoButton.addEventListener('click', function () {
    const todoDiv = document.createElement("div")
    todoDiv.classList.add("todo")
    const newTodo = document.createElement("li")
    newTodo.classList.add("list-item")
    newTodo.innerText = todoInput.value
    storageList.push(todoInput.value)
    

    let deletebutton = document.createElement("button")
    deletebutton.innerText= 'Delete'
    deletebutton.addEventListener('click', function(){
        todoDiv.remove()
        let i = localStorage.getItem('key')
        i = JSON.parse(i)
        i.splice(i.indexOf(todoInput.value))
        localStorage.setItem('key', JSON.stringify(i))
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
    
    localStorage.setItem('key', JSON.stringify(storageList))
    
})

function savedLi (y) {
    const newTodo = document.createElement("li")
    newTodo.classList.add("list-item")
    newTodo.innerText = todoInput.value
    storageList.push(y)

    let deletebutton = document.createElement("button")
    deletebutton.innerText= 'Delete'
    deletebutton.addEventListener('click', function(){
        todoDiv.remove()
        let i = localStorage.getItem('key')
        i = JSON.parse(i)
        i.splice(i.indexOf(todoInput.value))
        localStorage.setItem('key', JSON.stringify(i))
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

}



for (let y of JSON.parse(localStorage.getItem('key'))) {
    savedLi(y)
    //todoList.append(y)
    
}

//localStorage.getItem(todoInput.value)

//for (let x= 0; x < localStorage.length; x++ ) {
    //todoList.append(localStorage.getItem(localStorage.key(x)))
//}
//todoList.forEac((item)=> {
//    todoList()
//})