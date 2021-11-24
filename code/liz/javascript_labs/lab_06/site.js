const vm = new Vue({
    el: '#app',
    data: {
        game: {},
        gameDate: '',
        finalJeopardy: '',
        categories: [],
    },
    methods: {
        getJeopardy: function() {
            let x = this.gameDate.split('-')
            x = `${x[1]}/${x[2]}/${x[0]}`
            console.log(x)
            axios({
                method: 'get',
                url: `https://jarchive-json.glitch.me/game/${x}`,
            }).then(response => {
                console.log(response)
                this.game = response.data
                this.finalJeopardy = this.game['final jeopardy']
                this.categoryMaker()
            })
        },
        categoryMaker: function() {
            let categories = []
            for (item of this.game.jeopardy) {
                if (!categories.includes(item.category)) {
                    categories.push(item.category)
                } 
            }
            this.categories = categories
            console.log(categories)

        }
    },
    created: function() {
        // this.getJeopardy()
    }
   
})