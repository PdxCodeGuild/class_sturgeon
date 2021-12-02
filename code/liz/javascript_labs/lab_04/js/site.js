// vue todos

new Vue({
    el: '#app',
    data: {
        todos: [
            { text: 'finish this lab', id: 0, complete: false },
            { text: 'have fun', id: 1, complete: true}
        ],
        newTodo: ''
    },
    methods: {
        createTodo: function() {
            this.todos.push({
                text: this.newTodo,
                complete: false,
                id: this.todos.length})
            this.newTodo = ''
        },
        completed: function(todo) {
            // if (todo.complete === false) {
            //     todo.complete = true
            // } else {
            //     todo.complete = false
            // }
            todo.complete = !todo.complete
        },
        remove: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    },
    computed: {
        incomplete: function() {
            return this.todos.filter(function(item) {
                return item.complete === false
                // can also return !item.complete
            })
        },
        complete: function() {
            return this.todos.filter(function(item) {
                return item.complete === true
                // can also return item.complete
            })
        }
    }
})