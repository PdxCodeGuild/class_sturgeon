let app = new Vue({
    el: '#app',

    data: {
        active: false,
        apophis: "apophis.jpg",
        asteroid: '',
        asteroidName: '',
        bruce: "bruce.jpg",
        bruceActive: false,
        bruceAsteroid: "bruceAsteroid.jpg",
        camping: "camping.jpg",
        campingActive: false,
        campingAsteroid: "campingAsteroid.jpg",
        deep: "deep.jpg",
        date: '',
        designation: '',
        eighty: false,
        ended: false,
        explanation: '',
        fifty: false,
        forty: false,
        health: 100,
        hundred: false,
        inputDate: new Date().toISOString().slice(0,10),
        isHidden: true,
        lookUpSize: '',
        lookUpDate: '',
        lookUpDistance: '',
        lookUpSpeed: '',
        lunar: '',
        mph: '',
        mayan: "mayan.jpg",
        mayanAsteroid: "mayanAsteroid.jpg",
        mayanActive: false,
        missDistance: '',
        missileaudio: "Missile.mp3",
        morgan: "morgan.jpg",
        morganActive: false,
        name: '',
        ninety: false,
        potd: '',
        selection: '',
        seventy: false,
        showImage: false,
        sixty: false,
        sizeMeters: '',
        sizeMiles: '',
        ten: false,
        thirty: false,
        title: '',
        twenty: false,
        tyson: 'tyson.jpg',
        tysonActive: false,
        money: 0,
        resources: {
            Crowdsourcing: {
                icon: "🧑‍🤝‍🧑",
                cost: 5,
                rate: 3,
                count: 0
            },
            TaxHike: {
                icon: "💸",
                cost: 10,
                rate: 15,
                count: 0
            },
            Mob: {
                icon: "🔥",
                cost: 100,
                rate: 30,
                count: 0
            },
            missile: {
                icon: "🚀",
                cost: 1000,
                rate: 400.9,
                count: 0
            }
        }
    },

    methods: {
        loadNASA: function () {
            axios({
                method: 'GET',
                url: `https://api.nasa.gov/neo/rest/v1/feed?start_date=${this.inputDate}`,
                params: {
                    api_key: `${apiKey}`
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
                    api_key: `${apiKey}`
                }
            }).then(response => {
                this.asteroid = document.getElementById('asteroid').value.toString()
                this.designation = response.data['designation']
                this.lookUpSize = Math.round(response.data.estimated_diameter['meters']['estimated_diameter_max'])
                this.lookUpDate = response.data['close_approach_data'][0]['close_approach_date']
                this.lookUpDistance = Math.round(response.data['close_approach_data'][0]['miss_distance']['lunar'])
                this.lookUpSpeed = Math.round(response.data['close_approach_data'][0]["relative_velocity"]["miles_per_hour"])
            })
        },
        checkDate: function() {
            if (this.selection === "bruce") {
                this.inputDate = "1998-06-10"
            }
            else if (this.selection === "morgan") {
                this.inputDate = "1998-05-08"
            }
            else if (this.selection === "mayan") {
                this.inputDate = "2012-12-21"
            }
            else if (this.selection === "camping") {
                this.inputDate = "2021-05-21"
            }
            else if (this.selection === "apophis") {
                this.inputDate = "2029-04-13"
            }
        },
        loadPotd: function() {
            axios({
                method: 'GET',
                url: `https://api.nasa.gov/planetary/apod?`,
                params: {
                    api_key: `${apiKey}`
                }
            }).then(response => {
                this.potd = response.data["url"]
                console.log(this.potd)
                this.explanation = response.data["explanation"]
                this.title = response.data["title"]
            })
        },
        toggleImage: function() {
            this.showImage = !this.showImage
        },
        fire: function() {
            this.health -= 10
            this.resources.missile.count -= 1
            if ( this.health == 100 ) {
                this.hundred = true
            }
            if ( this.health == 90 ) {
                this.ninety = true
            }
            if ( this.health == 80 ) {
                this.eighty = true
            }
            if ( this.health == 70 ) {
                this.seventy = true
            }
            if ( this.health == 60 ) {
                this.sixty = true
            }
            if ( this.health == 50 ) {
                this.fifty = true
            }
            if ( this.health == 40 ) {
                this.forty = true
            }
            if ( this.health == 30 ) {
                this.thirty = true
            }
            if ( this.health == 20 ) {
                this.twenty = true
            }
            if ( this.health == 10 ) {
                this.ten = true
            }
            if ( this.health <= 0 ) {
                this.ended = true
            }
        },
        restart: function() {
            this.health = 100
            this.ended = false
        },
        buy: function(id) {
            this.resources[id].count++
            this.money -= this.resources[id].cost
            let inflation = 1.1
            this.resources[id].cost = Math.floor(this.resources[id].cost * inflation)
        },
        playSound (sound) {
            if(sound) {
                var audio = new Audio(sound);
                audio.play();
            }
        }
    },

    mounted: function() {
        let loopCount = 0
        setInterval(() => {
            loopCount++
            let keys = Object.keys(this.resources)
            for (index in keys) {
                let key = keys[index]
                this.money += this.resources[key].rate * this.resources[key].count
            }
        }, 100)
    },

    computed: {
        displayMissiles: function() {
            let m = ""
            for (var i = 0; i < this.resources.missile.count; i++) {
                m += "🚀"
            }
            return m
        }
    }
})

var tl = gsap.timeline({defaults:{opacity: 0}})
    .to('.warning', {opacity: 15, duration: 4, y: -2500})
    .to('.warning', {opacity: 0, duration: 1 })
    .from('main', {duration: 1, delay: 1.1, backgroundPosition: '200px 0px', opacity: 0}, "-=1.5")

setTimeout(() => { document.getElementById("remove").remove(); }, 9000)