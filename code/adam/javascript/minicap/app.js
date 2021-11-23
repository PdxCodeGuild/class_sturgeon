let app = new Vue({
    el: '#app',

    data: {
        bruce: "bruce.jpg",
        camping: "camping.jpg",
        date: '',
        designation: '',
        inputDate: new Date().toISOString().slice(0,10),
        isHidden: true,
        lookUpSize: '',
        lookUpDate: '',
        lookUpDistance: '',
        lookUpSpeed: '',
        lunar: '',
        mph: '',
        mayan: "mayan.jpg",
        missDistance: '',
        morgan: "morgan.jpg",
        name: '',
        sizeMeters: '',
        sizeMiles: '',
        asteroid: '',
        asteroidName: '',
    },

    methods: {
        loadNASA: function () {
            axios({
                method: 'GET',
                url: `https://api.nasa.gov/neo/rest/v1/feed?start_date=${this.inputDate}`,
                params: {
                    api_key: `x9tOqUPDJm12DiV8OLgtWCHTmUplEo2jisd1IVK0`
                }
            }).then(response => {
                this.inputDate = document.getElementById('inputDate').value.toString()
                this.day = response.data.near_earth_objects[this.inputDate]
                this.mph = Math.round(this.day[0]['close_approach_data'][0]["relative_velocity"]["miles_per_hour"])
                this.lunar = Math.round(this.day[0]['close_approach_data'][0]['miss_distance']['lunar'])
                this.missDistance = Math.round(this.day[0]['close_approach_data'][0]['miss_distance']['miles'])
                this.date = this.day[0]['close_approach_data'][0]['close_approach_date']
                this.name = this.day[0]['name']
                this.sizeMeters = Math.round(this.day[0]['estimated_diameter']['meters']['estimated_diameter_max'])
                this.sizeMiles = Math.round(this.day[0]['estimated_diameter']['miles']['estimated_diameter_max'])
            })
        },
        loadAsteroid: function () {
            axios({
                method: 'GET',
                url: `https://api.nasa.gov/neo/rest/v1/neo/${this.asteroid}`,
                params: {
                    api_key: `x9tOqUPDJm12DiV8OLgtWCHTmUplEo2jisd1IVK0`
                }
            }).then(response => {
                this.asteroid = document.getElementById('asteroid').value.toString()
                this.designation = response.data['designation']
                this.lookUpSize = Math.round(response.data.estimated_diameter['meters']['estimated_diameter_max'])
                this.lookUpDate = response.data['close_approach_data'][0]['close_approach_date']
                this.lookUpDistance = Math.round(response.data['close_approach_data'][0]['miss_distance']['lunar'])
                this.lookUpSpeed = Math.round(response.data['close_approach_data'][0]["relative_velocity"]["miles_per_hour"])
            })
        }
    }
})