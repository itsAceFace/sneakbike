<template>
  <div class="warning-card">
    <v-card class="mx-auto" color="#d6382977" outlined>
      <v-card-text>
        <div class="overline mb-4">
          <v-icon>mdi-alert</v-icon>Warning
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
  name: "WarningCard",
};
</script>