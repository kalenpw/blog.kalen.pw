### React + Laravel + Nginx ###

In this tutorial we'll create a simple password generator app with an API powered by Laravel, a frontend in React, all served via Nginx.

This assumes no experience in any of these technologies, but this just shows how to integrate them. You'll want to go through each ones individual tutorials. 

#### React Prereqs ####
##### Skip if you already have nodejs and npm installed ######
The order in which you setup React or Laravel doesn't matter, but I generally prefer to do the Frontend first with dummy JSON data that I can change on the fly in case I see changes to make.

Before installing React, you'll need to ensure you have the proper prerequistes installed, Node.js and npm.

To check if you already have Node installed open a terminal and run 
`nodejs --version`
If you have it installed you'll see something like this
`v13.6.0`
If you had Nodejs installed you likely have npm installed and check with 
`npm --version`
and see
`6.13.4`

If you don't have either installed you'll need to [follow the directions to install both](https://github.com/nodesource/distributions/blob/master/README.md#debinstall) at the time of writing this you can do so with
```
curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
sudo apt-get install -y nodejs
```
once that is completed you will have Nodejs and npm installed. You can check by running `nodejs --version` and `npm --version`

#### React ####
We'll use [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) to bootstrap our React project.

```
npx create-react-app password-generator-ui
cd password-generator-ui
npm start
```
Note: `npx` is installed with npm.

This should have opened a browser tab to `localhost:3000` and displayed the React default screen.
# todo image