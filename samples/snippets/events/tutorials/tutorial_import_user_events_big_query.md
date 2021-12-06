# **Import User Events From the BigQuery Table Tutorial**

## Let's get started

The Retail API offers you a convenient way to import user event data from previously loaded BigQuery table.

Using BigQuery table allows you to import massive amounts of user events data with no limits.

To find more information about different import types, their restrictions, and use cases, check the [Retail API documentation](https://cloud.google.com/retail/docs/import-user-events#considerations)

**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a terminal:

```bash
python3 -m venv tutorial-env
```

```bash
source tutorial-env/bin/activate
```

Next, install Google packages:

```bash
python3 -m pip install google
python3 -m pip install google.cloud.retail
python3 -m pip install google.cloud.storage
python3 -m pip install google.cloud.bigquery
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Prepare user events for importing

We have prepared a JSON file with a bunch of valid user events in the "events/resources" directory: 

**resources/user_events.json**

And another JSON file with both valid and invalid products, we will use both of these files as data sources.

**resources/user_events_some_invalid.json**

You can use this file in the tutorial, or, if you want to use your own data, you should update the names of a bucket and a JSON files in the code samples.

You can import events that are **NOT older than 90 days** into the Retail catalog. Otherwise, the import will fail.

To keep our historical user evens more recent, update the timestamps in the **user_events.json** and **user_events_some_invalid.json** files. 
Run this script in a Terminal, and you will get the user events with yesterday's date:

```bash
python  setup/update_user_events_json.py
```

Now, your data are updated and ready to be deployed to the Cloud Storage.

## Create the BigQuery table and upload user events

To upload the data to the BigQuery table you need to create a dataset first, then create table with specific User Events data schema. 
Next, upload data to the table from prepared JSON file. The data in the file should correspond the User Events schema as well.

There is a **resources/user_events.json** with valid products. You should upload it to the **```user_events```** dataset, **```events```** table.

Also, there is a **resources/user_events_some_invalid.json** containing some invalid user events along with valid ones. You should upload it to the **```user_events```** dataset, **```events_some_invalid```** table. This table will be used to demonstrate the error handling.

Run the following code in the Terminal to create tables and import data:
```bash
python events/setup/events_create_bigquery_table.py
```
The dataset "user_events" with both tables are created, check them in [Cloud Console](https://console.corp.google.com/bigquery)

## Create the BigQuery table and upload products from UI admin console

In case if you do not have permissions to run the ```bq``` command and performing the previous step you have got "Permission denied" error, you can try the other way to create the table and upload your data.

### Upload catalog data to Cloud Storage

After you have updated the timestamps in both JSON files:
**resources/user_events.json** and **resources/user_events_some_invalid.json**, you can proceed with uploading these data to Cloud Storage.

In your own project you should create a Cloud Storage bucket and put the JSON file there.
The bucket name must be unique, for convenience it can be named as <YOUR_PROJUCT_ID>_events_<TIMESTAMP>.

To create the bucket and upload the JSON file run the following command in the Terminal:

```bash
python events/setup/events_create_gcs_bucket.py
```
Now you can see the bucket is created in the [Cloud Storage](pantheon.corp.google.com/storage/browser), and the file is uploaded.

The **name of the created GRS bucket** is printed in the Terminal, save it somewhere, you will need it on the next step

### Create the BigQuery table and upload user events

Go to the [BigQuery in Cloud Console](https://console.corp.google.com/bigquery).

1. In the Explorer panel you see the list of your projects. 
2. Click the "three dot" icon next to current project name and chose **Create Dataset** option.
   Set the Dataset Id and click **Create**.
3. Click "three dots" icon next to your new dataset and chose **Create Table**.
   3.1 Set the **Source**: in the field **Create table from** chose **Google Cloud Storage** option.
   Click **Browse** in the **Select file from GCS bucket** and chose the bucket you have created on the previous step. Chose the **user_events.json**, click Select.
   3.2 Set the **Destination** field **Table** with a value **```events```**
   3.3 Next, provide a table **Schema**. Click **Edit as a text** and paste in the field the schema which you can find in the **events/resources/events_schema.json** file.
   Then, click **Create table**.
   
In a result the BigQuery table is created. You can proceed and import user events to the catalog.

## Import user events to the Retail catalog from the BigQuery table

You have already created a BigQuery table, so you can use it in your Retail API import request.

To check the example of an import user events request, open **events/import_user_events_big_query.py**.

The **```parent```** field in the **ImportUserEventsRequest** contains a **catalog name** along with a branch number you are going to import your
user events to.

The **```input_config```** field defines the **BigQuerySource** as an import source.

To perform the user events import, open Terminal and run the command:

```bash
python events/import_user_events_big_query.py
```

## Response analysis

Once you have called the import user events method from the Retail API, the **import operation** has started.

Importing may take some time depending on the size of your BigQuery table.

The operation is completed when the **```operation.done()```** field is set to true. 

Check the result. One of the following fields should be present:
 - **```error```**, if the operation failed.
 - **```result```**, if the operation was successful.

You have imported valid user event objects into the catalog.

Check the ```big_query_operation.metadata.success_count``` field to get the total number of the successfully imported events.

The number of failures during the import is returned to the ```big_query_operation.metadata.failure_count``` field.

The operation is successful, and the operation object contains a **```result```** field.
Check it printed out in a Terminal. It should look like this: 

```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 13500
}
```

## Errors appeared during the importing

Now, let's try to import one invalid user event object and check the error message in the operation response. Note that in this case the operation itself is considered successful.

The ```type``` field is required and should have one of [defined values](https://cloud.google.com/retail/docs/user-events#types). That is, if you set some invalid value, you get the invalid user event object. 

You should create one more BigQuery table **```import_tutorial_invalid```** in the same dataset, dataset that contains such invalid user events.

Follow the instructions described in **Upload user events data to the Cloud Storage bucket** and **Create the BigQuery table with the user events data** steps, use the **resources/user_events_some_invalid.json** as a source.

Let's import from the table with one invalid user event to get an error message.

Go to the code sample, assign a value of ```table_id``` to the table name:

```table_id = "events_some_invalid"```

Now, run the code sample and wait till the operation is completed. 

Next, check the operation printed out to the Terminal.

## Errors appeared during importing. Output analysis

If the operation is completed successfully, you can find a **```result```** field. Otherwise, there would be an **```error```** field instead.

In this case, the operation is considered as successful, and the ```big_query_operation.metadata.success_count``` field contains the number of the successfully imported events, which is "3".

There is one invalid user event in the input table, and the number of failures during the importing in the ```big_query_operation.metadata.failure_count``` field is also "1".

The ```operation.result``` field points to the errors bucket where you can find a JSON file with all the importing errors.

The response is the following: 

```
errors_config {
  gcs_prefix: "gs://945579214386_us_import_user_event/errors14561839169527827068"
}
import_summary {
  joined_events_count: 3
}
```

## Errors appeared due to an invalid request

Next, let's send an invalid import request to check the error message. 

In the code sample, find the **```get_import_events_big_query_request()```** method, and add there a local variable ```default_catalog``` with some invalid catalog name.

Now, run the code again and check the error message. It should look like this:

```
google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.
```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to prepare the data for importing user events from the BigQuery table.

**Thank you for completing this tutorial!**
