<template>
  <div class="home">
    <div class="container mt-3">      
      <div class="row mt-3 singleReview"
            v-for="(review, index) in reviews"
            :key="review.pk">
        <div class="col-8">
          <p class="mb-0">Visité par:
            <span><b class="text-danger">{{ review.review_author }}</b>, le  <i>{{ review.created_at }}</i></span>
          </p>
          <h2><b>{{ review.restaurant_name }}</b></h2>          
          <p class="text-success" >{{ review.restaurant_adress }}</p> 
          <hr class="mb-0">    
        </div>
        <div class="col-4 text-center my-auto">
          <button v-show="reviewToShow !== index" type="button" class="btn btn -sm btn-outline-info" @click="reviewToShow= index">Consulter</button>
          <button v-show="reviewToShow == index" type="button" class="btn btn -sm btn-outline-danger" @click="reviewToShow= null">Refermer</button>  
          </div>       
        <hr>

         <div v-show="reviewToShow == index">
          <ReviewDetail
          :id="review.id"/>
        </div>
      </div>  
    </div>
  </div>  
</template>

<script>
import { apiService } from "@/common/api.service.js";
import ReviewDetail from "@/components/ReviewDetail.vue";
export default {
  name: "home",
  data () {
    return {
      reviews: [],
      reviewToShow: null,
    }
  },
  components: {
    ReviewDetail
  },
  methods: {
    getReviews() {
      let endpoint = "/api/restaurant_review/";
      apiService(endpoint)
        .then(data => {          
          this.reviews.push(...data)          
      })
    },  
  }, 
  mounted() {      
    this.getReviews()
    console.log(this.reviews) 
    },
};
</script>

<style >
.pac-container:after {  
  background-image: none !important;
    height: 0px;
}
body {
  background-image:url(../assets/Optimized-117.jpg);
}

.singleReview {
  background-color: white;
  border: 1px solid 
}
</style>