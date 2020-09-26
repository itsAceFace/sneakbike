<template>
  <div class="race-checklist">
    <p>
      <b>IN PROGRESS, NOT FINAL.</b>
    </p>

    <v-tabs background-color="#92de69" v-model="tab">
      <v-tab value="host">HOST</v-tab>
      <v-tab value="c1">COM1</v-tab>
      <v-tab value="c2">COM2</v-tab>
      <v-tab value="m1">MOD1</v-tab>
      <v-tab value="idk">WHODOESTHIS</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item key="host">
        <br />
        <v-progress-linear v-model="progressValHost" color="blue" />
        <br />
        <div v-for="(dutyList, timeSection, index) in dutiesHOST" :key="`dutiesHOST-${index}`">
          <div class="time-section">
            <span class="time-section">{{timeSection}}</span>
          </div>
          <div
            v-for="(duty, index2) in dutyList"
            :key="`dutiesHOST-dutyList-${timeSection}-${index}-${index2}`"
          >
            <v-checkbox v-model="selectedHost" :value="`dutiesHOST-dutyList-${index}-${index2}`">
              <template v-slot:label>
                <span class="checklist-item">{{duty}}</span>
              </template>
            </v-checkbox>
          </div>
        </div>
      </v-tab-item>

      <v-tab-item key="c1">
        <br />
        <v-progress-linear v-model="progressValC1" color="blue" />
        <br />
        <div v-for="(dutyList, timeSection, index) in dutiesC1" :key="`dutiesC1-${index}`">
          <div class="time-section">
            <span class="time-section">{{timeSection}}</span>
          </div>
          <div
            v-for="(duty, index2) in dutyList"
            :key="`dutiesC1-dutyList-${timeSection}-${index}-${index2}`"
          >
            <v-checkbox v-model="selectedC1" :value="`dutiesC1-dutyList-${index}-${index2}`">
              <template v-slot:label>
                <span class="checklist-item">{{duty}}</span>
              </template>
            </v-checkbox>
          </div>
        </div>
      </v-tab-item>

      <v-tab-item key="c2">
        <br />
        <v-progress-linear v-model="progressValC2" color="blue" />
        <br />
        <div v-for="(dutyList, timeSection, index) in dutiesC2" :key="`dutiesC2-${index}`">
          <div class="time-section">
            <span class="time-section">{{timeSection}}</span>
          </div>
          <div
            v-for="(duty, index2) in dutyList"
            :key="`dutiesC2-dutyList-${timeSection}-${index}-${index2}`"
          >
            <v-checkbox v-model="selectedC2" :value="`dutiesC2-dutyList-${index}-${index2}`">
              <template v-slot:label>
                <span class="checklist-item">{{duty}}</span>
              </template>
            </v-checkbox>
          </div>
        </div>
      </v-tab-item>

      <v-tab-item key="m1">
        <br />
        <v-progress-linear v-model="progressValM1" color="blue" />
        <br />
        <div v-for="(dutyList, timeSection, index) in dutiesM1" :key="`dutiesM1-${index}`">
          <div class="time-section">
            <span class="time-section">{{timeSection}}</span>
          </div>
          <div
            v-for="(duty, index2) in dutyList"
            :key="`dutiesM1-dutyList-${timeSection}-${index}-${index2}`"
          >
            <v-checkbox v-model="selectedM1" :value="`dutiesM1-dutyList-${index}-${index2}`">
              <template v-slot:label>
                <span class="checklist-item">{{duty}}</span>
              </template>
            </v-checkbox>
          </div>
        </div>
      </v-tab-item>

      <v-tab-item key="whodoesthis">
        <br />
        <v-progress-linear v-model="progressValM1" color="blue" />
        <br />
        <div v-for="(dutyList, timeSection, index) in dutiesWHO" :key="`dutiesWHO-${index}`">
          <div class="time-section">
            <span class="time-section">{{timeSection}}</span>
          </div>
          <div
            v-for="(duty, index2) in dutyList"
            :key="`dutiesWHO-dutyList-${timeSection}-${index}-${index2}`"
          >
            <v-checkbox v-model="selectedWHO" :value="`dutiesWHO-dutyList-${index}-${index2}`">
              <template v-slot:label>
                <span class="checklist-item">{{duty}}</span>
              </template>
            </v-checkbox>
          </div>
        </div>
      </v-tab-item>
    </v-tabs-items>

    <!-- <v-expansion-panels v-model="panel" :disabled="disabled" multiple>
      <v-expansion-panel>
        <v-expansion-panel-header>HOST Duties</v-expansion-panel-header>
        <v-expansion-panel-content>
          <div v-for="(dutyList, timeSection, index) in dutiesHOST" :key="`dutiesHOST-${index}`">
            <div v-for="(duty, index2) in dutyList" :key="`dutiesHOST-dutyList-${index2}`">
              <v-checkbox v-model="selected" :value="`dutiesHOST-dutyList-${index2}`">
                <template v-slot:label>
                  <span class="checklist-item">: {{val}}</span>
                </template>
              </v-checkbox>
            </div>
          </div>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>-->
  </div>
