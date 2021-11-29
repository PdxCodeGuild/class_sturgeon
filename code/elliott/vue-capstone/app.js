const vm = new Vue({
    el: '#weatherApp',
    data: {
        weatherReport: {},
        forecastReport: {},
        city: '',

    },

    methods: {

        getWeather: function() {
            axios({
                method: 'get',
                url: 'http://api.openweathermap.org/data/2.5/weather',
                params: {
                    q: this.city,
                    appid: "549e6339397ac70ebf57336256bf4625",
                    units: 'imperial',
                },
            }).then(response => {this.weatherReport = response.data
                this.getForecast()
            })
                
        },

        getForecast: function(){
            axios({
                method: 'get',
                url: 'https://api.openweathermap.org/data/2.5/onecall',
                params: {
                    lat: this.weatherReport.coord.lat,
                    lon: this.weatherReport.coord.lon,
                    exclude: ['current','minutely','hourly'
                ],                    
                appid: "549e6339397ac70ebf57336256bf4625",
                    units: 'imperial',
                },
            }).then(response => this.forecastReport = response.data)
        },

        dateBuilder: function() {
            let d = new Date();
            let months = ["January", "February", "March", "April", "May","June", "July",
        "August", "September", "October", " November", "December"];
            let days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            let day = days[d.getDay()];
            let date = d.getDate();
            let month = months[d.getMonth()]
            let year = d.getFullYear()

            return `${day} ${date} ${month} ${year}`
        }

        
    },
})



