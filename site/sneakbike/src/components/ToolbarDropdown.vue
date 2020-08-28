<template>
  <div class="toolbar-dropdown">
    <v-menu open-on-hover offset-y>
      <template v-slot:activator="{ on }">
        <v-btn text large v-on="on">{{ name }}</v-btn>
      </template>

      <v-card class="mx-auto" max-width="300">
        <v-list>
          <v-list-item-group color="primary">
            <v-list-item
              v-for="(item, index) in pageList"
              :key="`${name}-${index}`"
              :to="item.route"
            >
              <v-list-item-content>
                <v-list-item-title v-text="item.name" />
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
export default {
  name: "ToolbarDropdown",
  props: {
    name: String,
    pageList: Array,
  },
};
</script>
