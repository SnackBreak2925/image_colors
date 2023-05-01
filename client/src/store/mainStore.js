import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    file: null,
    isLoading: false,
    countColor: null,
    colors: [],
  },
  mutations: {
    storeFile(state, file) {
      state.file = file
    },
    deleteFiles(state) {
      state.file = null
    },
    sendFile(state) {
      state.isLoading = true
      let body = {
        countColor: state.countColor
      }

      let reader = new FileReader()
      reader.readAsDataURL(state.file)
      reader.onload = () => {
        body['file'] = reader.result.replace(/data:.*,/, '')
        console.log(body)
        Vue.http.post('http://localhost:5000/proccess_image', body).then((data) => {
          state.colors = data.body
          state.isLoading = false
        })
      }
    },
    setCountColors(state, countColor) {
      state.countColor = countColor
    },
  },
  actions: {
    storeFile({ commit, state }, file) {
      commit('storeFile', file)
    },
    deleteFiles({ commit, state }) {
      commit('deleteFiles')
    },
    sendFile({ commit, state }) {
      commit('sendFile')
    },
    setCountColors({ commit, state }, countColor) {
      commit('setCountColors', countColor)
    },
  },
  getters: {
    isLoading(state) {
      return state.isLoading
    },
    getColors(state) {
      return state.colors
    },
    getFile(state) {
      return state.file
    }
  }
})
