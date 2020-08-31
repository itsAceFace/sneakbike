<template>
  <div class="sneakbike-description">
    <h1>What is Sneakbike?</h1>
    <p>
      The Sneakbike Community currently hosts two different events:
      <i>Sneakbike Mystery Races</i> and
      <i>Sneakly Weeklys</i>.
    </p>

    <h2>Sneakbike Mystery Races</h2>
    <p>
      These Mystery Races are events where
      <b>four players</b> at
      approximately the same skill level race to
      <b>complete an objective in each of three "mystery games"</b> &mdash; these games
      aren't known to the racers beforehand and are given to them right before
      the race starts!
    </p>

    <p>
      For more information about being a runner, see
      <router-link :to="'/runner-setup'">the runner setup</router-link>.
    </p>

    <p>
      For more information about getting involved in behind-the-scenes work including commentating, doing audio or visual work, working on the backend, etc., see
      <b>THIS LINK</b>.
    </p>

    <h2>Sneakly Weeklys</h2>
    <p>
      This is the Sneakbike community's "anything goes" event. It's a good time
      to
      <b>try out some new event ideas or to have a community night</b>.
    </p>

    <p>
      In the past we've had non-mystery races, casual playthroughs of weird
      games, learning a speedrun together, teaching streams, and once we all
      hung out and played Ballz 3D.
    </p>

    <p>
      If you have a neat idea and want to try it out, ask if you can make it a
      Sneakly Weekly!
    </p>
  </div>
</template>

<script>
export default {
  name: "SneakbikeDescription",
};
</script>
