new Vue({
    el: '#app',
    data: {
        todos: [
            { text: 'don\'t freak out', id: 0, complete: false },
        ],
        message: "hey"
    },
    methods: {
        createTodo: function() {
            let addedTodo = this.newTodo
            let id = this.todos.length
            this.todos.push({text: addedTodo, complete: false, id: id})
        }
    }
})