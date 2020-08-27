<template>
  <div class="about">
    <h1 id="runner-resources">Runner Resources</h1>
    <h2 id="beginning-the-race">Beginning the Race</h2>
    <ol>
      <li>
        When we're beginning the race, we'll give out an address and password.
        <ul>
          <li>
            For example, the address may look like:
            <code>rtmp://127.0.0.1:1935/live</code> and the password like
            <code>super_duper_secret</code>.
          </li>
        </ul>
      </li>
      <li>
        <p>In OBS, do the following:</p>
        <ul>
          <li>
            Go into
            <code>File > Settings > Stream</code>,
          </li>
          <li>
            Select
            <code>Service: Custom...</code>
          </li>
          <li>
            The
            <code>Server:</code> field is where you paste the address from step 1.
          </li>
          <li>
            The
            <code>Stream Key</code> is the password we give you.
          </li>
        </ul>
        <p>
          <img src="@/assets/images/obs_rtmp_setup.png" alt="OBS RTMP Setup" />
        </p>
      </li>
      <li>
        <p>At this point, you should be able to start stream using "Start Streaming" in the OBS program. We'll most likely let you know if everything is working correctly.</p>
      </li>
    </ol>
    <p>
      <strong>Note</strong>:
    </p>
    <ul>
      <li>
        You will
        <strong>NOT be streaming to Twitch when you hit "Start Streaming"</strong> but rather your stream will go through our RTMP server which will collect everyone's stream and redirect it so we can have multiple people on a single stream.
      </li>
      <li>Your twitch "on-air" alerts or emails will not go out, as you're not actually streaming to twitch.</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "RunnerResources",
};
</script>
