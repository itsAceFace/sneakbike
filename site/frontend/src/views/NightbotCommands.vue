<template>
  <div class="nightbot-commands">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Nightbot Command Update</h1>
          <NightbotCommandGen />
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import NightbotCommandGen from "@/components/NightbotCommandGen.vue";
export default {
  name: "NightbotCommands",
  components: { NightbotCommandGen },
};
</script>
