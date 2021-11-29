// this is jeopardy - mini capstone


Vue.component('clue-object', {
    data: function () {
        return {
            clicks: 0
        }
    },
    props: ['item', 'category'],
    template: `
    
    <div class="clue-container" v-if="category === item.category" @click="clicks += 1">
    
        <p class="value" v-if="clicks === 0" >{{ item.value }}</p>

        <p class="clue" v-else-if="clicks === 1">{{ item.clue }}</p>

        <p class="answer" v-else-if="clicks === 2">{{ item.answer }}</p>

        <p class="blank" v-else></p>
    </div>
    `
})


const vm = new Vue({
    el: '#app',
    data: {
        game: {},
        gameDate: '',
        finalJeopardy: '',
        jeopardyCategories: [],
        doubleJeopardyCategories: [],
        round: 0,
        count: 0,
        
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
                this.game = response.data
                this.finalJeopardy = this.game['final jeopardy']
                this.categoryMaker()
                this.round = 1
                this.count = 0
                this.clicks = 0
            })
        },
        categoryMaker: function() {
            let jeopardyCategories = []
            let doubleJeopardyCategories = []
            for (item of this.game.jeopardy) {
                if (!jeopardyCategories.includes(item.category)) {
                    jeopardyCategories.push(item.category)
                } 
            }
            this.jeopardyCategories = jeopardyCategories

            for (item of this.game['double jeopardy']) {
                if (!doubleJeopardyCategories.includes(item.category)) {
                    doubleJeopardyCategories.push(item.category)
                } 
            }
            this.doubleJeopardyCategories = doubleJeopardyCategories
            

        },
    },
    created: function() {
        // this.getJeopardy()
        // this.remove()
    }
   
})