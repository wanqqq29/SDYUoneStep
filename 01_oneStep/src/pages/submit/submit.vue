<template>
  <div class="q-pa-md">
    <div
      class="q-gutter-y-md"
      style="max-width: 600px"
    >
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab
            name="service"
            label="服务页"
          />
          <q-tab
            name="alarms"
            label="Alarms"
          />
          <q-tab
            name="movies"
            label="Movies"
          />
        </q-tabs>

        <q-separator />

        <q-tab-panels
          v-model="tab"
          animated
        >
          <q-tab-panel name="service">
            <div class="text-h6">服务页</div>
            <q-form
              action="http://127.0.0.1:8000/submitApi/?pos=service"
              method="post"
              @submit="onSubmit"
              @reset="onReset"
              class="q-gutter-md"
            >
              <q-input
                filled
                v-model="formValue.label"
                label="标题"
                name="label"
                hint="服务页内容标题"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please type something']"
              />
              <q-input
                filled
                v-model="formValue.href"
                label="目标链接"
                name="href"
                hint="外站链接需带有HTTP://或HTTPS://"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please type something']"
              />
              <q-input
                filled
                v-model="formValue.color"
                label="背景颜色"
                name="color"
                hint="颜色参考http://www.quasarchs.com/style/color-palette/#%E9%A2%9C%E8%89%B2%E5%88%97%E8%A1%A8"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please type something']"
              />
              <q-input
                filled
                v-model="formValue.icon"
                label="图标"
                name="icon"
                hint="图标参考https://fonts.google.com/"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please type something']"
              />
              <q-option-group
                v-model="formValue.type"
                :options="optionGroup"
                color="primary"
                name="type"
              />
              <div>
                <q-btn
                  label="Submit"
                  type="submit"
                  color="primary"
                />
                <q-btn
                  label="Reset"
                  type="reset"
                  color="primary"
                  flat
                  class="q-ml-sm"
                />
              </div>
            </q-form>

          </q-tab-panel>

          <q-tab-panel name="alarms">
            <div class="text-h6">Alarms</div>

          </q-tab-panel>

          <q-tab-panel name="movies">
            <div class="text-h6">Movies</div>
            Lorem ipsum dolor sit amet consectetur adipisicing elit.
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>



<script>
import { ref, reactive } from 'vue'

export default {
  setup() {
    const optionGroup = [
      {
        label: '教学服务',
        value: '0'
      }, 
      {
        label: '生活服务',
        value: '1'
      }, 
      {
        label: '餐厅',
        value: '2'
      }, 
      {
        label: '饮品',
        value: '3'
      }, 
      {
        label: '北苑广场',
        value: '4'
      }
]
    const formValue = reactive({
      label: '',
      href: '',
      color: 'primary',
      icon: '',
      type: '0',
      leixing: 'service'
    })

    return {
      tab: ref('service'),
      formValue,
      optionGroup
    }
  }
}
</script>