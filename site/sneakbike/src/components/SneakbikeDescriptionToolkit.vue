<template>
  <div class="sneakbike-description-framework">
    <h1>What's the Sneakbike Toolkit?</h1>
    <p>
      The Sneakbike Toolkit (SBTK) is our open-source solution to having a
      number of individuals stream on the same stream. It allows us to easily
      host races with a number of runners.
    </p>

    <InfoCard>
      For the technical folks, this boils down to a Terraform script which
      sets up an Nginx-RTMP server on a small AWS EC2 instance. The runners
      stream from OBS to the public IP and the race host will use OBS's
      <i>VLC Video Source</i> to display them on the stream.
    </InfoCard>

    <p>
      To use or play around with the code, check out
      <a
        href="https://github.com/jsal13/sneakbike/tree/master/scripts/terraform"
      >our github</a>.
    </p>
  </div>
</template>

<script>
import InfoCard from "@/components/InfoCard.vue";

export default {
  name: "SneakbikeDescriptionToolkit",
  components: { InfoCard },
};
</script>
