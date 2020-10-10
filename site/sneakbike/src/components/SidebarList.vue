<template>
  <div class="sidebar-list">
    <v-list-item-group color="primary">
      <v-list-item v-for="(item, index) in pageList" :key="`${name}-${index}`" :to="item.route">
        <v-list-item-content>
          <v-list-item-title v-text="item.name" />
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </div>
</template>

<script>
export default {
  name: "SidebarList",
  props: {
    pageList: Array,
    name: String,
  },
};
</script>