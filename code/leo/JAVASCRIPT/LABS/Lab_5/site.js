const vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        results: {},
        theSearch: "",
        pageNumber: 1,
        selected: 'author',
        options: [
          { text: 'by Author', value: 'author' },
          { text: 'by Keyword', value: 'keyword' },
          { text: 'by Tag', value: 'tag' }
        ],
    },


    methods: {
        
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => {
                this.qotd = response.data
            }).catch(console.log("error!"))
        },
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: this.theSearch,
                    type: this.selected,
                    page: this.pageNumber,
                },
                headers: {
                    "Authorization": `Token token="bfda36be660ededb2a0245d5ea7ad7c4"`
                }
            }).then(response => this.results = response.data)
        }
        
    },
    created: function() {
        this.loadQotd()
    }
})
