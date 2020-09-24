<template>
  <div class="race-checklist">
    <v-progress-linear v-model="progressVal" color="blue" />
    <br />
    <p>
      <b>IN PROGRESS, NOT FINAL.</b>
    </p>
    <div v-for="(item, index) in checklistItems" :key="`checklist-item-${index}`">
      <v-checkbox v-model="selected" :value="index">
        <template v-slot:label>
          <span class="checklist-item" v-html="item"></span>
        </template>
      </v-checkbox>
    </div>
  </div>
</template>

<script>
const checklistItems = [
  "(): Have an overlay ready.",
  "(): Have a background ready.",
  "<span class='host'>HOST</span>: <code>terraform apply</code> the server up.",
  "<span class='host'>HOST</span>: Give each runner the RTMP address and give each runner a Key.",
  "<span class='host'>HOST</span>: Each runner should have gameplay appropriately bordered by the overlay.",
  "<span class='host'>HOST</span>: If using game audio: check each runner's audio and balance against a known level.",
  "<span class='host'>HOST</span>: If using background music: make sure the background music starts (and stays) in the upper-green section of the OBS mixer.",
  "<span class='host'>HOST</span>: Test C1 and C2 levels above the music / game audio, as well as relative to each other.",
  "(): Set the game and title?  Is this the Host?  Will this re-set if they stream after it is set in chat?",
  "<span class='host'>HOST</span>: Mute each runner's audio.  (You may selectively unmute later.)",
  "<span class='host'>HOST</span>: Share the live screen with C1 and C2.",
  "<span class='c1'>C1</span>: Use the README Generator to generate a readme for the runners.",
  "<span class='c1'>C1</span>: Rename the games '1', '2', '3' and zip them in a folder with the README.",
  "<span class='c2'>C2</span>: Test the games in the Zip file to make sure they're all correct.",
  "<span class='c1'>C1</span>: Check that each runner has a functioning OBS with Sneakbike profile.",
  "<span class='c1'>C1</span>: Check that each runner has a functioning Emulator for the relevant system.",
  "<span class='c1'>C1</span>: Check that each runner has configured their controller correctly by having them run a test game.",
  "<span class='c1'>C1</span>: Have the canned opening and closing ready to read off.",
];

export default {
  name: "RaceChecklist",
  data() {
    return { selected: [], checklistItems };
  },
  computed: {
    progressVal() {
      return (100.0 * this.selected.length) / checklistItems.length;
    },
  },
};
</script>

<style lang="scss" scoped>
.v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

.checklist-item {
  font-size: 12px !important;
}
</style>