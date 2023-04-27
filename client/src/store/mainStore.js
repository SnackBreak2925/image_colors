import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    count: 777
  },
  mutations: {
    increment(state) {
      state.count++
    }
  },
  methods: {
    increment() {
      this.$store.commit('increment')
      console.log(this.$store.state.count)
    }
  },
  getters: {
    counts(state) {
      return state.count
    }
  }
})
