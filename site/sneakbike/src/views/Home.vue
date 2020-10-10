<template>
  <div class="home">
    <v-parallax src="@/assets/bkgd_helma_cropped.png" height="400" />

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <SneakbikeDescription />
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SneakbikeDescription from "@/components/SneakbikeDescription.vue";

export default {
  name: "Home",
  components: { SneakbikeDescription },
};
</script>
