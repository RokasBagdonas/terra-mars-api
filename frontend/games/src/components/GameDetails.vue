<template>
<h1 class="title">Game Details</h1>
<p>Select a game from the list..</p>
<table class="table">
    <thead>
    <tr>
        <th v-for="(item, name) in this.gameScores.scores[0]">{{name}}</th>
    </tr>
    </thead>
    <tbody>
        <tr v-for="playerScore in this.gameScores.scores" v-bind:key="playerScore">
            <td>{{playerScore}}</td>
        </tr>
    </tbody>
</table>


</template>


<script>
import Vue from 'vue'
export default {
    props: ['gameScores'],

}

</script>
