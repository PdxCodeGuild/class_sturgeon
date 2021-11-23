
const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        walletAddress: "0xA7C744f7255d74920984b469601a0379978945E7",
    },

    methods: {
        
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://api.coingecko.com/api/v3/coins/markets?',
                params: {
                    vs_currency : 'usd',
                    order : 'market_cap_desc',
                    per_page : '500',
                    page : '1',
                    sparkline: 'false',

                }
            }).then(response => this.results = response.data)
        }
        
    },


    created: function() {
        this.loadQuotes()
    }
})
