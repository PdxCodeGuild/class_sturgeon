//selectors
const todoInput = document.querySelector('.todo-input');
const todoButton = document.querySelector('.todo-button');
const todoList = document.querySelector('.todo-list');

//event listeners
todoButton.addEventListener('click', addTodo);
todoList = addEventListener('click', deleteCheck);

//Functions

function addTodo(event) {
    //Prevent form from submitting
    event.preventDefault()
    //Todo DIV
    const todoDiv = document.createElement("div")
    todoDiv.classList.add("todo")
    //Create li
    const newTodo = document.createElement('li')
    newTodo.innerText = todoInput.value
    newTodo.classList.add('todo-item')
    todoDiv.appendChild(newTodo)
    //Check mark button
    const completedButton = document.createElement('button')
    completedButton.innerHTML = '<img class="check-icon" src="https://img.icons8.com/external-kiranshastry-solid-kiranshastry/64/000000/external-check-multimedia-kiranshastry-solid-kiranshastry.png"/>'
    completedButton.classList.add("complete-btn")
    todoDiv.appendChild(completedButton)
    //check trash button
    const trashButton = document.createElement('button')
    trashButton.innerHTML = '<img class="trash-icon" src="https://img.icons8.com/windows/32/000000/trash.png"/>'
    trashButton.classList.add("trash-btn")
    todoDiv.appendChild(trashButton)
    //append to list
    todoList.appendChild(todoDiv)
    //clear
    todoInput.value = ""
}

function deleteCheck(e) {
    const item = e.target;
    //delete todo
    if(item.classList[0] === 'trash-btn'){
        const todo = item.parentElement;
        //animation
        todo.classList.add("fall")
        todo.addEventListener('transtioned', function() {
            todo.remove()
        })

    };

    //check mark
    if(item.classList[0] === 'complete-btn') {
        const todo = item.parentElement
        todo.classList.toggle("completed")
    }
}