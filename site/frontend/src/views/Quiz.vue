<template>
  <div class="dev-setup">
    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <h1>THE QUIZ</h1>
          <h1>(IN PROGRESS.)</h1>

          <QuizBox :quizList="quizList[0]" :number="0"></QuizBox>
          <QuizBox :quizList="quizList[1]" :number="1"></QuizBox>
          <QuizBox :quizList="quizList[2]" :number="2"></QuizBox>
          <QuizBox :quizList="quizList[3]" :number="3"></QuizBox>
          <QuizBox :quizList="quizList[4]" :number="4"></QuizBox>
          <QuizBox :quizList="quizList[5]" :number="5"></QuizBox>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import QuizBox from "@/components/QuizBox.vue";

const quizList = [
  {
    question:
      "You see this starting screen. How easy are the next 30 minutes going to be for you?",
    number: 1,
    answer: [
      { label: "This game?  Ezpz.", value: "1" },
      { label: "Not bad --- we can have infinte lives, right?", value: "0" },
      { label: "Oh.  This is going to be rough.", value: "-1" },
      {
        label: "I've never seen this game before in my dang life.",
        value: "-1.5",
      },
    ],
  },
  {
    question:
      "What does jumping on this little red-and-yellow flashing dude give you?",
    number: 2,
    answer: [
      { label: "Magic Cape that turns Mario Invisible.", value: "0" },
      { label: "Wait, what is this game?", value: "-1.5" },
      { label: "A fire-flower.", value: "-1" },
      { label: "A feather.", value: "1" },
    ],
  },
  {
    question:
      "You see this hole with a vine coming out on your adventure. Can you jump into the hole?",
    number: 3,
    answer: [
      {
        label: "Yeah, but if you want to be careful, ride the vine down.",
        value: "1",
      },
      {
        label:
          "I jump into every hole I see in a video game, regardless of context.",
        value: "0",
      },
      {
        label: "No, you can never jump in a hole in video games.",
        value: "-1",
      },
      { label: null, value: null },
    ],
  },
  {
    question: 'What does this blue character "gotta" do?',
    number: 4,
    answer: [
      { label: "Save the Princess.", value: "-1.5" },
      { label: "Get his Bananas back.", value: "-1" },
      { label: "Go Fast.", value: "1" },
      { label: null, value: null },
    ],
  },
  {
    question: "What is this character trying to accomplish?",
    number: 5,
    answer: [
      {
        label:
          "He is trying to penetrate the Pirates' base and destroy Mother Brain.",
        value: "-1",
      },

      {
        label:
          "It is trying to penetrate the Pirates' base and destroy Mother Brain.",
        value: "-1.5",
      },

      {
        label:
          "She is trying to penetrate the Pirates' base and destroy Mother Brain.",
        value: "1",
      },
    ],
  },
  {
    question:
      "What happens when you collect all of the letters in KONG in any of the SNES Donkey Kong Country games?",
    number: 6,
    answer: [
      { label: "You get a coin to use at the Casino.", value: "-1" },
      { label: "You get an extra life.", value: "1" },
      { label: "It ends the level.", value: "-1.5" },
      { label: null, value: null },
    ],
  },
];

export default {
  name: "Quiz",
  data() {
    return { quizList };
  },
  components: { QuizBox },
};
</script>
