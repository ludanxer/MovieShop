<template>
  <div class="log">
    <div id="log-session">
      <div class="image">
        <img src="@/assets/log.jpg" alt="log" />
      </div>
      <component :is="logview" @change="change"></component>
    </div>
  </div>
</template>

<script>
import SignUp from '@/components/SignUp.vue'
import SignIn from '@/components/SignIn.vue'

export default {
  data(){
    return {
      logview: SignUp
    }
  },
  components: {
    SignUp,
    SignIn,
  },
  methods: {
    change: function(){
      console.log('fuck');
      if(this.logview == SignUp){
        this.logview = SignIn;
      }
      else{
        this.logview = SignUp;
      }
    }
  }
}
</script>

<style scoped>
#log-session{
  margin-top: 4%;
  margin-left: 15%;
  height: 600px;
  width: 1024px;
  background-color: rgb(218, 218, 218);
  box-shadow: 15px 15px 8px rgba(190, 190, 190, 0.1);
}
.image{
  float: left;
}
</style>


