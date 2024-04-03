# Svelte/Python OCR reader

This is a project to practise basics of Svelte and Python

The plan is to develop it into something that allows you to convert the entries of an analog diary into a digital platform. 
With the help of an AI assistant, you'll also be able to summarise your diary entries, see trends or get feedback based on your goals   


# Frontend

## create-svelte

Everything you need to build a Svelte project, powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/main/packages/create-svelte).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm create svelte@latest

# create a new project in my-app
npm create svelte@latest my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.

# Backend

Python Flask Backend

To start the server: 

```bash
flask --app flaskr run --debug
```

The backend is using a [singleton instance](https://flask.palletsprojects.com/en/3.0.x/tutorial/factory/) of Flask, but that's currently not behaving well with the VSCode debugger, so I might use a simpler approach