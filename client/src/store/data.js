import { defineStore } from "pinia";

export const dataStore = defineStore('dataStore', {
    state: () => ({
        role: "",
        username: "",
        id: "",
    }),
    actions: {
        updateRole(role){
            this.role = role
        },
        updateUsername(username){
            this.username = username
        },
        updateID(id){
            this.id = id
        }
    }

})