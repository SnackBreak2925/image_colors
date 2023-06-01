import { mount } from '@vue/test-utils'
import Upload from '@/components/Upload.vue'

describe('Компонент Upload', () => {
  const wrapper = mount(Upload)

  it('отображает текст для Drag-and-drop', () => {
    expect(wrapper.html()).toContain('<div>Перетащите или <u>нажмите сюда</u> чтобы загрузить файлы.</div>')
  })

  it('предлагает бросить файл когда он перетаскивается', async () => {
    wrapper.setData({ isDragging: true })
    await wrapper.vm.$nextTick()
    expect(wrapper.html()).toContain('<div>Отпустите кнопку мыщи чтобы загрузить файл.</div>')
  })
})
