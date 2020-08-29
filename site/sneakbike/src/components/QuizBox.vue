<template>
  <div class="quiz-box">
    <v-card class="mx-auto" max-width="450px">
      <v-img
        class="white--text align-end"
        height="450px"
        width="450px"
        :src="require(`@/assets/quiz/quiz_${quizList['number']}.png`)"
      />
      <v-card-subtitle class="overline mb-4">Question {{quizList['number']}}</v-card-subtitle>
      <v-card-text class="text--primary">{{quizList['question']}}</v-card-text>
      <v-card-actions>
        <!-- TODO: Not sure how to do a v-for with v-radio buttons. -->
        <v-radio-group v-model="questionAnswer" column>
          <v-radio :label="quizList['answer'][0]['label']" :value="quizList['answer'][0]['value']" />
          <v-radio :label="quizList['answer'][1]['label']" :value="quizList['answer'][1]['value']" />
          <v-radio :label="quizList['answer'][2]['label']" :value="quizList['answer'][2]['value']" />
          <v-radio
            v-if="quizList['answer'][3]['label'] !== null"
            :label="quizList['answer'][3]['label']"
            :value="quizList['answer'][3]['value']"
          />
        </v-radio-group>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "QuizBox",
  props: {
    number: Number,
    question: String,
    quizList: Object,
  },
  data() {
    return { questionAnswer: null };
  },
};
</script>

<style lang="scss">
.quiz-box {
  margin-top: 1rem;
  margin-bottom: 2rem;
}
</style>