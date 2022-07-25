<script setup>
import { useSampleSkeletonStore } from "../stores/sampleSkeletonStore.js";
import { ref, inject } from "vue";
    let name = ref("skeleton");
    let description = ref("skeleton description");
    let sampleVariable = ref("");
    const $api = inject("$api");
    const sampleSkeletonStore = useSampleSkeletonStore();
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
button.button.fancy-button.is-fullwidth(type="button" @click="sampleSkeletonStore.changeStoreVariable()") Change store variable
p {{ sampleVariable }}
p {{ sampleSkeletonStore.sampleStoreVariable }}
</template>
