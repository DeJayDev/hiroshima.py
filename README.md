# Hiroshima.py

Hiroshima removes all instances of songs by viral artist TOKYO'S REVENGE from your Spotify.

## Why?

An Instagram user by the name of \@gthstar confessed that her and TOKYO'S REVENGE had a sexual relationship while she was 14, although she'd tell him she was 16.
At this time, this makes TOKYO'S REVENGE approximiately 20 years old. 

A confirmed source says that among others, TOKYO'S REVENGE:
* had phone sex with this and other minors
* sexted this and other minors
* and "apparently just randomly saying he’s horny in the middle of conversation"

TOKYO'S REVENGE has made a few small "statements" regarding the situation including:
* Speaking on it a "few times"
* Making a Voice Channel in his Discord for everyone to hear him speak, where he owned up to everything and said that the majority of it is true
* Apologized on Instagram Live
* "cried over the phone when apologizing to his friends in a vc, saying how music is really his only way he’s made it out being homeless and such"

This all went on for three years, and the last recorded incident was January of last year.

[Sourced from u/slatatat69 on r/TokyosRevenge](https://www.reddit.com/r/TokyosRevenge/comments/lg46xx/heres_what_we_know_so_far_based_on_what_ive_heard/)

## How?

If you'd no longer like to support TOKYO'S REVENGE musically on Spotify, there's only a couple things to do:

First, create an app for this on Spotify's Developer Dashboard - this ensures that you are in control of your data (and that I don't have to host anything)

1. Go [here](https://developer.spotify.com/dashboard/applications)
2. Select `CREATE AN APP`
3. Name it however you'd like, I called it `Hiroshima.py`
4. Provide a description for Spotify, I provided:
    * "Remove songs by TOKYO'S REVENGE from your playlists"
5. Select `EDIT SETTINGS` and enter `http://localhost:8080` as a `Redirect URI`
6. Scroll down and select `SAVE`
7. Keep this page open, as you will need `Client ID` and `Client Secret`

Install spotipy:

```bash
pip install spotipy
```

Run the following command, providing your `Client ID` and `Client Secret` where requested:
```bash
SPOTIPY_CLIENT_ID=CLIENT_ID SPOTIPY_CLIENT_SECRET=CLIENT_SECRET python hiroshima.py 
```

## Why do you want all these permissions?

The best part is, I don't even need these permissions - you run the code and control all of the data.

### Unsure of what's happening? I've commented hiroshima.py to the best of my ability for you.

However, I will describe the permissions this application requests:

* `user-follow-read`:
    * Description: `Read access to the list of artists and other users that the user follows.`
    * Displayed during Signin: `Access your followers and who you are following. `
    * Why: To build a list of your following so that we may check if TOKYO'S REVENGE is in this list
* `user-follow-modify`:
    * Description: `Write/delete access to the list of artists and other users that the user follows.`
    * Displayed during Signin: `Manage who you are following.`
    * Why: To modify the list built by the above scope, removing TOKYO'S REVENGE.
* `playlist-read-collaborative`:
    * Description: `Include collaborative playlists when requesting a user's playlists.`
    * Displayed during Signin: `Access your collaborative playlists.`
    * Why: To build a list of your playlists to modify. 
* `playlist-read-private`:
    * Description: `Read access to user's private playlists.`
    * Displayed during Signin: `Access your private playlists.`
    * Why: To build a list of your playlists to modify.
* `playlist-modify-public`:
    * Description: `Write access to a user's public playlists.`
    * Displayed during Signin: `Manage your public playlists.`
    * Why: To modify the list built by the above scopes, removing TOKYO'S REVENGE.
* `playlist-modify-private`:
    * Description: `Write access to a user's private playlists.` 
    * Displayed during Signin: `Manage your private playlists.`
    * Why: To modify the list built by the above scopes, removing TOKYO'S REVENGE.
