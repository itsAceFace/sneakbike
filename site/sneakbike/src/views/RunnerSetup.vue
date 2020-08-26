<template>
  <div class="runner-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <WarningCard>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed tincidunt purus, eu auctor massa. Etiam non faucibus ligula, a hendrerit mi. Nullam finibus sapien vulputate, mattis nisl non, commodo massa. Etiam at sollicitudin ipsum. In in nisl et mauris sollicitudin aliquam. Sed neque tortor, tincidunt consectetur laoreet vitae, pellentesque eu risus. Pellentesque ipsum turpis, gravida nec quam non, aliquam condimentum nunc. Cras id iaculis felis. Duis ornare erat a felis congue, finibus lobortis ante feugiat. Quisque tempor varius sem a dignissim. Integer in diam ac est tincidunt dignissim laoreet in nisi. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed eleifend dapibus quam.</WarningCard>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
import WarningCard from "@/components/WarningCard.vue";

export default {
  name: "RunnerSetup",
  components: { WarningCard },
};
</script>
