import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Rest_Reviews from "../views/Rest_Reviews.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/rest_reviews/:maps",
    name: "rest_reviews",
    component: Rest_Reviews,
    props: true
  },  
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
