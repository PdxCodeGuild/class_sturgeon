
Vue.component('quote-item',{
    data: function() {
        return {
        }
    },
    props: ['quote'],
    template: `
    <div>
        <h3>{{ quote.body }}</h3>
        <p>{{ quote.author }}</p>
        <p v-if="quote.tags.length"><u>Tags:</u> 
        <li v-for="tag in quote.tags">{{ tag }}</li>
        </p>
        <hr>
        <br>
    </div>
    `,

})

new Vue ({
    el: "#app",
    data: {
        message: "Quote time",
        search_text: '',
        type: 'author',
        page: 1,
        qod: {},
    },
    methods: {
        quote: function (){
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                headers: {
                    "Authorization": 'Token token="a5cc4f9c190f7f0149e309a86572efbb"'
                },
                
            }).then((response) => {
                this.qod = (response.data)
            })
            },
        search: function (){
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                headers: {
                    "Authorization": 'Token token="a5cc4f9c190f7f0149e309a86572efbb"'
                },
                params: {
                    "filter": this.search_text,
                    "type": this.type,
                    "page": this.page
                }
            }).then((response) => {
                this.qod = (response.data)
                
            })
                this.search_text = '' 
                this.type = 'author'
            },
        
        
    },
    created: function (){
        this.quote()
    }
})