let counter = 0
new Vue({
    el: "#app",
    data: {
        new_todo_text: '',
        message: "Todo List",
        items: [],
        
    },
    methods: {
        add: function () {            
            this.items.push({ 
                text: this.new_todo_text,
                complete: false,
                id: counter++
            })
            this.new_todo_text = ''            
        },
        done: function (item) {
            if (item.complete) {
                item.complete = false
            }
            else item.complete = true
        },
        del: function(item) {
            this.items.splice(this.items.indexOf(item), 1)
        }
    },
    computed: {
        comp_items: function () {
            return this.items.filter(function (item) {
                return item.complete
            })
        },
        inc_items: function () {
            return this.items.filter(function (item) {
                return !item.complete
            })
        }
    } 
})