Vue.component('exercise-item', {
    data: function() {
        return{

        }
    },
    props: ['results'],
    template:`
    <div>
        <div class="exercise" v-for="result in results.results">
            <h3>{{result.name}}</h3>
            <p>ID: {{result.id}}</p>
            

        </div>
    </div>
    `,
})

new Vue ({
    el: "#app",
    data: {
        message: "Lab 6 time",
        results: {},
        search_text: '',
        limit: 20,
        offset: 20,
        
    },
    methods: {
        list: function(){
            axios({
                method: "get",
                url: "https://wger.de/api/v2/exercise",
                headers: {
                    "Content-Type": "application/json"
                    // "Authorization": "Token a9767f683694789792329e82e456c7e1442e6da3"
                },
                params: {
                    "limit": 20,
                    "offset": 0,
                    "language": 2,
                    
                }
            }).then((response) => {
                this.results = (response.data)
               
            })
        },
        next_page: function(){
            this.offset += 20
            axios({
                method: "get",
                url: "https://wger.de/api/v2/exercise",
                headers: {
                    "Content-Type": "application/json"
                },
                params: {
                    "limit": this.limit,
                    "offset": this.offset,
                    "language": 2,
                }  
            }).then((response) => {
                this.results = (response.data)
            })
        },
        prev_page: function(){
            this.offset -= 20
            axios({ 
                method: "get",
                url: "https://wger.de/api/v2/exercise",
                headers: {
                    "Content-Type": "application/json"
                },
                params: {
                    "limit": this.limit,
                    "offset": this.offset,
                    "language": 2,
                }
            }).then((response) => {
                this.results = (response.data)
            })
        },
        categories: function(){
            axios({
                method: "get",
                url: "https://wger.de/api/v2/exercisecategory",
                headers: {
                    "Content-Type": "application/json"
                },
                params: {
                    "language": 2
                }
            }).then((response) => {
                this.results = (response.data)
            })
        },
        group: function(){
            axios({
                method: "get",
                url: "https://wger.de/api/v2/exercise",
                headers: {
                    "Content-Type": "application/json"
                    // "Authorization": "Token a9767f683694789792329e82e456c7e1442e6da3"
                },
                params: {
                    "limit": 20,
                    "offset": 0,
                    "language": 2,
                    "category": 13,
                }
            }).then((response) => {
                this.results = (response.data)
               
            })
        },
    }
})