Vue.component('todo-item',{
    data: function(){
        return
    },
    // template, recommends using the backticks for some reason that I wasn't really listening.
    template: `
    `
})

new Vue({
    el: '#app',
    data: {
        todo:[
            {id:1, text: "wash the dog", complete: false},
            {id:2, text: "pet the dog", complete: false},
            {id:3, text: "cook the dog", complete: true},
        ],
        newTodo: {id: 4, text: "", complete: false}
    },
    methods: {
        addTodo: function(){
            this.todos.push({
                id: this.NewTodo.id,
                text: this.newTodo.text, 
                complete: this.NewTodo.complete
            })
            this.newTodo.id++
            this.newTodo.text = ""
        }

    },
    computed:{
        imcompleteTodos: function(){
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
});

