<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <a class="button is-primary"> Bulma button? </a>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>
