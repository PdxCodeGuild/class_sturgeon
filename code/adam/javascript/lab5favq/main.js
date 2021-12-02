Vue.component('qotd-item', {
    props: ['qotd'],
	template: 
            `<div>
                <button @click="$emit('load-qotd', qotd)" class="button1">
                    Quote of the Day:
                </button>
                <template v-if="Object.keys(qotd).length">
                    <p>{{ qotd.quote.body }}</p>
                    <p><a :href="qotd.quote.url">{{ qotd.quote.author }}</a></p>
                </template>
            </div>`, 
    data: function () {
        return {
            qotd:{}}
        },
    })

let vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        results: [],
        filter: "",
        selection: "",
        page: 1,
        tag: "tag.png",
        author: "author.jpg",
        keyword: "keyword.jpg",
        isHidden: true,
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => { this.qotd = response.data
            }).catch(console.log("error! - in case the internet goes down or something"))
        },
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: this.filter,
                    type: this.selection,
                    page: this.page,
                },
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                }
            }).then(response => this.results = response.data)
        },
    nextPage: function() {
        this.page++,
        console.log(this.page)
        this.loadQuotes()
    },
    previousPage: function() {
        if (this.page >=2) {
            this.page--
        }
        this.loadQuotes()
    }},
    created: function() {
        this.loadQotd()
    }
})