[![pipeline status](https://gitlab.com/lisael/santa/badges/master/pipeline.svg)](https://gitlab.com/lisael/santa/commits/master)
[![coverage report](https://gitlab.com/lisael/santa/badges/master/coverage.svg)](https://gitlab.com/lisael/santa/commits/master)

# Santa

Declarative JSON-REST api test framework, so simple, it's hard to belive.

- Santa is a concept a 5yo can understand.
- Santa brings so much magic in your life, it's hard to believe before you see.
- Santa loves you all equally. QA people, POs, developers, everyone.
- Writing your wish-list to Santa doesn't involve any Electron-ic or Atom-ic stuff. Just a Notepad.
- Santa gifts are not limited to what's available on the internet. You can craft your own or
  let the elves fulfill your sweetest dreams.
- Don't tell Santa he's my fantasy Postman, he'd get upset.
- You'd better not upset Him.

## Features

- Declarative, git-friendly, YAML syntax
- Ansible-like architecture and lazy jinja templating
- Validator/extractor/context_processors
- Leverage asyncio (with aiohttp client) to parallelize runs
- Interactive test case builder
- Almost everything is easily customisable
    - custom validators
    - custom extractors
    - custom context processors
    - custom tasks
    - custom jinja functions

## Quick start

### Install

At the moment, the project has no released package and must be installed from sources:

```sh
virtualenv --python=/usr/bin/python3 santa
cd santa
. bin/activate
git clone https://gitlab.com/lisael/santa.git
cd santa
pip install -e
```

### Test project

To run the testing project (a modifed version of DRF tutorial):

```sh
make testproj_run
```

Alternatively, use the docker image:

```sh
make docker_run_testproj
```

### Create a project

```sh
mkdir myproject
cd myproject
mkdir {suite,context}
```

### Add a context

A context is a nested map that is passed from one task to the next one. Each
task may use and/or modify the context. 


```sh
$EDITOR context/local.yml
```

```yaml
# myproject/context/local.yml
---
domain: localhost
scheme: http

urls:
  default:
    port: 8080
    scheme: "{{ scheme }}"
    host: "{{ domain }}"
    headers:
      Authorization: "{{ basic_auth(users.admin.username, users.admin.password) }}"
      Content-Type: "application/json"

users:
  admin:
    username: admin
    password: admin
```

This defines a context that is available in all tests.

The context layout is free, the only requirements are:

1. The root object is a map
2. keys of the root map do not start with `_` (reserved for internal use)

However, some good practices may emerge and this kind of inventory per type of
objects we are to manipulate has proven useful.

The values are templated. It's important to understand that the templating is lazy
and is applied when the value is read, and re-evaluated each time the value is read.

The laziness has two interesting consequences:

1. Not all variable have to be defined when the first test starts.
   - However, it must be defined at the time it's used
2. When variables are changed, the value of dependent variables is re-evaluated
   - e.g. if `users.admin.password` changes, `urls.default.headers.Authorization` is
   still correct

### Add a test suite

```sh
$EDITOR suite/snippets.yml
```

```yaml
---
- test:
    name: List snippets
    url:
      $<: urls.default
      path: snippets/
```

The URL is not fully defined here, as it extends the context variable `url.default` using
the special `$<` key.  Only the API endpoint (aka. `path`) is missing in `url.default`.

No method is defined in our `test`, santa assumes `GET`.

### Run the tests

The basic syntax of the command is `santa test <context> <suite>`

```sh
santa test local snippets
```

The result shows one test run and did not fail:

```
suite/snippets.yml: List snippets: OK

Summary
**************************************************
tests: 1    success: 1    skipped: 0    failed: 0
**************************************************
```

### Reusing the context

This local test is nice (albeit small, we're going to expand the test coverage later), but
we'd like to run this tests against multiple environments.

Hopefully, the context can be extended. This provides a clean way to reuse parts of a base
context in child contexts.

Let's define a base context:

```sh
$EDITOR context/base.yml
```

```yaml
---
domain: "{{ undefined('Domain must be set') }}"
scheme: https

urls:
  default:
    scheme: "{{ scheme }}"
    host: "{{ domain }}"
    headers:
      Authorization: "{{ basic_auth(users.admin.username, users.admin.password) }}"
      Content-Type: "application/json"

users:
  admin:
    username: "{{ undefined('Admin username') }}"
    password: "{{ undefined('Admin passord') }}"
```

`undefined` is a builtin template function (as is `basic_auth`) that raises an
`UndefinedError` if the value is accessed. These values are mandatory in
inherited contexts.

Now we can re-write our context to extend base.yml

```sh
$EDITOR context/local.yml
```

```yaml
---
extends: base
domain: localhost
scheme: http

urls:
  default:
    port: 8080

users:
  admin:
    username: admin
    password: admin
```

Run this:

```sh
santa test local snippets
suite/snippets.yml: List snippets: OK

Summary
**************************************************
tests: 1    success: 1    skipped: 0    failed: 0
**************************************************
```

### Assertions

So far, we did call our API endpoint, but apparently we did not check anything in the result
of the call. Well actually, we did. The `test` task validate the HTTP status of the response
against sensible defaults (depending on the method).

We can add a simple validator that checks if expected keys are present in the result:

```sh
$EDITOR suite/snippets.yml
```

```yaml
- test:
    name: List snippets
    url:
      $<: urls.default
      path: snippets/
    validate:
      - json:
          contains:
            - count
            - next
            - previous
            - results
```

Validators are listed in the `test` argument `validate`

```sh
santa test local snippets   
suite/snippets.yml: List snippets: OK

Summary
**************************************************
tests: 1    success: 1    skipped: 0    failed: 0
**************************************************
```

Note that the default HTTP status validator is still run. To override the default
status validator, just add your own:

```yaml
    validate:
      - status: [417]
```

### Going postal

Posting an new snippet is as simple as:

```yaml
- test:
    name: Post test snippet
    method: POST
    url:
      $<: urls.default
      path: snippets/
    json_body:
      title: test.py
      code: |
        from math import sin, pi
        
        sin(pi/2)
      linenos: false
      language: python
      style: vim
```

This works, but we're repeating ourselves a bit, don't we?

The `url` part is the same as in our "List snippets" test. And what if we decide to
add a `/blog/` in our API and to move snippets under `/pastebin/` for namespacing
sake ? Would we change each and every tests that call `/snippets/` to `/pastebin/snippets` ?

We also want to test many ways to call snippets, each one uses all or a part of the `json_body`
we defined here. It would be nice to re-use a json payload with sensible default.

It's time to leverage the context to enforce the DRY principle. We add the `endpoints` mapping
that defines all our endpoints (URLs and payloads). Note that these endpoint are shared amongst
all environments, so we define them once in the base context.

```sh
$EDITOR context/base.yml
```

```yaml
---
domain: "{{ undefined("Domain must be set") }}"
scheme: https

urls:
  default:
    scheme: "{{ scheme }}"
    host: "{{ domain }}"
    headers:
      Authorization: "{{ basic_auth(users.admin.username, users.admin.password) }}"
      Content-Type: "application/json"

users:
  admin:
    username: "{{ undefined("Admin username") }}"
    password: "{{ undefined("Admin passord") }}"

endpoints:
  snippets:
    url:
      $<: urls.default
      path: snippets/
    json:
      title: ""
      code: ""
      linenos: false
      language: null
      style: vim
```

Change the suite accordingly:


```sh
$EDITOR suite/snippets.yml
```

```yaml
- test:
    name: List snippets
    url:
      $<: endpoints.snippets.url
    validate:
      - json:
          contains:
            - count
            - next
            - previous
            - results

- test:
    name: Post test snippet
    method: POST
    url:
      $<: endpoints.snippets.url
    json_body:
      $<: endpoints.snippets.json
      title: test.py
      code: |
        from math import sin, pi
        
        sin(pi/2)
      language: python
```

-- BEGIN TROLL --

It may seem strange to some users to define JSON values in yaml. It's also harder to copy and
paste real payloads.

I, for myself, think that JSON is not a human language and should never be used as a
human-to-machine format.

Anyway, remember that JSON is valid YAML ;).

-- END OF TROLL (quickly resolved, hopefully) --

```sh
santa test local snippets   
```

```
suite/snippets.yml: List snippets: OK
suite/snippets.yml: Post test snippet: OK

Summary
**************************************************
tests: 2    success: 2    skipped: 0    failed: 0
**************************************************
```

### Manipulating the context

There are 4 ways to update a context:

1. Define another context that `extends` the first one
2. Pass an `--extra-var` option at the invocation of the suite
3. Extract data from the result JSON in a test
4. Manipulate the context with `context_processors` defined in the suite.

We've already show the first way and the second is pretty clear. These two methods are
static in the sense that they update the context before the suite is run. The third and
fourth methods, on the other hand are dynamic. They are defined in the suite itself and
react to events occuring during the tests.

#### Extractors

Say that we want to keep track of the snippet we've just posted. On a POST, the API
give us the id of the created snippet in the result JSON. Using an extractor, we can
bind a context variable to any value. Let's add an extractor to the POST:

```sh
$EDITOR suite/snippets.yml
```

```yaml

# ...

- test:
    name: Post test snippet
    method: POST
    url:
      $<: endpoints.snippets.url
    json_body:
      $<: endpoints.snippets.json
      title: test.py
      code: |
        from math import sin, pi
        
        sin(pi/2)
      language: python
    extract:
      - jq:
          pattern: .id
          bind: snippets.first.id
      - jq:
          pattern: .url
          bind: snippets.first.full_url
```

We use the jq extractor that binds a context variable to the result of the given
jq pattern.

Note that if a key is not found on the path of the bond variable, it is simply
created, e.g. those extractors created `snippets`, `snippets.first`, `snippets.first.id`
(bound to the new snippet id) and `snippets.first.full_url` (bound to the new snippet
url)


#### Context processors

If we are to call the new created snippet, we now have to define the URL like this

```yaml
- test:
    name: Get first test
    url:
      $<: endpoints.snippets.url
      path: "{{ endpoints.snippets.url}}{{ snippets.first.id }}/"
```

For the sake or DRYness, we can register this url in `snippets.first` context mapping.

That's exactly what context processors are for:

```sh
$EDITOR suite/snippets.yml
```

```yaml

# ...

- context:
  - copy:
      src: endpoints.snippets.url
      dest: snippets.first.url
  - update:
      snippets.first.url.path: "{{ endpoints.snippets.url.path }}{{ snippets.first.id }}/"

```

`context` is a new task type, that accesses the context. It's a list of context processors that
are run in the order of definition. Here, at first we copy the snippets URL into the new snippet's
info mapping and then we update the path to point to the id of the snippet.

We can check that the contex processor did its job using the `message` task that prints nice formated
messages or raw yaml representing the context:

```sh
$EDITOR suite/snippets.yml
```

```yaml

# ...

- message:
    message: The full url is {{ snippets.first.full_url }}
    context: 
      - snippets
```

```sh
santa test local snippets
```

```
suite/snippets.yml: List snippets: OK
suite/snippets.yml: Post test snippet: OK
suite/snippets.yml: context: OK

The full url is http://localhost:8080/snippets/15/
 snippets:
  first:
    full_url: http://localhost:8080/snippets/15/
    id: 15
    url:
      headers:
        Authorization: 'Basic YWRtaW46YWRtaW4='
        Content-Type: application/json
      host: localhost
      path: snippets/15/
      port: 8080
      scheme: http

suite/snippets.yml: : OK

Summary
**************************************************
tests: 2    success: 2    skipped: 0    failed: 0
**************************************************
```

Now we can use the API to manipulate the first snippet with less boilerplate YAML:

```sh
$EDITOR suite/snippets.yml
```

```yaml

# ... (remove the message to avoid log pollution)


- test:
    name: Get new snippet
    method: GET
    url:
      $<: snippets.first.url
    validate:
      - json:
          partial:
            language: python
```

```sh
santa test local snippets   
```

```
suite/snippets.yml: List snippets: OK
suite/snippets.yml: Post test snippet: OK
suite/snippets.yml: context: OK
suite/snippets.yml: Get new snippet: OK

Summary
**************************************************
tests: 3    success: 3    skipped: 0    failed: 0
**************************************************
```

### More context tricks.

The snippets API is open to multiple users with various permissions. For example, a snippet
has an `owner` field. Only the owner of a snippet can edit the snippet. To tests this we need to
impersonate multiple users. The authentication is HTTP basic auth, and we defined the `default` URL
(which in turn is the base of all URLs) like this:

```yaml
# context/base.yml
---

# ...

urls:
  default:
    port: 8080
    scheme: "{{ scheme }}"
    host: "{{ domain }}"
    headers:
      Authorization: "{{ basic_auth(users.admin.username, users.admin.password) }}"
      Content-Type: "application/json"

# ...

```

The problem that arise here is that the authenticated user is hard-coded in the context: `admin`.

The solution is to use the laziness and late evaluation of the context:

```sh
$EDITOR context/base.yml
```

```yaml
# ...

urls:
  default:
    port: 8080
    scheme: "{{ scheme }}"
    host: "{{ domain }}"
    headers:
      Authorization: "{{ basic_auth(users.current.username, users.current.password) }}"
      Content-Type: "application/json"

# ...
```

The trick consists in using the undefined user `current` to generate the authentication
header. Now we have to set this user to any defined user in a `context` task and all
subsequent requests will correctly authenticate. 

We have to add the `context` task at the top of the snippets suite:


```sh
$EDITOR suite/snippets.yml
```

```yaml
---
- context:
  - copy:
      src: users.admin
      dest: users.current
# ...
```

### More endpoints

Let's test the other endpoint, `/users/`. With all we've already setup it's easy.

First, we add the endpoint definition in the base context

```sh
$EDITOR context/base.yml
```

```yaml
# ...

endpoints:
  snippets:
    url:
      $<: urls.default
      path: snippets/
    json:
      title: ""
      code: ""
      linenos: false
      language: null
      style: vim
  users:
    url:
      $<: urls.default
      path: users/
```

Then we create a suite:

```sh
$EDITOR suite/users.yml
```

```yaml
---
- context:
  - copy:
      src: users.admin
      dest: users.current

- test:
    name: Get users
    url:
      $<: endpoints.users.url
```

Wait a minute... That's not DRY, we're repeating the copy of the user `admin` to
`current`. There must be a way to avoid this.

Suites can include each other. We can use this feature to avoid duplication of code.

Create a suite called `log_as/admin`:

```sh
$EDITOR suite/log_as/admin.yml
```

```yaml
---
- context:
  - copy:
      src: users.admin
      dest: users.current
```

Include this suite in `users.yml` and `snippets.yml`

```sh
$EDITOR suite/users.yml
```

```yaml
---
- include: log_as/admin

- test:
    name: Get users
    url:
      $<: endpoints.users.url
```

```sh
$EDITOR suite/snippets.yml
```

```yaml
---
- include: log_as/admin

- test:
# ...
```

Avoiding code duplication is more future-proof. At the moment, the API implements
only basic HTTP authentication. If we decide to implement token authentication or even
OAuth dance, we only have to change the implementation of `suite/log_as/admin.yml`, and
the `include` task abstract the login logic away.

We can try the new endpoint tests: 

```sh
santa test local users   
```

```
suite/log_as/admin.yml: context: OK
suite/users.yml: include: OK
suite/users.yml: Get users: OK

Summary
**************************************************
tests: 1    success: 1    skipped: 0    failed: 0
**************************************************
```

Note that the log lines are printed when the task is completed. That's why the log is
somewhat hard to follow. The first line is the included context processor, the second
one tels that the inclusion did complete, and the third is the actual test.

The logging logic may change in the future. However, if you have to perform a fine
analysis of a suite result, use alternate outputs like json or yaml:

```sh
santa test local users -o yaml
```

### Run all the suites at once

When we are writing a suite, it's nice to be able to run only what we're currently
working at. (e.g. users or snippets). But when the tests are run, we want to run them
all at once. We can use the include task to create a collection of suites:


```sh
$EDITOR suite/all.yml
```

```yaml
---
- include: snippets

- include: users
```

Run this...

```sh
santa test local all
```

Guess what... We're somehow repeating ourselves. Each of the included suite
includes `log_as/admin` repeating the context update. It's not that
problematic here as we use basic HTTP auth and `log_as/admin` only access the
local memory through the context, but logging as an admin user may require a
HTTP roundtrip or two.

The naive solution is to include `log_as/admin` at the top of `all.yml` and to
remove it from `snippets.yml` and `users.yml`. It works, but we would loose the
ability to run the suites in isolation.

The `require` task is what we need. `require` works like include except that it
keeps track of what suite was required and don't repeat the suite.

```sh
$EDITOR suite/users.yml
```

```yaml
---
- require: log_as/admin

- test:
# ...
```

```sh
$EDITOR suite/snippets.yml
```

```yaml
---
- require: log_as/admin

- test:
# ...
```

Run this...

```sh
santa test local all
```

```
suite/log_as/admin.yml: context: OK
suite/snippets.yml: require: OK
suite/snippets.yml: List snippets: OK
suite/snippets.yml: Post test snippet: OK
suite/snippets.yml: context: OK
suite/snippets.yml: Get new snippet: OK
suite/all.yml: include: OK
suite/users.yml: require: SKIPPED
  suite/log_as/admin.yml already completed
suite/users.yml: Get users: OK
suite/all.yml: include: OK

Summary
**************************************************
tests: 4    success: 4    skipped: 0    failed: 0
**************************************************
```

Internally the completed required suite are kept into the context. This should prevent
from login as user1 -> login as user2 -> login as user1 again. `require` accepts a
second argument that resets previously required suites:

```yaml
- require:
    suite: log_as/user1
    reset: log_as/*
```

`reset` accept globs, but excludes it's own `suite` from the expanded names.

### Run suites in parallel

In continuous integration process, the tests must be fast and should raise issues
as soon as possible. Large functional test suite are slow. To mitigate this issue,
santa allows parallel tests.

Now we two have problems.

Parallel execution is never simple to handle and this feature must be used with much
precautions. To help the user to wrap their head around parallel tests, santa uses
a straightforward technique, the context is simply duplicated and the new context is 
passed to the new "thread", with no possibility to share context values among threads.

This implementation is limiting, and may force the user to repeat themselves but it's
much safer and avoids a whole class of client-side race conditions.

However it's not a silver bullet and the user must care about server-side race
conditions. For example, if a thread counts the snippets in the database while
another one creates snippets and a third thread delete snippets, the first thread is 
in trouble to get consistent and reproducible results. We can't do anything on the
client side to mitigate this uncertainty.

That said, with careful implementation of isolated threads, concurrency may substantially
speed up your test suite.

To run tests in parallel, just replace `include` with `fork`:

```sh
$EDITOR suite/all.yml
```

```yaml
---
- fork: snippets

- fork: users
```

```sh
santa test local all   
```

```
suite/log_as/admin.yml: context: OK
suite/snippets.yml: require: OK
suite/log_as/admin.yml: context: OK
suite/users.yml: require: OK
suite/snippets.yml: List snippets: OK
suite/users.yml: Get users: OK
suite/snippets.yml: Post test snippet: OK
suite/snippets.yml: context: OK
suite/snippets.yml: Get new snippet: OK
suite/all.yml: fork: OK
suite/all.yml: fork: OK

Summary
**************************************************
tests: 4    success: 4    skipped: 0    failed: 0
**************************************************
```

But... `require` did not work as intended, it looks like the second requirement
of `log_as/admin` was not skipped.

Remember that the context is forked in `fork` and also that `require` keeps track
of completed suites in the context.

The context in the suite `users` is not aware of the completion of the requirements
in `snippets`. Moreover, there is no guarantee about the order of execution of the
two `require` tasks.

The solution is to require `log_as/admin` in the umbrella suite:

```sh
$EDITOR suite/all.yml
```

```yaml
---
- require: log_as/admin

- fork: snippets

- fork: users
```

Now, the admin is logged in at the time the contexts fork and the completed
required suites are known in forked contexts:

```sh
santa test local all   
```

```
suite/log_as/admin.yml: context: OK
suite/all.yml: require: OK
suite/snippets.yml: require: SKIPPED
  suite/log_as/admin.yml already completed
suite/users.yml: require: SKIPPED
  suite/log_as/admin.yml already completed
suite/snippets.yml: List snippets: OK
suite/users.yml: Get users: OK
suite/snippets.yml: Post test snippet: OK
suite/snippets.yml: context: OK
suite/snippets.yml: Get new snippet: OK
suite/all.yml: fork: OK
suite/all.yml: fork: OK

Summary
**************************************************
tests: 4    success: 4    skipped: 0    failed: 0
**************************************************
```

Right. Both thread did skip the admin login as it was already done.

## Customization

Create a plugin package

```sh
mkdir plugins
touch plugins/__init__.py
```

Add a custom extractor

```
# the name of the file is not important. Just put stuff where it belong
$EDITOR plugins/extractor.py
```

```python
from santa.extractor import Extractor
from santa.parser import IntField

class Accumulate(Extractor):
    """ Given an array of int as `src` extract the sum of its values """
    # if not set, the yaml name defaults to the lowered classname
    # __yaml_name__ = "accumulate"
    src = StringField()
    bind = ContextValueField()

    async def __call__(self, response, ctx):
        data = await response.json()
        array = data[self.src]
        ctx.bind(self.bind, sum(array), create=True)
```

This class defines an extractor as well as the yaml code required to
call it.

```yaml
---
- test:
    name: Get the sum of stuff
    method: GET
    url:
      extends: urls.default
      path: /api/v12/stuff
    extract:
      - accumulate:
          src: stuff
          bind: stuff.count
```

Custom validators and context processors can be implemented the same
way.
