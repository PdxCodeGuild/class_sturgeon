

const vm = new Vue({
    el: '#app',
    data: {
        results: {},
        filter: '',
        type: ''
    },
    methods: {
        

        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: this.filter, //name of author
                    type: this.type //'author' 'tag' 'keyword'
                    
                },
                headers: {
                    "Authorization": `Token token="ee10ca6bf7fcb39a101cf7aa66ef776d"`
                }
            }).then(response => this.results = response.data)
        },

        
    },

    created: function() {
        this.loadQuotes()
    }
})







