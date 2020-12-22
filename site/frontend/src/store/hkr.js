import Vue from 'vue'

export default {
    namespaced: true,
    state: {
        itemFoundState: { type: Object },
    },
    mutations: {
        setItemFoundState(state, payload) {
            Vue.set(state.itemFoundState, payload.name, payload.value)
        },
    }
}