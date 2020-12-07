<template>
  <div class="info-card">
    <v-card class="mx-auto" color="#e5e2ff" outlined>
      <v-card-text>
        <div class="overline mb-4">
          <v-icon>mdi-gamepad-variant-outline</v-icon>&nbsp;Note
        </div>
        <p class="text--primary">
          <slot></slot>
        </p>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "InfoCard",
};
</script>