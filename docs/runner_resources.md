# Runner Resources

- [Runner Resources](#runner-resources)
  - [Beginning the Race](#beginning-the-race)

---

---

## Beginning the Race

1. When we're beginning the race, we'll give out an address and password.
   - For example, the address may look like: `rtmp://127.0.0.1:1935/live` and the password like `super_duper_secret`.
2. In OBS, do the following:

   - Go into `File > Settings > Stream`,
   - Select `Service: Custom...`
   - The `Server:` field is where you paste the address from step 1.
   - The `Stream Key` is the password we give you.

   ![OBS RTMP Setup](../static/images/obs_rtmp_setup.PNG)

3. At this point, you should be able to start stream using "Start Streaming" in the OBS program. We'll most likely let you know if everything is working correctly.

**Note**:

- You will **NOT be streaming to Twitch when you hit "Start Streaming"** but rather your stream will go through our RTMP server which will collect everyone's stream and redirect it so we can have multiple people on a single stream.
- Your twitch "on-air" alerts or emails will not go out, as you're not actually streaming to twitch.
