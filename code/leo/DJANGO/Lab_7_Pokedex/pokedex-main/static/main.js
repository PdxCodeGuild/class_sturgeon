const vm = new Vue({
    el: "#app",
    delimiters: ['[[', ']]'],
    data: {
      pokemonList:[],
    },

    methods: {


      loadPokemon: function() {
        axios({
          method: "get",
          url: "/apis/v1/"
        }).then(response => (this.pokemonList = response.data))
      },

      capturePokemon: function(pokemon, user) {
        if (pokemon.caught_by.includes(user)) {
          return alert('You already have this pokemon')
        } 
        else {
        pokemon.caught_by.push(user)
          axios({
            method: "patch",
            url: "/apis/v1/"+ pokemon.id + '/',
            headers: {
              'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
            },
            data: {
              "caught_by": pokemon.caught_by
            }
          }).then(response => (this.loadPokemon()))
            }
      },

      resealePokemon: function(pokemon, user) {
        
        pokemon.caught_by.splice(pokemon.caught_by.indexOf(user), 1)
        
        axios({
            method: "patch",
            url: "/apis/v1/"+ pokemon.id + '/',
            headers: {
              'X-CSRFToken': document.querySelector('input[name=csrfmiddlewaretoken]').value
            },
            data: {
              "caught_by": pokemon.caught_by
            }
          }).then(response => (this.loadPokemon()))    
      }

  },


    created: function(){
      this.loadPokemon()
    }


  })