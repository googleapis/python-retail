# **Import User Events From the Cloud Storage Tutorial**

## Let's get started

The Retail API offers you an easy way to import your user event data inline. All you need is to create the array of user events and set it as an inline source.

If you want to have the increased privacy of having all authentication occur on the backend and are capable of performing a backend import.

You can find more information about different import types, their restrictions, and use cases in the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a Terminal:
```bash
pip install virtualenv
```
```bash
virtualenv <your-env>
```
```bash
source <your-env>/bin/activate
```
Next, install Google packages:
```bash
pip install google
```
```bash
pip install google-cloud-retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell Terminal to
run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable. It will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Import user events to the Retail catalog from the inline source

To check the example of an import user events request, open **events/import_user_events_inline.py**.

Here, in the ```get_user_events()``` method the user events are created to be used in the ```input_config```.

The **```parent```** field in the **ImportUserEventsRequest** contains a **catalog name** along with a branch number you are going to import your
user events to.

The **```input_config```** field defines the **UserEventInlineSource** as an import source.

To perform the user events import, open Terminal and run the command:

```bash
python events/import_user_events_inline.py
```

## Response analysis

Once you have called the import user events method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of user events set in your Cloud Source.

The operation is completed when the **```operation.done()```** field is set to true. 

Check the result. One of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid user event objects into the catalog.

Check the ```import_operation.metadata.success_count``` field to get the total number of the successfully imported events.

The number of failures during the import is returned to the ```import_operation.metadata.failure_count``` field.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal. It should look like this: 

```
import_summary {
  joined_events_count: 3
}
```

## Errors appeared during the importing

Now, let's try to import a few invalid user event objects and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The ```type``` and ```visitor_id``` fields are required, so if you remove them, you get the invalid user event objects. 

Set some invalid value to the ```user_event.event_type``` field and run the import one more time to get an error message.

The expected error message is like the following:

```
google.api_core.exceptions.InvalidArgument: 400 Unsupported inputConfig.userEventInlineSource.userEvents.eventType invalid.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing user events inline.

**Thank you for completing this tutorial!**
