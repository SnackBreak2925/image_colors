// import { mount, createLocalVue, shallowMount } from '@vue/test-utils'
// import Vuex from 'vuex'
// import Play from '@/components/Play.vue'
// // import store from '@/store/mainStore.js'

// const localVue = createLocalVue()
// localVue.use(Vuex)

// describe('Компонент Play', () => {
//   let getters
//   let store
//   let actions
//   let state
//   const file = {
//     name: 'upload.test.jpg',
//     size: 61416,
//     type: 'image/jpeg',
//     lastModified: 1685642683687,
//     webkitRelativePath: '',
//   }

//   beforeEach(() => {
//     getters = {
//       getFile: () => file,
//     }
//     state = {
//       file: file
//     }
//     actions = {
//       sendFile: jest.fn(),
//       setCountColors: jest.fn(),
//     }
//     store = new Vuex.Store({
//       getters,
//       actions,
//       state
//     })
//   })
//   const wrapper = shallowMount(Play, { localVue, store })

//   it("вызывает запись количества цветов в хранилище при выборе", () => {
//     const input = wrapper.find('b-form-select')
//     wrapper.setData({ wannaColors: 12 })
//     input.element.value = 12
//     input.trigger('change')
//     expect(store.actions.setCountColors(wrapper.vm.wannaColors)).toHaveBeenCalled()
//   })

//   // it('отображается кнопка старта когда загружен файл и ввыбрано количество цветов', () => {
//   //   wrapper.setData({ wannaColors: 12 })
//   //   const img = wrapper.find('img')
//     // await wrapper.vm.$nextTick()
//   // })
// })
