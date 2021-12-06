
const vm = new Vue({
    el: '#app',
    data: {
        results: [],
        coinSelected: '',
        coinQuantity: '',
        porfolio: [],
        total: 0,
    },

    methods: {
        
        loadCoins: function() {
            let i = 0
            while (i < 4) {
            i++ 
                axios({
                method: 'get',
                url: 'https://api.coingecko.com/api/v3/coins/markets?',
                params: {
                    vs_currency : 'usd',
                    order : 'market_cap_desc',
                    per_page : '250',
                    page : i,
                    sparkline: 'false',
                }
            }).then(response => this.results = this.results.concat(response.data))
     
        }},
        
        loadPorfolio: function() {
            for (each of this.results){
                if( each.name === this.coinSelected) {
                    let usd = each.current_price * this.coinQuantity
                    this.total = this.total + usd
                    this.porfolio.push( {
                        
                        id: this.porfolio.length + 1,
                        name: each.name,
                        symbol: each.symbol.toUpperCase(),
                        price: each.current_price,
                        image: each.image,
                        quantity: this.coinQuantity,
                        uservalue: usd,

                        });
                }}
                this.coinSelected = '';
                this.coinQuantity = '';
        },
        removeCoin: function (each) {
            this.total = this.total - each.uservalue
            this.porfolio.splice( this.porfolio.indexOf(each), 1);
          },
    },
    created: function() {
        this.loadCoins()
    }
})
