<template>
  <div class="ranking-quiz">
    <h1>So, you wanna know how tough you are, hotshot?</h1>
    <p>
      New runners might not know if they're
      <i>novice, advance</i> or
      <i>expert</i> mystery game players, so we've devised this
      <i>very serious, very legit</i> quiz for you to take.
    </p>

    <hr />
    <br />
    <br />
    <h1>THE QUIZ</h1>
    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="./../static/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 1</v-card-subtitle>
      <v-card-text
        class="text--primary"
      >You see this starting screen. How easy are the next 30 minutes going to be for you?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question1Answer" column>
          <v-radio label="This game?  Ezpz." value="1"></v-radio>
          <v-radio label="Not bad --- we can have infinte lives, right?" value="0"></v-radio>
          <v-radio label="Oh.  This is going to be rough." value="-1"></v-radio>
          <v-radio label="I've never seen this game before in my dang life." value="-1.5"></v-radio>
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />

    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="./../static/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 2</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question2Answer" column>
          <v-radio label value="1"></v-radio>
          <v-radio label value="0"></v-radio>
          <v-radio label value="-1"></v-radio>
          <v-radio label value="-1.5"></v-radio>
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />

    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="./../static/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 3</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question3Answer" column>
          <v-radio label value="1"></v-radio>
          <v-radio label value="0"></v-radio>
          <v-radio label value="-1"></v-radio>
          <v-radio label value="-1.5"></v-radio>
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />

    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="./../static/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 4</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question4Answer" column>
          <v-radio label value="1"></v-radio>
          <v-radio label value="0"></v-radio>
          <v-radio label value="-1"></v-radio>
          <v-radio label value="-1.5"></v-radio>
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />

    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="./../static/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 5</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question5Answer" column>
          <v-radio label value="1"></v-radio>
          <v-radio label value="0"></v-radio>
          <v-radio label value="-1"></v-radio>
          <v-radio label value="-1.5"></v-radio>
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: "RankingQuiz",
  data() {
    return {
      question1Answer: null
    };
  }
};
</script>
