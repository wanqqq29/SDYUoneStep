<template>
  <q-layout view="hHh lpR fFf">
    <q-header
      elevated
      class="bg-primary text-white"
    >
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          一步山青
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer
      bordered
      class="bg-grey-2 text-white"
    >
      <q-toolbar>
        <q-toolbar-title>
          <div class="row">
            <div class="col"></div>

            <div class="col-12 col-md-auto">
              <q-tabs
                v-model="tab"
                align="justify"
                narrow-indicator
              >
                <q-route-tab
                  class="text-purple col"
                  name="index"
                  label="首页"
                  to="/"
                />
                <q-route-tab
                  class="text-orange col"
                  name="tool"
                  label="服务"
                  to="/tool"
                />
                <q-route-tab
                  class="text-teal col"
                  name="details"
                  label="吃喝玩乐详情页"
                  to="/list"
                />
                <q-route-tab
                  class="text-teal col"
                  name="movies"
                  label="Movies"
                  to="/test"
                />

              </q-tabs>
            </div>

            <div class="col"></div>
          </div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

  </q-layout>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      tab: ref('index')
    }
  }
}
</script>