</template>

<script>
// import { values } from "lodash";

const dutiesHOST = {
  "Before Race Day": ["Set up Terraform and your OBS Profile."],
  "Race Day": [
    "'terraform apply' the server up.",
    "Give each runner the RTMP address and give each runner a Key.",
    "Each runner should have gameplay appropriately bordered by the overlay.",
    "If using game audio: check each runner's audio and balance against a known level.",
    "If using background music: make sure the background music starts (and stays) in the upper-green section of the OBS mixer.",
    "Test C1 and C2 levels above the music / game audio, as well as relative to each other.",
    "Mute each runner's audio.  (You may selectively unmute later.)",
    "Share the live screen with C1 and C2.",
  ],
  // "During Race": [],
  "After Race": ["!! REMEMBER TO SHUT DOWN SERVER WITH 'terraform destroy'!"],
};

const dutiesC1 = {
  "Before Race Day": [
    "Use the README Generator to generate a readme for the runners.",
    "Rename the games '1', '2', '3' and zip them in a folder with the README.",
    "Check that each runner has a functioning OBS with Sneakbike profile.",
    "Check that each runner has a functioning Emulator for the relevant system.",
    "Check that each runner has configured their controller correctly by having them run a test game.",
  ],
  "Race Day": ["Have the canned opening and closing ready to read off."],
  "During Race": [
    "Shout out racers, host, main mod or mods, and commentators.",
  ],
  // "After Race": [],
};

const dutiesC2 = {
  "Before Race Day": [
    "Test the games in the Zip file to make sure they're all correct.",
  ],
  "Race Day": ["Mute all runners when the race is about to start."],
  "During Race": [
    "Find a raid when it gets close to the end (probably when the runners get into the post-race room).",
    "Unmute runners when doing runner interviews.",
  ],
  // "After Race": [],
};

const dutiesM1 = {
  // "Before Race Day": [],
  // "Race Day": [],
  "During Race": ["Moderate Chat."],
  // "After Race": [],
};

const dutiesWHO = {
  "Before Race Day": [
    "Make the racers 'current-racer' role in discord.",
    "Make the commentators 'Sneak-Ops' role in discord.",
    "Have overlay ready.",
    "Have background ready.",
    "Have runners fill out running forms.",
  ],
  "Race Day": [
    "Set the game and title?  Is this the Host?  Will this re-set if they stream after it is set in chat?",
  ],
  // "During Race": [],
  "After Race": ["Remove 'current-racer' tag from racers."],
};

export default {
  name: "RaceChecklist",
  data() {
    return {
      selectedHost: [],
      selectedC1: [],
      selectedC2: [],
      selectedM1: [],
      selectedWHO: [],
      dutiesHOST,
      dutiesC1,
      dutiesC2,
      dutiesM1,
      dutiesWHO,
      tab: "",
    };
  },
  computed: {
    progressValHost() {
      return (100.0 * this.selectedHost.length) / 10;
    },
    progressValC1() {
      return (100.0 * this.selectedC1.length) / 7;
    },
    progressValC2() {
      return (100.0 * this.selectedC2.length) / 4;
    },
    progressValM1() {
      return (100.0 * this.selectedM1.length) / 1;
    },
    progressValWHO() {
      return (100.0 * this.selectedWHO.length) / 7;
    },
  },
};
</script>

<style lang="scss" scoped>
.v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0 !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}

.checklist-item {
  font-size: 13px !important;
}

span.time-section {
  font-size: 16px;
  font-weight: bold;
}
div.time-section {
  margin-bottom: 1rem !important;
}
</style>