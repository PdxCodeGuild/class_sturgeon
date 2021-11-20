const vm = new Vue({
    el: '#app',
    data: {
        quotes: {},
        selectedType: '',
        userInput: '',
    },
    methods: {
        getQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                headers: {
                    Authorization: `Token token="${apiKey}"`
                }
            }).then(response => {
                this.quotes = response.data
            })
        },
        requestedQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: 'this.userInput',
                    type: 'selectedType}'
                },
                headers: {
                    Authorization: `Token token="${apiKey}"`
                }
            })
        }
    },
    created: function() {
        this.getQuotes()
    }
})