const vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        results: {},
        filter: "",
        type: "",
    },
    methods: {

        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    type: 'author'
                },
                headers: {
                    "Authorization": `Token token="ee10ca6bf7fcb39a101cf7aa66ef776d"`
                }
            }).then(response => this.results = response.data)
        },
    
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: this.filter, //name of author
                    type: 'author'//'author' 'tag' 'keyword'
                },
                headers: {
                    "Authorization": `Token token="ee10ca6bf7fcb39a101cf7aa66ef776d"`
                }
            }).then(response => {
                this.qotd = response.data
            }).catch(console.log("error!"))
        },
    },
    created: function() {
        this.loadQuotes()
        
    }
})







