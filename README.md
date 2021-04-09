# Continous Delivery with Code Build and App Engine
## Cloud Build
Cloud Build is a service that executes your builds on Google Cloud Platform infrastructure. Cloud Build can import source code from Cloud Storage, Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your specifications, and produce artifacts such as Docker containers or Java archives.

### Cloud Build integration with GitHub
1. Create a Github account.
2. Prepare a GitHub repo with some source code to build.
3. Search for "Google Cloud Build" in github marketplace and setup a plan.
4. Select the repository you want to integrate with Google Cloud.
5. It will redirect to Triggers page in the Google Cloud console.
6. Select Create Tigger and enter the following trigger settings.
    * Name: Enter a name for your trigger.
    * Description (optional): Enter a description for your trigger.
    * Event: Select the repository event to invoke your trigger.
        * Push to a branch: Set your trigger to start a build on commits to a particular branch.
    * Source: Select the repository and the corresponding branch or tag to watch for events.
        * From the list of available repositories, select the desired repository. To connect a new repository.
        * Branch or Tag: Specify a regular expression with the branch or tag value to match.
    * Configuration: Select the build config file located in your remote repository or create an inline build config file to use for your build.
        * Autodected: Select this if your repository already have a cloudbuild.yaml or Dockerfile.
        * Location: Specify the location for your configuration.
            * Repository: If your config file is in located in your remote repository, provide the location of your build config file.  
7. Click Create to save your build trigger.

#### Create build config file.