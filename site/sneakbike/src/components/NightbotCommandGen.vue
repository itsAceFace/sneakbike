<template>
  <div class="nightbot-command-gen">
    <v-card class="mx-auto" max-width="600" outlined>
      <v-card-text>
        <p>
          <b>!game Retro</b>
        </p>
        <p>
          <b>!title Sneakbike Mystery Race with Friends! :']</b>
        </p>
        <p>
          <b>!runners {{runners}}</b>
        </p>
        <p>
          <b>!commentators {{commentators}}</b>
        </p>
      </v-card-text>
    </v-card>
    <br />

    <v-row>
      <v-col>
        <v-text-field
          label="Commentator 1 Name"
          placeholder="Commentator 1"
          v-model="commentator1Name"
          outlined
        />
      </v-col>
      <v-col>
        <v-text-field
          label="Commentator 1 Twitch Username"
          placeholder="commentator1"
          v-model="commentator1Twitch"
          outlined
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field
          label="Commentator 2 Name"
          placeholder="Commentator 2"
          v-model="commentator2Name"
          outlined
        />
      </v-col>
      <v-col>
        <v-text-field
          label="Commentator 2 Twitch Username"
          placeholder="commentator2"
          v-model="commentator2Twitch"
          outlined
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field label="Runner 1 Name" placeholder="Runner 1" v-model="runner1Name" outlined />
      </v-col>
      <v-col>
        <v-text-field
          label="Runner 1 Twitch Username"
          placeholder="runner1"
          v-model="runner1Twitch"
          outlined
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field label="Runner 2 Name" placeholder="Runner 2" v-model="runner2Name" outlined />
      </v-col>
      <v-col>
        <v-text-field
          label="Runner 2 Twitch Username"
          placeholder="runner2"
          v-model="runner2Twitch"
          outlined
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field label="Runner 3 Name" placeholder="Runner 3" v-model="runner3Name" outlined />
      </v-col>
      <v-col>
        <v-text-field
          label="Runner 3 Twitch Username"
          placeholder="runner3"
          v-model="runner3Twitch"
          outlined
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-text-field label="Runner 4 Name" placeholder="Runner 4" v-model="runner4Name" outlined />
      </v-col>
      <v-col>
        <v-text-field
          label="Runner 4 Twitch Username"
          placeholder="runner4"
          v-model="runner4Twitch"
          outlined
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "NightbotCommandGen",
  data() {
    return {
      runner1Twitch: "",
      runner2Twitch: "",
      runner3Twitch: "",
      runner4Twitch: "",
      runner1Name: "",
      runner2Name: "",
      runner3Name: "",
      runner4Name: "",
      commentator1Twitch: "",
      commentator2Twitch: "",
      commentator1Name: "",
      commentator2Name: "",
    };
  },
  computed: {
    runners() {
      const names = [
        this.runner1Name,
        this.runner2Name,
        this.runner3Name,
        this.runner4Name,
      ];
      const twitch = [
        this.runner1Twitch,
        this.runner2Twitch,
        this.runner3Twitch,
        this.runner4Twitch,
      ];

      let txt = [];
      for (var idx = 0; idx < 4; idx++) {
        if (names[idx] !== "") {
          if (twitch[idx] !== "") {
            txt.push(names[idx] + " :: https://twitch.tv/" + twitch[idx]);
          } else {
            txt.push(names[idx]);
          }
        }
      }

      return txt.join(" || ");
    },
    commentators() {
      const names = [this.commentator1Name, this.commentator2Name];
      const twitch = [this.commentator1Twitch, this.commentator2Twitch];

      let txt = [];
      for (var idx = 0; idx < 2; idx++) {
        if (names[idx] !== "") {
          if (twitch[idx] !== "") {
            txt.push(names[idx] + " :: https://twitch.tv/" + twitch[idx]);
          } else {
            txt.push(names[idx]);
          }
        }
      }

      return txt.join(" || ");
    },
  },
};
</script>
