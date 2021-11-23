const vm = new Vue({
    el: '#app',
    data: {
        weather: {},
        city: ''
    },
    methods: {
        

        getWeather: function() {
            axios({
                method: 'get',
                url: '',
                params: {
                    q: this.city,
                    appid: "549e6339397ac70ebf57336256bf4625"
                },
                
                
            }).then(response => this.results = response.data)
        },

        
    },
})



