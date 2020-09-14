<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">TrustyMonkey</router-link>

      <div class="collapse navbar-collapse flex-row justify-content-end">

        <vue-google-autocomplete
          ref="inputField"
          id="map"
          class="form-control mr-sm-2"
          placeholder="Rechercher un restaurant"
          v-on:placechanged="getAddressData"
          country="fr"
          types="establishment"          
        ></vue-google-autocomplete>

        <!-- <ul class="navbar-nav mr-2">
          <li class="nav-item active"> -->
           <form @submit.prevent="login">
            <div class="form-group">              
              <input class="form-control" id="username" placeholder="Nom" v-model="username">             
            </div>
            <div class="form-group">              
              <input type="password" class="form-control" id="password" placeholder="Mot de passe" v-model="password">
            </div>          
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
            <!-- <a v-if="requestUser" class="btn btn-danger" href="/accounts/logout/">Se deconnecter</a>
            <a v-else class="btn btn-primary" href="/accounts/login/">Se connecter</a> -->
          <!-- </li>
        </ul> -->
      </div>
    </div>
  </nav>
</template>


<script>
import VueGoogleAutocomplete from "vue-google-autocomplete";
import { store } from "../common/store.js";
import axios from "axios"

export default {
  name: "NavbarComponent",
  components: { VueGoogleAutocomplete },
  data() {
    return {
      requestUser: null,
      addressData: "",
      password: null,
      username: null,
      token: null,     
    };
  },
  created() {
    this.setRequestUser();
    console.log(this.requestUser)    
  },  
  methods: {
    login () {
      axios.post("http://127.0.0.1:8000/api/token/", {
        username: this.username,
        password: this.password
      })
      .then(resp => {
        this.token = resp.data.access;
        console.log(resp)        
        localStorage.setItem("user-token", this.token)
      }) 
      .catch(err => {
        console.log(err),
        localStorage.removeItem("user-token")
      })
    },
    setRequestUser() {      
      this.requestUser = window.localStorage.getItem("username");      
    },
    getAddressData(addressData, placeResultData) {
      this.placeResultData = placeResultData;
      this.addressData = addressData;      
      this.lat = this.placeResultData.geometry.location.lat(),
      this.lng = this.placeResultData.geometry.location.lng(),      
      store.setRestLat(this.lat)      
      store.setRestLng(this.lng)      
      this.$router.push({ name: "rest_reviews", 
                params: { maps: this.placeResultData.place_id,
                          name: this.placeResultData.name,
                          adress: this.placeResultData.formatted_address,
                          opening_hours: this.placeResultData.opening_hours.weekday_text,
                          phone: this.placeResultData.formatted_phone_number,
                          website: this.placeResultData.website,
                          type: this.placeResultData.types,}})      
      this.$refs.inputField.$refs.autocomplete.value='';      
    },      
  }
};
</script>

<style scoped>
.my-navbar {
  border-bottom: 1px solid grey;
}
.navbar-brand {
  font-weight: bold;
  font-size: 200%;
}
.navbar-brand:hover {
  color: grey !important;
}
#map {
  width: 45%;
}
.form-control {
  border-left: none;
  border-right: none;
  border-top: none;
  border-bottom: 1px solid lightblue;
}
</style>