import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    count: 777,
    file: null
  },
  mutations: {
    storeFile(state, file) {
      state.file = file
    },
    deleteFiles(state) {
      state.file = null
    },
  },
  actions: {
    storeFile({ commit, state }, file) {
      state.file = file
      commit('storeFile', file)
    },
    deleteFiles({ commit, state }) {
      commit('deleteFiles')
    },
  },
  getters: {
    counts(state) {
      return state.count
    }
  }
})
