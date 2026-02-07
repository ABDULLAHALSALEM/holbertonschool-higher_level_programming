# JavaScript - DOM Manipulation

## Description
This project focuses on learning how to manipulate the Document Object Model (DOM) using JavaScript. It covers various techniques for selecting, modifying, and interacting with HTML elements dynamically.

## Learning Objectives
At the end of this project, you should be able to:
- Select HTML elements using JavaScript
- Understand the difference between ID, class, and tag name selectors
- Modify an HTML element's style
- Get and update an HTML element's content
- Modify the DOM
- Make requests with fetch API
- Listen/bind to DOM events
- Listen/bind to user events

## Requirements
- All files are interpreted on Chrome (version 57.0 or later)
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- Your code should be semistandard compliant
- You are not allowed to use `var`
- HTML should not reload for each action

## Tasks

### 0. Color Me
**File:** `0-script.js`
- Updates the text color of the header element to red (#FF0000)
- Must use `document.querySelector` to select the HTML tag

### 1. Click and turn red
**File:** `1-script.js`
- Updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id `red_header`
- Must use `document.querySelector` to select the HTML tag

### 2. Add `.red` class
**File:** `2-script.js`
- Adds the class `red` to the header element when the user clicks on the tag with id `red_header`
- Must use `document.querySelector` to select the HTML tag

### 3. Toggle classes
**File:** `3-script.js`
- Toggles the class of the header element when the user clicks on the tag with id `toggle_header`
- The header element must always have one class: `red` or `green`
- Must use `document.querySelector` to select the HTML tag

### 4. List of elements
**File:** `4-script.js`
- Adds a `<li>` element to a list when the user clicks on the element with id `add_item`
- Must use `document.querySelector` to select the HTML tag

### 5. Change the text
**File:** `5-script.js`
- Updates the text of the header element to "New Header!!!" when the user clicks on the element with id `update_header`
- Must use `document.querySelector` to select the HTML tag

### 6. Star wars character
**File:** `6-script.js`
- Fetches the character name from the URL: https://swapi-api.hbtn.io/api/people/5/?format=json
- Displays the name in the HTML tag with id `character`
- Must use the Fetch API

### 7. Star Wars movies
**File:** `7-script.js`
- Fetches and lists the title for all movies from the URL: https://swapi-api.hbtn.io/api/films/?format=json
- Lists all titles in the HTML tag with id `list_movies`
- Must use the Fetch API

### 8. Say Hello!
**File:** `8-script.js`
- Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of "hello" from the fetched translation
- Displays the translation in the HTML tag with id `hello`
- Must use the Fetch API

### 9. No jQuery
**File:** `100-script.js`
- Updates the text color of the header element to red (#FF0000)
- Must be executed when the page is loaded
- Must use `document.querySelector` to select the HTML tag

### 10. List, add, remove
**File:** `101-script.js`
- Adds, removes, and clears LI elements from a list when the user clicks
- Must use `document.querySelector` to select the HTML tag


