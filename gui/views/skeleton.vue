<script setup>
import { ref, inject } from "vue";
    let name = ref("skeleton");
    let description = ref("skeleton description");
    let sampleVariable = ref("");
    const $api = inject("$api");
    function testApi(){
        // Sample API request
        $api.get("/api/v2/health").then((response) => {
            console.log('Woohoo, this page can talk to the API!');
        }).catch((error) => {
            console.error(error);
        });
    }
    function sampleFunction(){
        sampleVariable.value = "You clicked the button!";
    }
</script>

<template lang="pug">
h2 {{ name }}
p {{ description }}
button.button.fancy-button.is-fullwidth(type="button" @click="testApi()") Test API 
button.button.fancy-button.is-fullwidth(type="button" @click="sampleFunction()") Click Me
p {{ sampleVariable }}
</template>
