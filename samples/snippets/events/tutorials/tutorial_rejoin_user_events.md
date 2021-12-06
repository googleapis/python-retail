# **Rejoin User Events Tutorial**

## Let's get started

The Retail API expose methods for managing user events.

The Rejoin operation joins specified events with the latest version of the product catalog.

A user event is considered unjoined if the product it is associated with isn't present in the catalog at the time that the user event is ingested. Unjoined events lack detailed product information and are not as useful to training models and serving results.

In addition to addressing unjoined events, the rejoin operation can be used to correct events that have been joined with the wrong product catalog.

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

## Rejoin user events

The ```RejoinUserEventsRequest``` consists only of two fields: 
 - **```parent```** - Required field. The parent catalog name, such as projects/<YOUR_PROJECT_NUMBER>/locations/global/catalogs/default_catalog.
 - **```user_event_rejoin_scope```** - Required field. The scope of user events to be rejoined with the latest product catalog. If the rejoining aims at reducing number of unjoined events, set UserEventRejoinScope to UNJOINED_EVENTS. If the rejoining aims at correcting product catalog information in joined events, set UserEventRejoinScope to JOINED_EVENTS. If all events needs to be rejoined, set UserEventRejoinScope to USER_EVENT_REJOIN_SCOPE_UNSPECIFIED.

Learn more about the user events in [the Retail documentation](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#rejoinusereventsrequest)

You can check the **RejoinUserEventsRequest** example in the ```events/rejoin_user_event.py``` file.

Run the code sample in the Terminal with the following command:
```bash
python events/rejoin_user_event.py
```

The rejoin operation may last long time, up to 24 hours. If the longrunning operation is successfully done, then ```rejoined_user_events_count```, the number of user events that were joined with the latest product catalogs, is returned.

## Error handling

Next, let's check the error handling. Send a rejoin request with invalid parent.

Find the comment ```# TO CHECK THE ERROR HANDLING TRY TO PASS INVALID CATALOG:``` and uncomment the next line.

Run the same code sample again:
```bash
python events/rejoin_user_event.py
```

Check the error message appeared, it should be like the following:

```none
google.api_core.exceptions.NotFound: 404 catalog_id 'invalid_catalog' not found for project. In most cases, this should be set to 'default_catalog'.
If you just created this resource (for example, by activating your project), it may take up 5 minutes for the resource(s) to be activated.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to rejoin the user events. We encourage you to exercise in rejoining the user events with different UserEventRejoinScope.

**Thank you for completing this tutorial!**
