A "sticky" footer - one that sticks to the bottom of the page when there isn't a full screen of content, but is only visible after scrolling to the bottom of a page with more content is a basic feature included in most sites.

With Bootstrap 4 it is quite simple to achieve. 

Add the following css:

```css
/* Sticky Footer Classes */
html,
body {
    height: 100%;
}

body {
    display: flex;
    flex-direction: column;
}

.content-wrapper {
    flex: 1 0 auto;
}

footer {
    flex-shrink: 0;
}
```

and then wrap all your website content in a div with class `content-wrapper` and ensure you use a `<footer>` element for your footer. You could also change the `footer` to `.footer` but using semantic HTML is important.

There are plenty of other ways to do this, but this is the one I've found is the simplest and due to using flex it can handle any amount of content in the footer.