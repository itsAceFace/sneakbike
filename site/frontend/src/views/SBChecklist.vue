<template>
  <div class="raceday-checklist">
    <v-container>
      <v-row>
        <v-col cols="2" />
        <v-col cols="8">
          <h2>Role Description</h2>
          <v-btn depressed @click="showDescriptions = !showDescriptions">Show/Hide Descriptions</v-btn>
          <br />
          <br />
          <div v-if="showDescriptions">
            <ul>
              <li class="roles">
                <b>
                  Production 1
                  <span class="role-abbr">(P1)</span>
                </b>: Responsible for hosting the Sneakbike RTMP server, hosting OBS, importing RTMP streams, adjusting audio.
              </li>
              <li class="roles">
                <b>
                  Production 2
                  <span class="role-abbr">(P2)</span>
                </b>: Responsible for updating Streamelements before and during the race, helping runners set up their consoles and streams before the race, general assistance to P1.
              </li>
              <li class="roles">
                <b>
                  Commentator 1
                  <span class="role-abbr">(C1)</span>
                </b>: Responsible for opening and closing commentary, race commentary, shouting out various runners, mods, etc., and generally pushing the usually-less-experienced C2 to be more comfortable and better at commentating.
              </li>
              <li class="roles">
                <b>
                  Commentator 2
                  <span class="role-abbr">(C2)</span>
                </b>: Responsible for server-muting and announcing things to runners during the race, general commentary, and generally assists C1.
              </li>
              <li class="roles">
                <b>
                  Moderator 1
                  <span class="role-abbr">(M1)</span>
                </b>: Responsible for moderating the channel.
              </li>
              <li class="roles">
                <b>
                  Game Picker
                  <span class="role-abbr">(GP1)</span>
                </b>: Responsible for choosing games before the race, testing games, as well as creating a README and the game zip bundle.
              </li>
            </ul>
          </div>
        </v-col>
        <v-col cols="2"></v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="3" />
        <v-col cols="6">
          <h2>Role Checklist</h2>
          <v-flex class="d-flex flex-wrap">
            <div v-for="name in Object.keys(duties)" :key="`chip-${name}`">
              <v-chip
                class="ma-1"
                :class="{'dimmed-chip': selectedRole !== name}"
                :color="'rgb(99, 103, 174)'"
                @click="changeSelectedRole(name)"
              >
                <span class="chip-text">{{ name }}</span>
              </v-chip>
            </div>
          </v-flex>
        </v-col>
        <v-col cols="3" />
      </v-row>

      <template>
        <v-row justify="center">
          <v-col cols="2" />
          <v-col cols="8">
            <div v-for="timeFrame in Object.keys(selectedDuties)" :key="`tf-${timeFrame}`">
              <h2>{{ timeFrame }}</h2>

              <v-list>
                <v-list-item-group multiple>
                  <v-list-item v-for="duty in selectedDuties[timeFrame]" :key="`tf-duty-${duty}`">
                    <template v-slot:default="{ active, }">
                      <v-list-item-action>
                        <v-checkbox :input-value="active" color="primary"></v-checkbox>
                      </v-list-item-action>

                      <v-list-item-content>
                        <span v-html="duty" />
                      </v-list-item-content>
                    </template>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </div>
          </v-col>
          <v-col cols="2" />
        </v-row>
      </template>
    </v-container>
  </div>
</template>

<script>
import duties from "@/data/checklist.js";

export default {
  name: "SBChecklist",
  data() {
    return {
      duties,
      selectedRole: "P1",
      showDescriptions: true,
    };
  },
  computed: {
    selectedDuties() {
      return this.duties[this.selectedRole];
    },
  },
  methods: {
    changeSelectedRole(name) {
      this.selectedRole = name;
    },
  },
};
</script>

<style scoped>
.roles {
  margin-bottom: 1rem;
}

.role-abbr {
  color: #313791;
  font-family: "Roboto", sans-serif;
}

.chip-text {
  color: white;
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* IE10+/Edge */
  user-select: none; /* Standard */
  cursor: default;
}

.dimmed-chip {
  opacity: 0.45;
}
</style>