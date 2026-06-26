## Project Submission

TBD

### Submission

> These items must be completed on the **campus platform** as part of your project submission — not in this PR.

- [x] GitHub repository URL provided
- [x] GitHub Pull Request URL provided
- [x] Loom video link provided
- [x] VM IP address provided
- [x] Admin credentials provided

#### Loom Video

- [x] Maximum duration of 5 minutes was respected
- [x] Speech is understandable
- [x] Shows how the application is started
- [x] Briefly demonstrates the implementation of the feature
- [x] Shows how to log into the admin portal
- [x] Products are created via data seed

### Repository

- [x] Contains a Pull Request from the feature branch to the default branch
- [x] Pull Request branch contains more than one commit
- [x] README present and contains a section about the new feature "Tags"

### Implementation

- [x] There is a model named "Tag" that can be assigned to one or more products
- [x] Tags have been added to the admin panel and can be viewed via Django Admin
- [x] The fields `created_at` and `updated_at` are read-only fields and cannot be added or edited via the admin portal
- [x] The Product model has a `tags` property that can be linked to the product via a ManyToMany relation, meaning mulxiple tags can be added to a product in the admin portal
- [x] Tests include test cases that verify the new Tags feature — at minimum one test case covering a failure scenario and one test case verifying a successful execution (i.e. correct creation of a tag)
- [x] The product views have been updated so that tags are displayed on the product page
- [x] The comment field on a product review is cleared after submission
- [x] If a product has no tags, an italic label "no tags available" should be displayed

### README.md

- [x] Heading as H1 — title of the repo/project
- [x] Description of the repository in a maximum of 2–5 complete sentences directly below the title
- [x] Contains a TOC section (Table of Contents)
- [x] Contains a Quickstart section — maximum 10 bullet points with 1–2 lines of text each
- [x] Contains a Usage section — extended usage and configuration guide
- [x] Contains an overview of features as a list; each feature should be explained in 1–3 sentences describing how to use the functionality or what to keep in mind

### .gitignore

- [x] Ignores all known patterns for Python code (`.pyc`, `__pycache__`, `*venv`, `*egg`)
- [x] Ignores all files of type .DS_Store (macOS specific)
- [x] Ignores all patterns related to dotenv (*.env)
- [x] Exception to the dotenv rule: the file `example.env` is not ignoredx
### Testing

- [x] The application can be started in a container and is accessible in the browser at `localhost:<PORT>`
- [x] Static files load correctly (CSS & JS) — Django admin panel looking correct is a good indicator
- [x] Can log into the Django admin portal
- [x] Can create new products via the portal
- [x] Can create new categories via the portal
- [x] Can create new tags via the portal
- [x] Can add tags to products via the admin portal
- [x] The website displays tags on the product pages