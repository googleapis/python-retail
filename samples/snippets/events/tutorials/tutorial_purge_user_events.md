# **Purge User Events Tutorial**

## Let's get started

The Retail API expose methods for managing user events.
If you want to purge the user events from the catalog you can use the **```PurgeUserEvents```** method.


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

## Purge user events

Sending the ```PurgeUserEventsRequest``` you need to specify the following fields: 
 - **```parent```** - Required field. The parent catalog name, such as projects/<YOUR_PROJECT_NUMBER>/locations/global/catalogs/default_catalog.
 - **```filter```** - Required field. The filter string to specify the events to be deleted. Empty string filter is not allowed. 
   The eligible fields for filtering are:
   - eventType: UserEvent.event_type string.
   - eventTime: in ISO 8601 "zulu" format.
   - visitorId: Specifying this will delete all events associated with a visitor.
   - userId: Specifying this will delete all events associated with a user.
 - **```force```** - If force is set to **false**, the method will return the expected purge count without deleting any user events, 
   if set to **true** the user events will actually purge from the catalog.

You can check the **PurgeUserEventsRequest** example in the ```events/purge_user_event.py``` file.

The **filter** field is set with the value:

```filter = 'visitorId="123abc"```

Run the code sample in the Terminal with the following command:

```bash
python events/purge_user_event.py
```

In a result the longrunning operation is started. You can check the operation name in the Terminal output.

The purge operation may last long time, up to 24 hours. If the longrunning operation is successfully done, then ```purged_events_count``` is returned in the google.longrunning.Operations.response field.

## Error handling

Next, let's check the error handling. Send a request with invalid filter.

Find the comment ```# TO CHECK ERROR HANDLING SET INVALID FILTER HERE::```, and set the filter field with some invalid value.

```purge_user_event_request.filter = 'invalid="123abc"'```

Run the same code sample again:
```bash
python events/purge_user_event.py
```

Check the error message appeared, it should be like the following:

```none
google.api_core.exceptions.InvalidArgument: 400 Invalid filter 'invalid="123abc"'. '=' can not be specified with 'invalid' Valid filter examples: 
eventTime>"2012-04-23T18:25:43.511Z" eventTime<"2012-04-23T18:25:43.511Z" eventType=search visitorId="someVisitorId"
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to purge the user events. We encourage you to exercise in purging the user events using different filters.

**Thank you for completing this tutorial!**
