new Vue ({
    el: '#app', 
    data: {
        todo:[
            {id:1, text: "wash the dog", complete: true},
            {id:2, text: "pet the dog", complete: false},
            {id:3, text: "cook the dog", complete: false},
        ],
        newTodo: ''
    },
    methods: {
        addTodo: function() {
            this.todos.push({
                id: this.newTodo.id,
                text: this.newTodo.text,
                completed: this.newTodo.completed
            })
            this.newTodo.id++
            this.newTodo.text = ""
        },
        removeTodo: function(todo){
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    },
    computed:{
        incompleteTodos: function(){
            let incompleteTodos = []
            for (let i=0; i<this.todos.length; i++){
                if (!this.todos[i].completed){
                    incompleteTodos.push(this.todo[i])
                }
            }
            return incompleteTodos
        },
        completeTodos: function(){
            let completeTodos = []
            for (let i=0; i<this.todos.length; i++){
                if (!this.todos[i].completed){
                    completeTodos.push(this.todo[i])
                }
            }
            return completeTodos
        }
    }
})
