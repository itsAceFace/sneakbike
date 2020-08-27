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
    <h1>(IN PROGRESS. NOT DONE!)</h1>
    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        src="@/assets/images/quiz_1.png"
      />
      <v-card-subtitle class="overline mb-4">Question 1</v-card-subtitle>
      <v-card-text
        class="text--primary"
      >You see this starting screen. How easy are the next 30 minutes going to be for you?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question1Answer" column>
          <v-radio label="This game?  Ezpz." value="1" />
          <v-radio label="Not bad --- we can have infinte lives, right?" value="0" />
          <v-radio label="Oh.  This is going to be rough." value="-1" />
          <v-radio label="I've never seen this game before in my dang life." value="-1.5" />
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
        src="@/assets/images/quiz_2.png"
      />
      <v-card-subtitle class="overline mb-4">Question 2</v-card-subtitle>
      <v-card-text
        class="text--primary"
      >What does jumping on this little red-and-yellow flashing dude give you?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question2Answer" column>
          <v-radio label="Magic Cape that turns Mario Invisible." value="0" />
          <v-radio label="Wait, what is this game?" value="-1.5" />
          <v-radio label="A fire-flower." value="-1" />
          <v-radio label="A feather." value="1" />
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
        src="@/assets/images/quiz_3.png"
      />
      <v-card-subtitle class="overline mb-4">Question 3</v-card-subtitle>
      <v-card-text
        class="text--primary"
      >You see this hole with a vine coming out on your adventure. Can you jump into the hole?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question3Answer" column>
          <v-radio label="Yeah, but if you want to be careful, ride the vine down." value="1" />
          <v-radio
            label="I jump into every hole I see in a video game, regardless of context."
            value="0"
          />
          <v-radio label="No, you can never jump in a hole in video games." value="-1" />
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
        src="@/assets/images/quiz_4.png"
      />
      <v-card-subtitle class="overline mb-4">Question 4</v-card-subtitle>
      <v-card-text class="text--primary">What does this blue character "gotta" do?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question4Answer" column>
          <v-radio label="Save the Princess." value="-1.5" />
          <v-radio label="Get his Bananas back." value="-1" />
          <v-radio label="Go Fast." value="1" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 5</v-card-subtitle>
      <v-card-text class="text--primary">What is this character trying to accomplish?</v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question5Answer" column>
          <v-radio
            label="He is trying to penetrate the Pirates' base and destroy Mother Brain."
            value="-1"
          />
          <v-radio
            label="It is trying to penetrate the Pirates' base and destroy Mother Brain."
            value="-1.5"
          />
          <v-radio
            label="She is trying to penetrate the Pirates' base and destroy Mother Brain."
            value="1"
          />
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
        src="@/assets/images/quiz_6.png"
      />
      <v-card-subtitle class="overline mb-4">Question 6</v-card-subtitle>
      <v-card-text class="text--primary">
        What happens when you collect all of the letters in
        <code>KONG</code> in any of the SNES Donkey Kong Country games?
      </v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question6Answer" column>
          <v-radio label="You get a coin to use at the Casino." value="-1" />
          <v-radio label="You get an extra life." value="1" />
          <v-radio label="It ends the level." value="-1.5" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 7</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question7Answer" column>
          <v-radio label="." value="-1" />
          <v-radio label="." value="-1.5" />
          <v-radio label="." value="1" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 8</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question8Answer" column>
          <v-radio label="." value="-1" />
          <v-radio label="." value="-1.5" />
          <v-radio label="." value="1" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 9</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question9Answer" column>
          <v-radio label="." value="-1" />
          <v-radio label="." value="-1.5" />
          <v-radio label="." value="1" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 10</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question10Answer" column>
          <v-radio label="." value="-1" />
          <v-radio label="." value="-1.5" />
          <v-radio label="." value="1" />
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
        src="@/assets/images/quiz_5.png"
      />
      <v-card-subtitle class="overline mb-4">Question 11</v-card-subtitle>
      <v-card-text class="text--primary"></v-card-text>
      <v-card-actions>
        <v-radio-group v-model="question11Answer" column>
          <v-radio label="." value="-1" />
          <v-radio label="." value="-1.5" />
          <v-radio label="." value="1" />
        </v-radio-group>
      </v-card-actions>
    </v-card>

    <br />
    <br />
  </div>
</template>

<script>
// Rookie, Experienced, Veteran

export default {
  name: "RankingQuiz",
  data() {
    return {
      question1Answer: null,
      question2Answer: null,
      question3Answer: null,
      question4Answer: null,
      question5Answer: null,
      question6Answer: null,
      question7Answer: null,
      question8Answer: null,
      question9Answer: null,
      question10Answer: null,
      question11Answer: null,
      question12Answer: null,
      question13Answer: null,
      question14Answer: null,
      question15Answer: null,
      question16Answer: null,
      question17Answer: null,
      question18Answer: null,
      question19Answer: null,
      question20Answer: null
    };
  }
};
</script>
