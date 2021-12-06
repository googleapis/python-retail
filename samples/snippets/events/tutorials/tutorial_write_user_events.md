# **Write User Events Tutorial**

## Let's get started

The Retail API expose methods for managing user events.
If you want to add one user event to the catalog you can use the **```WriteUserEvent```** method.


**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Get started with Google Cloud Retail

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

### Select your project and enable the Retail API

Google Cloud organizes resources into projects. This lets you
collect all the related resources for a single application in one place.

If you don't have a Google Cloud project yet or you're not the Owner of an existing one, you can
[create a new project](https://console.cloud.google.com/projectcreate).

After the project is created, set your PROJECT_ID to a ```project``` variable.
1. Run the following command in Terminal:
    ```bash
    gcloud config set project <YOUR_PROJECT_ID>
    ```

1. Check that the Retail API is enabled for your Project in the [Admin Console](https://console.cloud.google.com/ai/retail/).

### Set up authentication

To run a code sample from the Cloud Shell, you need to authenticate. To do this, use the Application Default Credentials.

1. Set your user credentials to authenticate your requests to the Retail API

    ```bash
    gcloud auth application-default login
    ```

1. Type `Y` and press **Enter**. Click the link in Terminal. A browser window should appear asking you to log in using your Gmail account.

1. Provide the Google Auth Library with access to your credentials and paste the code from the browser to the Terminal.

1. Run the code sample and check the Retail API in action.

**Note**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

### Set the PROJECT_NUMBER environment variable

Because you are going to run the code samples in your own Google Cloud project, you should specify the **project_number** as an environment variable. It will be used in every request to the Retail API.

1. You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

1. Set the environment variable with the following command:
    ```bash
    export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
    ```

### Install Google Cloud Retail libraries

To run Python code samples for the Retail API tutorial, you need to set up your virtual environment.

1. Run the following commands in a Terminal to create an isolated Python environment:
    ```bash
    pip install virtualenv
    virtualenv myenv
    source myenv/bin/activate
    ```
1. Next, install Google packages:
    ```bash
    pip install google
    pip install google-cloud-retail
    pip install google.cloud.storage
    pip install google.cloud.bigquery

    ```

### Clone the Retail code samples

This step is required if this is the first Retail API Tutorial you run.
Otherwise, you can skip it.

Clone the Git repository with all the code samples to learn the Retail features and check them in action.

<!-- TODO(ianan): change the repository link -->
1. Run the following command in the Terminal:
    ```bash
    git clone https://github.com/t-karasova/grs-samples-python.git
    ```

    The code samples for each of the Retail services are stored in different directories.

1. Go to the ```grs-samples-python``` directory. It's our starting point to run more commands.
    ```bash
    cd grs-samples-python
    ```

## Write user event

The ```WriteUserEventRequest``` consists only of two fields: 
 - **```parent```** - Required field. The parent catalog name, such as projects/<YOUR_PROJECT_NUMBER>/locations/global/catalogs/default_catalog.
 - **```user_event```** - Required field. The user event you are going to write. 
   
Learn more about the user events in [the Retail documentation](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#userevent)

You can check the **WriteUserEventRequest** example in the ```events/write_user_event.py``` file.

Run the code sample in the Terminal with the following command:
```bash
python events/write_user_event.py
```

The Retail API returns the created user event. Check the output in the Terminal.


## Error handling

Next, let's check the error handling. Send a request with invalid parent.

Find the comment ```# TO CHECK THE ERROR HANDLING TRY TO PASS INVALID CATALOG:``` and uncomment the next line.

Run the same code sample again:
```bash
python events/write_user_event.py
```

Check the error message appeared, it should be like the following:

```none
google.api_core.exceptions.NotFound: 404 catalog_id 'invalid_catalog' not found for project. In most cases, this should be set to 'default_catalog'.
If you just created this resource (for example, by activating your project), it may take up 5 minutes for the resource(s) to be activated.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to write the user events. We encourage you to exercise in creating the user events by your self.

**Thank you for completing this tutorial!**
