<template>
  <div class="race-checklist">
    <p>
      <b>IN PROGRESS, NOT FINAL.</b>
    </p>

    <v-radio-group v-model="selectedJob">
      <v-radio
        v-for="(job, index) in jobs"
        :key="`job-${index}`"
        :label="job.toUpperCase()"
        :value="job"
      ></v-radio>
    </v-radio-group>

    <ChecklistJob :dutiesJOB="duties[selectedJob]" :key="selectedJob" />
  </div>
</template>

<script>
// import { values } from "lodash";
import ChecklistJob from "@/components/ChecklistJob.vue";

const jobs = ["host", "c1", "c2", "m1", "gamepicker"];

const duties = {
  host: {
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
  },
  c1: {
    "Before Race Day": [
      "Check that each runner has a functioning OBS with Sneakbike profile.",
      "Check that each runner has a functioning Emulator for the relevant system.",
      "Check that each runner has configured their controller correctly by having them run a test game.",
    ],
    "Race Day": ["Have the canned opening and closing ready to read off."],
    "During Race": [
      "Shout out racers, host, main mod or mods, and commentators.",
    ],
    // "After Race": [],
  },
  c2: {
    "Before Race Day": [
      "Test the games in the Zip file to make sure they're all correct.",
    ],
    "Race Day": ["Mute all runners when the race is about to start."],
    "During Race": [
      "Find a raid when it gets close to the end (probably when the runners get into the post-race room).",
      "Unmute runners when doing runner interviews.",
    ],
    // "After Race": [],
  },
  gamepicker: {
    "Before Race Day": [
      "Choose console and games.",
      "Pick Objectives for games.",
      "Validate game and objective choices with commenatators.",
      "Once validated with commenators, use the README Generator to generate a readme for the runners.",
      "Rename the games '1', '2', '3' and zip them in a folder with the README.",
      "Send the zip file to the commentators.",
    ],
  },
  m1: {
    // "Before Race Day": [],
    // "Race Day": [],
    "During Race": ["Moderate Chat."],
    // "After Race": [],
  },
};

// const dutiesWHO = {
//   "Before Race Day": [
//     "Make the racers 'current-racer' role in discord.",
//     "Make the commentators 'Sneak-Ops' role in discord.",
//     "Have overlay ready.",
//     "Have background ready.",
//     "Have runners fill out running forms.",
//   ],
//   "Race Day": [
//     "Set the game and title?  Is this the Host?  Will this re-set if they stream after it is set in chat?",
//   ],
//   // "During Race": [],
//   "After Race": ["Remove 'current-racer' tag from racers."],
// };

export default {
  name: "RaceChecklist",
  data() {
    return {
      duties,
      jobs,
      selectedJob: "host",
    };
  },
  components: { ChecklistJob },
};
</script>
