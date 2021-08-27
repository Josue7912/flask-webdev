# Template Inheritance

Emily is still a bit slow to get her app in good shape, so after bribing you with more dog costumes, she's asked you to help overhaul her HTML pages. She's getting super tired of having to copy all her HTML from one page to the next, and rightly so! You remembered from your Flask lessons that Jinja supports **template inheritance** so you know just what to do.

Another thing that bugs you is that her website still looks like it came out right after the birth of the Internet, like the old [SpaceJam](https://spacejam.com/) website. You know just how much better webpages with **Bootstrap** look, so you're planning to make her site look much better. Hopefully she doesn't get mad about the redesign and take back all those dog costumes you've more than earned (although a gift card to Applebee's would have been *so* much better).

___

## Instructions

**Read everything before you start!**

(Before you start, you can copy `app.py` and `costumes.html` from the last lab once you've already solved it.)

Similar to how you inherited your grandfather's itchy sweaters against your own will (thanks gramps), in this lab you'll 1) be using template inheritance to prevent code reuse. Then once you have that, you'll 2) improve the look of the pages with Bootstrap.

### 1. Make a Base Template

The first step is to make a base template. There's a lot you can reuse in these templates, but to make it easier for you, make a base template that defines blocks for:

- `head`
- `title`
- `content` (parent content section)
- `page_content` (renders most of the content within `content`)
- `footer`
- any other sections you think might make sense

(don't add a `header` section just yet, more instructions below)

Then have the other templates reuse that base template. For this lab, keep in mind there is no one right answer. Once you are done with this step, the webpages should look about the same as they did before.

### 2. Bootstrapping the Project

Only after step 1 will you be ready for step 2, which is to add Flask-Bootstrap to the project to improve the look of the pages. Keep the original `style.css` in as it defines CSS classes that are used in the templates.

Once you see that the pages have Bootstrap styles, replace the `<header>` tags with a fancy Bootstrap navigation bar. See the course page on Flask-Bootstrap for the HTML structure for the navbar.

In short, for this step, all you are required to do is:

- add Flask-Bootstrap
- replace the header with a navigation bar
