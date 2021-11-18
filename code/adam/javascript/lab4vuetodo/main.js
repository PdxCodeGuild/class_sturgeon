Vue.component('todo-item', {
	props: ['todo'],
	template: 
            `<li>
                <span :class="{'done': isDone}" @click="toggleDone">
                    {{ todo.text }}
                </span>
                <button @click="$emit('edit-todo', todo, todo.id)" class="button1">
                    Edit
                </button>
                <button @click="$emit('remove-todo', todo)" class="button">
                    Delete
                </button>
            </li>`, 
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
        message: "Don't procrastinate now, git 'er done!",
        isEditing: false,
        todo: '',
        edit_id: "",
        todos: [
            { 
                id: 0, 
                text: "This is a default list item: Wash the dishes", 
                isDone: false
            },
            { 
                id: 1, 
                text: "This is a default list item: Wash the laundry", 
                isDone: false
            }
        ],
        selectedTodo: null
    },

// I'm trying something here

    mounted() {
        if (localStorage.todos) {
            this.todos = JSON.parse(localStorage.todos);
        }
    },
    watch: {
        todos(storeTodos) {
            localStorage.todos = JSON.stringify(storeTodos);
        }
    },
    

// Let's see if it works! UPDATE!!!!! It WORKS!!!! Local storage is a thing! Wahooo!!!!!

    methods: {
        storeTodo(todo) {
            if (this.todo.length > 3) {
            console.log(todo)
            id_value = this.todos.length
            this.todos.push({id:id_value, isDone:false, text:this.todo})
            this.todo = ''
        }},

        removeTodo(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },

        updateTodo() {
            // this.todos.splice(this.edit_id, 1, this.todo)
            this.todos[this.edit_id].text=this.todo
            console.log(this.todos[this.edit_id])
            this.todo = ''
            this.isEditing = false
        },

        editTodo(todo, id) {
            this.isEditing = true
            this.todo = todo.text
            this.edit_id = id
            console.log(id)
            // something about this being an indexof to make it work
        },

        toggleDone() {
            console.log(this)
            this.isDone = !this.isDone
        }
    }
})