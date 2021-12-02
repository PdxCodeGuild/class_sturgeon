Vue.component('list-item', {
    props: ['quote'],
    template: `
    <li>
        {{ quote.body }} <br>&emsp;- {{ quote.author }}
    </li>
    `
})


new Vue({
    el: '#app',
    data: {
        quotes: {},
        selectedType: '',
        userInput: '',
        results: {},
        page: 1,
        lastUserInput: '',
        lastSelectedType: '',
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
                    filter: this.userInput,
                    type: this.selectedType,
                    page: this.page
                },
                headers: {
                    Authorization: `Token token="${apiKey}"`
                }
            }).then(response => {
                this.results = response.data
            })
            this.lastUserInput = this.userInput
            this.lastSelectedType = this.selectedType
            this.userInput = ''
            this.selectedType = ''
        },
        nextPage: function() {
            this.page++
            console.log(this.page)
            this.userInput = this.lastUserInput
            this.selectedType = this.lastSelectedType
            this.requestedQuotes()
        },
        backPage: function() {
            this.page--
            console.log(this.page)
            this.userInput = this.lastUserInput
            this.selectedType = this.lastSelectedType
            this.requestedQuotes()
        }
    },
    created: function() {
        this.getQuotes()
    }
})