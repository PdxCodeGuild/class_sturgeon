Vue.component('todo-item', {
	props: ['todo'],
	template: `<li :class="{'done': isDone}" @click="toggleDone">{{ todo.text }}<button @click="$emit('remove-todo', todo)">Delete!</button><button @click="$emit('edit-todo', todo)">Edit!</button></li>`, 
    data () {
        return {
            isDone: false,
            }
        },
    methods: {
        toggleDone() {
            this.isDone = !this.isDone;
        },
    },

})

var app1 = new Vue({
    el: '#app-todolist',
    data: {
        isEditing: false,
        todo: '',
        todos: [
            // "This is a default list item: Go to the gym",
            // "This is a default list item: Make your bed",
            { id: 1, text: "This is a default list item: Wash the dishes", isDone: false},
            { id: 2, text: "This is a default list item: Wash the laundry", isDone: false}
        ],
        selectedTodo: null
    },
    
    methods: {
        storeTodo() {
            this.todos.push(this.todo)
            this.todo = ''
        },

        removeTodo(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },

        updateTodo() {
            this.todos.splice(this.selectedIndex, 1, this.todo)
            this.todo = ''
            this.isEditing = false
        },

        editTodo(todo) {
            this.isEditing = true
            this.todo = todo
            this.selectedIndex = index
            // something about this being an indexof to make it work
        },

        toggleDone() {
            console.log(this)
            this.isDone = !this.isDone
        }
    }
})