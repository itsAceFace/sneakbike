<template>
  <div class="race-data-tool">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>Race Data Tool</h1>

          <p>
            Used to populate Nightbot commands and the
            <a
              :href="sneaksquadURL"
              target="_blank"
            >Sneaksquad Googledoc</a>.
          </p>

          <hr />
          <br />

          <v-flex class="d-flex flex-wrap">
            <v-text-field
              class="race-data-tool-field"
              label="C1"
              placeholder="Commentator 1"
              v-model="nameC1"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="C2"
              placeholder="Commentator 2"
              v-model="nameC2"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="P1"
              placeholder="Producer 1"
              v-model="nameP1"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="P2"
              placeholder="Producer 2"
              v-model="nameP2"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="Runner1"
              placeholder="Runner 1"
              v-model="nameRunner1"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="Runner2"
              placeholder="Runner 2"
              v-model="nameRunner2"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="Runner3"
              placeholder="Runner 3"
              v-model="nameRunner3"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="Runner4"
              placeholder="Runner 4"
              v-model="nameRunner4"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="GP1"
              placeholder="Game Picker"
              v-model="nameGamePicker"
              outlined
            />
            <v-text-field
              class="race-data-tool-field"
              label="Race Diffulty Level"
              placeholder="Beginner"
              v-model="difficulty"
              outlined
            />
          </v-flex>
          <v-text-field
            class="race-data-tool-field"
            label="Games and System"
            placeholder="(SNES) Ace Ventura 2, Zombies ate The Mask"
            v-model="gamesAndConsole"
            outlined
          />

          <br />
          <hr />
          <br />
          <h3>Nightbot Commands:</h3>

          <ul>
            <li class="command-item">!game Retro</li>
            <li class="command-item">!title Sneakbike Mystery Race with Friends! :']</li>
            <li class="command-item">!commands edit !runners {{runnersString}}</li>
            <li
              class="command-item"
            >!commands edit !commentators The lovely voices you're hearing: {{commentatorsString}}</li>
          </ul>

          <br />
          <hr />
          <br />

          <h3>Sneaksquad Row:</h3>
          <p>
            Copy-paste the row values into the
            <a
              :href="sneaksquadURL"
              target="_blank"
            >Sneaksquad Googledoc</a> starting at the "Level" column. You'll have to manually input the date and VOD.
          </p>
          <table>
            <tr>
              <th>Level</th>
              <th>Commentators</th>
              <th>P1</th>
              <th>P2</th>
              <th>Game Picker</th>
              <th>Runners</th>
              <th>Games</th>
            </tr>
            <tr>
              <td>{{ difficulty !== null ? difficulty.toLowerCase() : ""}}</td>
              <td>{{ [nameC1, nameC2].filter(x => x).join(", ") }}</td>
              <td>{{ nameP1 }}</td>
              <td>{{ nameP2 }}</td>
              <td>{{ nameGamePicker }}</td>
              <td>{{ [nameRunner1, nameRunner2, nameRunner3, nameRunner4].filter(x => x).join(", ")}}</td>
              <td>{{ gamesAndConsole }}</td>
            </tr>
          </table>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
const sneaksquadURL =
  "https://docs.google.com/spreadsheets/d/1HjUhWhGxIt8CMUG3uLbplxpnZq0h3ikcVPGRTUaa-ws/edit?usp=sharing";

export default {
  name: "RaceDataTool",
  data() {
    return {
      nameC1: null,
      nameC2: null,
      nameP1: null,
      nameP2: null,
      nameGamePicker: null,
      nameRunner1: null,
      nameRunner2: null,
      nameRunner3: null,
      nameRunner4: null,
      gamesAndConsole: null,
      difficulty: null,
      sneaksquadURL,
    };
  },
  computed: {
    runnersString() {
      return this.addTwitchURL([
        this.nameRunner1,
        this.nameRunner2,
        this.nameRunner3,
        this.nameRunner4,
      ]).join(" || ");
    },
    commentatorsString() {
      return this.addTwitchURL([this.nameC1, this.nameC2]).join(" || ");
    },
  },
  methods: {
    addTwitchURL(sArray) {
      return sArray
        .map((s) => {
          return s !== null ? `https://twitch.tv/${s}` : null;
        })
        .filter((x) => x);
    },
  },
};
</script>

<style scoped>
.race-data-tool-field {
  margin-right: 1rem;
}

ul {
  padding: 0;
}

.command-item {
  list-style: none;
  font-size: 1.2rem;
  font-family: "Roboto", sans-serif;
  margin-bottom: 1rem;
  color: #3c3684;
  font-weight: bold;
}

table {
  width: 100%;
}

table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  font-size: 0.75rem;
}
th {
  background-color: #999999;
}

td {
  max-width: 150px;
  word-wrap: break-word;
}

h3 {
  margin-bottom: 1rem;
  margin-top: 1rem;
}
</style>
