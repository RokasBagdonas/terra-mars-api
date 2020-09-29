<template>
<table class="table">
<thead>
    <tr>
    <th>Id</th>
    <th>Date</th>
    <th>Game Map</th>
    <th>Num Of Gen</th>
    <th>Draft</th>
    <th>Prelude</th>
    <th>Venus Next</th>
    <th>Colonies</th>
    </tr>
</thead>

<tbody>
<tr v-for="game in games" v-bind:key="game">
<td v-for="(value, key) in game" v-bind:key="key">{{ value }}</td>
</tr>
</tbody>
</table>


</template>

<script>
import {getAllGames} from '../mars-api-endpoints';
import {axios} from 'axios';

export default {
data() {
    return {
    games: [],
    }
},
created: function(){
    console.log("created hook");
},
mounted: function(){
    getAllGames()
    .then(response => {this.games = response.data.results; console.log(response.status); console.log(response)})
    .then(() => console.log(this.games))
    .catch(error => console.log(error));
}
}
</script>
