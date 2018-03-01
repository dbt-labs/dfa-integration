## Manual Authentication Instructions

### Create an app

Create a "Web Application" type app via the Google Developer console, and set the redirect URI to:

```
http://127.0.0.1:3555/
```

Save the `client_id` and `client_secret` somewhere safe, you'll need them later.

### Initialize the OAuth flow

You'll need to make a few requests to get a refresh token from the DFA API.

The first request initializes the OAuth flow for your DFA app. Replace the dummy `<client_id>` in the below URL, and load it in your browser:

```
https://accounts.google.com/o/oauth2/v2/auth?client_id=<client_id>&redirect_uri=http://127.0.0.1:3555/refresh&scope=https://www.googleapis.com/auth/dfareporting https://www.googleapis.com/auth/dfatrafficking&access_type=offline&response_type=code
```

This should take you through a redirect flow, and redirect you to a broken page like:

```
http://127.0.0.1:3555/?code=<code>
```

Copy the code, and move onto the next part.

### Get a refresh token

Now, you want to make a `POST` to generate a refresh token. Replace `<client_id>`, `<client_secret>`, and `<code>` with the respective values when you actually make the request.

```
POST https://www.googleapis.com/oauth2/v4/token

Headers
  Content-Type: application/x-www-form-urlencoded

Body
  code: <code>
  client_id: <client_id>
  client_secret: <client_secret>
  redirect_uri: http://127.0.0.1:3555/refresh
  grant_type: authorization_code
```

This will return a refresh token that you can use to query the DFA API!
