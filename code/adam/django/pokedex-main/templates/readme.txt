cut from the home.html as a way to edit pokedex

<div>
    <input type="text" placeholder="New Pokemon Name" v-model="newPokemon.name"><br>
    <template v-if="postErrors.name">
        <p v-for="error in postErrors.name">[[ error ]]</p>
    </template>
    <textarea placeholder="Pokemon Number" v-model="newPokemon.number"></textarea><br>
    <template v-if="postErrors.number">
        <p v-for="error in postErrors.number">[[ error ]]</p>
    </template>
    <button @click="createPokemon">New Pokemon</button>
</div>


createPokemon: function() {
    // let csrf_token = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    axios({
        method: 'post',
        url: '/apis/v1/pokemon',
        headers: {
            'X-CSRFToken': this.csrf_token
        },
        data: {
            "name": this.newPokemon.name,
            "author": this.currentUser.id,
            "number": this.newPost.body
        }
    }).then(response => {
        this.loadPokemon()
        this.newPokemon = {
            "name": "",
            "author": null,
            "number": ""
        }
    }).catch(error => {
        if (error.response.status === 400) {
            this.postErrors = error.response.data
        }
    })
},