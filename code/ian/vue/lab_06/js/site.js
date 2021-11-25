

Vue.component('exercise-item', {
    data: function() {
        return{

        }
    },
    props: ['results'],
    methods: {
        comp_group: function (comp_id, comp_name) {
            console.log(comp_id)
            console.log(comp_name)
            this.$root.group_search = comp_id
            this.$root.group_label = comp_name
            this.$root.group()
        },
        comp_info: function(comp_uuid) {
            console.log(comp_uuid)
            this.$root.uuid = comp_uuid
            this.$root.ex_detail()
        },
        comp_pic: function(comp_uuid) {
            this.$root.uuid = comp_uuid
            this.$root.ex_pic()
        },
        comp_add: function(comp_name) {
            this.$root.workouts.push({
                text: comp_name,
                reps: 0,
                weight: 0,
                sets: []
                
            })
        },
        comp_img: function(comp_id, comp_name) {
            return `https://wger.de/media/exercise-images/${comp_id}/${comp_name.replace(' ','-')}-1.png`
            
        }
    },
    template:`
    <div>
        <div class="group" v-for="result in results.results">
            <div v-if="!result.creation_date">
                <h1><a @click="comp_group(result.id, result.name)"><i class="fas fa-angle-right"></i>  {{result.name}}</a></h1>
            </div>
            <div id="exercise" v-if="result.creation_date">
                <h2>
                <a @click="comp_add(result.name)"><i class="fa fa-plus"></i></a>
                {{result.name}}</h2>
            
            </div>

        </div>
    </div>
    `,
})

{/* <img :src="comp_img(result.id, result.name)"> */}

new Vue ({
    el: "#app",
    data: {
        message: "Workout Log",
        workouts: [],
        complete_workouts: [],
        results: {},
        weight: 0,
        reps: 0, 
        group_search: '',
        group_label: '',
        uuid: '',
        pic: '',
        limit: 20,
        offset: 0,
        
    },
    methods: {
        list: function(){
            this.group_search = ''
            this.group_label = ''
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
                console.log(response.data)
                this.results = (response.data)
               
            })
            this.home()
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
                    "category": this.group_search
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
                    "category": this.group_search,
                }
            }).then((response) => {
                this.results = (response.data)
            })
        },
        categories: function(){
            this.group_label = ''
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
            this.home()
        },
        group: function(){
            this.offset = 0
            
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
                    "category": this.group_search,
                }
            }).then((response) => {
                this.results = (response.data)
                
               
            })
        },
        del: function(item){
            this.workouts.splice(this.workouts.indexOf(item), 1)
        },
        complete: function(){
            this.complete_workouts.push({
                date : Date().replace('GMT-0800 (Pacific Standard Time)', ''),
                session : this.workouts
            })
            this.workouts = []
            
        },
        set: function (item) {
            
            i = this.workouts.indexOf(item)
            this.weight = this.workouts[i].weight
            this.reps = this.workouts[i].reps
            
            this.workouts[i].sets.push({
                set: this.workouts[i].sets.length+1,
                reps: this.reps,
                weight: this.weight
            })
            this.workouts[i].reps = 0
            this.workouts[i].weight = 0
            
            
        },
        history: function() {
            let history=document.getElementById("history")
            let home=document.getElementById("home")
            
            home.style.display="none"
            history.style.display ="block"
            
        },
        home: function() {
            let history=document.getElementById("history")
            let home=document.getElementById("home")
            
            home.style.display="block"
            history.style.display="none"
        },
        
        
    },
    created: function (){
        this.list()
    }
})