
const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        coinSelected: '',
        coinQuantity: '',
        porfolio: [],
    },

    methods: {
        
        loadCoins: function() {
            axios({
                method: 'get',
                url: 'https://api.coingecko.com/api/v3/coins/markets?',
                params: {
                    vs_currency : 'usd',
                    order : 'market_cap_desc',
                    per_page : '5',
                    page : '1',
                    sparkline: 'false',

                }
            }).then(response => this.results = response.data)
        },
        
        loadPorfolio: function() {
            for (each of this.results){
                if( each.name === this.coinSelected) {
                    let usd = each.current_price * this.coinQuantity
                    this.porfolio.push( {
                        
                        id: this.porfolio.length + 1,
                        name: each.name,
                        symbol: each.symbol,
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
            console.log('here')
            console.log(each)
            this.porfolio.splice( this.porfolio.indexOf(each), 1);
          },
    },
    created: function() {
        this.loadCoins()
    }
})
