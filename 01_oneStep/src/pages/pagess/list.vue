<template>
  <div class="q-pa-sm">
    <q-splitter
      v-model="splitterModel"
      disable
    >

      <template v-slot:before>
        <q-page-sticky position="top-left">
          <q-tabs
            v-model="tab"
            vertical
            class="text-teal"
          >
            <q-tab
              v-for="i in tabpanel"
              :name=i.name
              :key="i"
              :label=i.label
            />
          </q-tabs>
        </q-page-sticky>
      </template>

      <template v-slot:after>
        <q-tab-panels
          v-model="tab"
          animated
          vertical
          transition-prev="jump-up"
          transition-next="jump-up"
        >
          <q-tab-panel
            v-for="i in tabpanel"
            :name=i.name
            :key="i"
            :label=i.label
          >
            <q-card>
              <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
                <div class="text-h5 absolute-bottom text-right">
                  {{i.label}}
                </div>
              </q-img>
              <q-list>
                <q-item
                  clickable
                  v-for="i in card"
                  :key="i"
                >
                  <q-item-section>
                    <q-img :src=i.imgsrc />
                  </q-item-section>

                  <q-item-section>
                    <q-item-label hreader>{{i.item_name}}</q-item-label>
                    <q-item-label overline>￥{{i.item_prince}}</q-item-label>
                    <q-item-label caption>{{i.item_desc}}</q-item-label>
                  </q-item-section>
                </q-item>
              </q-list>
            </q-card>
          </q-tab-panel>
        </q-tab-panels>
      </template>
    </q-splitter>
  </div>
</template>

<script>
import { ref, reactive, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import { api } from 'boot/axios';


export default {
  setup () {
    const tabpanel = ref([{
      name: '1',
      label: '暂无信息'
    }])
    const card = ref([{
      imgsrc: "https://cdn.quasar.dev/img/parallax2.jpg",
      item_name: "商品名称",
      item_prince: "0",
      item_desc: "商品描述"
    }])
    const route = useRoute()


    function load (a) {
      api.get('/ct_list?loc=' + a)
        .then((response) => {
          if (response['data']['tab'].flag != '0') {
            tabpanel.value = response['data']['tab']
            card.value = response['data']['card']
          } else {
            console.log('null')
          }

        })
        .catch(error => {
          console.log(error)
        })
    }


    onMounted(() => {
      load(route.params.loc)
    })

    return {
      splitterModel: 30,
      tabpanel,
      card,
      load,
      tab: ref('1'),
    }
  }
}
</script>
