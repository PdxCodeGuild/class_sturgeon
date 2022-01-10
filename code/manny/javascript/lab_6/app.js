const vm= new Vue({
    el: '#app',
    data : {
        info: {},
        author : "",
        poemCount : "1",
    },
    methods:{
      getPoem : function (){
        axios({
          method: "get",
          url : `https://poetrydb.org/author,poemcount/${this.author};${this.poemCount}.json`
        }).then(response => {
          this.info = response.data
        })
      },
      readPoem : function(poem){
        this.info = [poem]
      },
      getRandom : function (){
        axios({
          method: "get",
          url : `https://poetrydb.org/random`
        }).then(response => {
          this.info = response.data
        })
      },
    },
    mounted : function() {
      this.getRandom()
    },
  })

//event listeners
