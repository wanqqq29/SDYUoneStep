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
              v-for="(i,index) in tabpanel.data"
            :name=i.loc
            :key="index"
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
            v-for="(i,index) in tabpanel.data"
            :name=i.loc
            :key="index"
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
                  v-for="ii in card[i.label]"
                  :key="ii"
                >
                  <q-item-section>
                    <q-img :src=ii.imgSrc />
                  </q-item-section>

                  <q-item-section>
                    <q-item-label hreader>{{ii.sName}}</q-item-label>
                    <q-item-label overline>￥{{ii.sPrice}}</q-item-label>
                    <q-item-label caption>{{ii.sDesc}}</q-item-label>
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
    const tabpanel = reactive({
      data:''
    })
    const card = ref([{
      imgSrc: "https://cdn.quasar.dev/img/parallax2.jpg",
      sName: "商品名称",
      sPrince: "0",
      sDesc: "商品描述"
    }])
    const route = useRoute()
    const tab = ref('0')

    // function load (a) {
    //   api.get('/ct_list?loc=' + a)
    //     .then((response) => {
    //       if (response['data']['tab'].flag != '0') {
    //         tabpanel.value = response['data']['tab']
    //         card.value = response['data']['card']
    //       } else {
    //         console.log('null')
    //       }

    //     })
    //     .catch(error => {
    //       console.log(error)
    //     })
    // }
 function load (a) {
      api.get('http://127.0.0.1:8000/tabpanelApi/?pos=' + a)
        .then((response) => {
          tabpanel.data = response['data']['tab']
          tab.value = response['data']['tab'][0]['loc']
          console.log(response['data']['tab'])
        })
        .catch(error => {
          console.log(error)
        })

        api.get('http://127.0.0.1:8000/cardApi/')
        .then((response) => {
          card.value = response['data']
        })
        .catch(error => {
          console.log(error)
        })
    }


    onMounted(() => {
      load(route.params.pos)
      console.log(route.params.pos,'pos')
      console.log(route.params.loc,'loc')
    })

    return {
      splitterModel: 30,
      tabpanel,
      card,
      load,
      tab,
    }
  }
}
</script>
