# Galileo Scope Components

Galileo Scope Components is a Dash component library.

Get started with:
1. Install Dash and its dependencies: https://dash.plot.ly/installation
2. Run `yarn build:js-dev`
3. Run `make example`
4. Visit http://localhost:8050 in your web browser

## Usage

1. Add artifactory repository to pip

In `requirements.txt`, add this to the top of the file.
```
--extra-index-url https://artifactory.robot.car/artifactory/api/pypi/galileo-python/simple
```

or in `pip.conf`, add
```conf
extra-index-url = https://artifactory.robot.car/artifactory/api/pypi/galileo-python/simple
```

2. Install `galileo-scope-components`
```
$ pip install galileo-scope-components
```
```
// requirements.txt
dash
dash-html-components
dash-core-components
galileo-scope-components
```

3. Use the components in your `scope.py`
```py
from galileo_scope_components import Layout, Typography

app.layout = Layout([
    Typography('Galileo Scope Components are cool!',
        fontFamily='mono',
        fontSize=5,
        color='red')
])
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md)

### Install dependencies

If you have selected install_dependencies during the prompt, you can skip this part.

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.
    ```
    $ virtualenv venv
    $ venv/Scripts/activate
    ```
    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Write your component code in `src/lib/components/GalileoScopeComponents.react.js`. 

- The demo app is in `src/demo` and you will import your example component code into your demo app.
- Test your code in a Python environment:
    1. Build your code
        ```
        $ npm run build:all
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ make example
        $ $(EDITOR) galileo_scope_components/usage/__init__.py
        ```
- Write tests for your component.
    - A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    - Run the tests with `$ pytest tests`.
    - The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Add custom styles to your component by putting your custom CSS files into your distribution folder (`galileo_scope_components`).
    - Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    - Make sure the stylesheets are added to the `_css_dist` dict in `galileo_scope_components/__init__.py` so dash will serve them automatically when the component suite is requested.
- [Review your code](./review_checklist.md)

### Create a production build and publish:

1. Build your code:
    ```
    $ npm run build:all
    ```
2. Create a Python tarball
    ```
    $ python setup.py sdist
    ```
    This distribution tarball will get generated in the `dist/` folder

3. Test your tarball by copying it into a new environment and installing it locally:
    ```
    $ pip install galileo_scope_components-0.0.1.tar.gz
    ```

4. If it works, then you can publish the component to NPM and PyPI:
    1. Cleanup the dist folder (optional)
        ```
        $ rm -rf dist
        ```
    2. Publish on PyPI
        ```
        $ twine upload dist/*
        ```
    3. Publish on NPM (Optional if chosen False in `publish_on_npm`)
        ```
        $ npm publish
        ```
        _Publishing your component to NPM will make the JavaScript bundles available on the unpkg CDN. By default, Dash servers the component library's CSS and JS from the remote unpkg CDN, so if you haven't published the component package to NPM you'll need to set the `serve_locally` flags to `True` (unless you choose `False` on `publish_on_npm`). We will eventually make `serve_locally=True` the default, [follow our progress in this issue](https://github.com/plotly/dash/issues/284)._
5. Share your component with the community! https://community.plot.ly/c/dash
    1. Publish this repository to GitHub
    2. Tag your GitHub repository with the plotly-dash tag so that it appears here: https://github.com/topics/plotly-dash
    3. Create a post in the Dash community forum: https://community.plot.ly/c/dash

