<template>
  <div class="home">
    <v-parallax src="@/assets/backgrounds/bkgd_helma_cropped.png" height="400" />

    <v-container>
      <v-row justify="center">
        <v-col cols="2" />
        <v-col cols="8">
          <div class="sneakbike-description">
            <h1>
              What
              <i>is</i> Sneakbike?
            </h1>
            <p>Sneakbike is a community of people working towards three primary goals:</p>

            <ul>
              <li>
                <b>Community</b>: Making friends, being nice to each other, and friendly competition.
              </li>
              <li>
                <b>Learning New Skills</b>: A commitment to helping each other grow and learn new things.
              </li>
              <li>
                <b>Usability and Quality of Open-Source Offerings</b>: Striving to make the tools we use as easy as possible for others to pick up and use for their own races.
              </li>
            </ul>

            <h1>What does Sneakbike do?</h1>

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

            <h2>Sneakly Weeklys</h2>
            <p>
              This is the Sneakbike community's "anything goes" event. It's a good time
              to
              <b>try out some new event ideas or to have a community night</b>.
            </p>

            <p>
              In the past we've had
              <i>
                non-mystery races, casual playthroughs of weird
                games, learning a speedrun together, teaching streams,
              </i> and sometimes we just hang out and play games together.
            </p>

            <h2>What's the Sneakbike Toolkit?</h2>
            <p>
              The Sneakbike Toolkit (SBTK) is our lightweight, open-source solution to having a
              number of individuals stream on the same stream. It allows us to easily
              host races with a number of runners.
            </p>

            <info-card>
              For the technical folks, this boils down to a Terraform script which sets
              up an Nginx-RTMP server on a small AWS EC2 instance. The runners stream
              from OBS to the public IP and the race host will use OBS's
              <i>VLC Video Source</i> to display them on the stream.
            </info-card>

            <p>
              To use or play around with the code, check out
              <a
                href="https://github.com/jsal13/sneakbike/"
              >our github</a>.
            </p>
          </div>
        </v-col>
        <v-col cols="2" />
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>
