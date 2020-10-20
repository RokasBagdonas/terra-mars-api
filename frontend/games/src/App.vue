<template>
<NavBar> </NavBar>
<router-view/>
</template>


<script lang="ts">
import Vue from 'vue';
import NavBar from "./components/NavBar.vue";
export default ({
components: {
    NavBar,
}
})
</script>
