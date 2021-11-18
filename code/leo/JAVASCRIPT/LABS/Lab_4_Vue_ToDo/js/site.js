var app = new Vue({
    
        el: '#app',
        
        data: {
          newTodo: '',
          todoList: [],
        },
        
        computed: {
          memoryToDos() {
            return this.todoList;
          },
        },
        
        methods: {
          
          addItem: function () {
            this.todoList.push( {
              
              id: this.todoList.length + 1,
              name: this.newTodo,
              completed: false,
            });
            
            this.newTodo = '';
          },

          removeTodo: function ( each ) {
            this.todoList.splice( this.todoList.indexOf(each), 1);
          },

          completedTodo: function ( each ) {
            each.completed = true;
          },
        },
      } );