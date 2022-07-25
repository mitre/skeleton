import { defineStore } from "pinia";

export const useSampleSkeletonStore = defineStore({
  id: "skeleton",
  state: () => ({
    sampleStoreVariable: "Original Store Variable"
  }),
  actions: {
    changeStoreVariable(){
        this.sampleStoreVariable = "Store variable changed!";
    },
  },
});
