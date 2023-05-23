import { mount, shallowMount, createLocalVue } from '@vue/test-utils'
// import Vuex from 'vuex'
// import Colors from "@/components/Colors.vue"
// import Play from "@/components/Play.vue"
import Upload from "../src/components/Upload.vue"

// const localVue = createLocalVue()

// localVue.use(Vuex)

describe('Компонент Upload', () => {
  const wrapper = mount(Upload)

  it('отображает текст для Drag-and-drop', () => {
    expect(wrapper.html()).toContain('<div>Перетащите или <u>нажмите сюда</u> чтобы загрузить файлы.</div>')
  })

  it("предлагает бросить файл когда он перетаскивается", async () => {
    wrapper.setData({ isDragging: true })
    await wrapper.vm.$nextTick()
    expect(wrapper.html()).toContain('<div>Отпустите кнопку мыщи чтобы загрузить файл.</div>')
  })
})
