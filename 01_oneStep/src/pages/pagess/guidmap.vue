<template>
<iframe src="static/map.html" frameborder="0" width="100%" height="600px"></iframe>
</template>
<script>
import { onMounted } from 'vue';

export default {
    setup() {
        onMounted(() => {
            document.getElementsByTagName('iframe')[0].height=document.documentElement.clientHeight-100;
        })
    }
}

</script>
