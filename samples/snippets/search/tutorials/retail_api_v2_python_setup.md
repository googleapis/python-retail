# Getting started with Google Cloud Retail (Python)

<walkthrough-disable-features toc></walkthrough-disable-features>

#

Learn how to call the Google Cloud Retail API using client libraries:

1.  Create a Google Cloud Project or choose existing one

2.  Enable the Retail API in a Google Cloud project.

3.  Set up authentication.

3.  Use code samples to call the Retail API.

Estimated time to complete:
<walkthrough-tutorial-duration duration="5"></walkthrough-tutorial-duration>

To get started, click **Start**.

## Select your project and enable the Retail API

Google Cloud Platform organizes resources into projects. This allows you to
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet, you can [create New Project](https://pantheon.corp.google.com/projectcreate)

After the project is created, set your PROJECT_ID to a ```project``` variable. 
Run the following command in Terminal:
```bash
gcloud config set project <YOU_PROJECT_ID>
```

Next, proceed with enabling the Retail API:
```bash
gcloud service enable retail
```

To learn how to set up your application, click **Next**.

## Set up authentication

To run a code sample from the Cloud Shell, you need to authenticate. Luckily, Google Cloud makes it easy to use the Application Default Credentials. 

Open Terminal and run the following command to set the project:
```bash
gcloud config set project <YOUR_PROJECT_ID>
```

Click **Authorize** in the Authorization popup.

Next, set your user credentials to authenticate your requests to the Retail API

```bash
gcloud auth application-default login
```

Type 'Y' and press Enter. Click on the link in Terminal. A browser window should appear asking you to log in using your gmail account.

Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

Run the code sample and check the Retail API in action.

To learn how to call the Retail API from the Cloud Shell code samples, click **Next**.

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Install Google Cloud Retail libraries

To run Python code samples for Retail API tutorial, you need to set up your virtual environment.

Run the following commands in a Terminal:
```bash
pip install virtualenv
```
```bash
virtualenv myenv
```
```bash
source myenv/bin/activate
```
Next, install Google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```


## Open CloudShell tutorials

'#Need to add tutorials to some regestry to make them available by ID

<walkthrough-tutorial-card id="retail_api_querying_python_v2" title="Search simple query tutorial" keepPrevious=true>
Learn how to search for products in a catalog using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_pagination_python_v2" title="Search with pagination tutorial" keepPrevious=true>
Learn how to navigate the search results using Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_filtering_python_v2" title="Search with filtering tutorial" keepPrevious=true>
Learn how to filter search results using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_ordering_python_v2" title="Search with ordering tutorial" keepPrevious=true>
Learn how to order search results using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_boosting_python_v2" title="Search with boosting tutorial" keepPrevious=true>
Learn how to prioritize products in the search response using the Retail API</walkthrough-tutorial-card>

<walkthrough-tutorial-card id="retail_api_query_expansion_python_v2" title="Search with query expansion tutorial" keepPrevious=true>
Learn how to enable the query expansion feature using the Retail API</walkthrough-tutorial-card>