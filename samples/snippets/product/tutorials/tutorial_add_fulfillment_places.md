# **Update Inventory. Add Fulfillment Places**

## Let's get started

Changes to a product inventory information may occur more frequently than changes to its catalog information.

After the fulfillment availability for some specific places has changed, you may decide to push updates describing this change instead of using the ```UpdateProduct``` method to respecify the entire product fulfillment information.

In such cases, ```AddFulfillmentPlaces``` and ```RemoveFulfillmentPlaces``` methods can be used to incrementally update product fulfillment. The place IDs are added to or removed from a given fulfillment type based on the fulfillment changes.

These methods are asynchronous because of downstream optimizations that support hundreds of concurrent updates per product, without sacrificing performance.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/inventory-updates#inventory-update-methods)


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
```

```bash
python3 -m pip install google.cloud.retail
```

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable. It will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Add fulfillment places 

To send the ```AddFulfillmentPlacesRequest```, you need to set the following fields:
 - ```product``` - the product name whose inventory information you wnd to update,
 - ```type``` - the fulfillment type. You may set one of the [supported values](https://cloud.google.com/retail/docs/reference/rpc/google.cloud.retail.v2#addfulfillmentplacesrequest),
 - ```place_ids[]``` - the store IDs for each of the fulfillment types,
 - ```add_time``` - the time when the fulfillment updates are pushed. It is used to prevent out-of-order updates on the fulfillment information. If not provided, the internal system time will be used,
 - ```allow_missing``` - if set to true and the Product is not found, the fulfillment information will still be processed and retained for up to 24 hours and processed once the Product is created. 

Open **product/add_fulfillment_places.py** and check the ```AddFulfillmentPlacesRequest```.

To add the fulfillment places, open terminal and run the following command:

```bash
python product/add_fulfillment_places.py
```

Check the responses in the Terminal. As you can see, the product was initially created with fulfillment places 'store0' and 'store1'. 
Then, check the ```get_product()``` response, the fulfillment places 'store2', 'store3', 'store4' was added to the 'pickup-in-store' fulfillment type.

## Send out-of-order add_fulfillment_places request

The ```AddFulfillmentPlaces``` method allows you to specify the update time when the request is sent.
The Retail API compares the update time you've specified with the latest recorded for the relevant inventory fields. The update happens only if the specified update time value is greater than the latest update time value.

Let's modify the ```add_fulfillment_request```: change the list of the **place_ids**.

To change the ```request_time``` value, set now() - 1 day:
```
request_time = datetime.datetime.now() - datetime.timedelta(days=1)
```
Next, before you run the same code sample again, comment out the line ```create_product(product_id)``` to avoid the error message "Product already exists" appears.

Uncomment the ```#delete_product(product_name)``` line to clean up after the code sample run.

Run the code once again:
```bash
python product/add_fulfillment_places.py
```

Check the product printed out in the Terminal. The fulfillment places information has no updates.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to add the product fulfillment places using the Retail API. We encourage you to 
practice in updating fulfillment information right here in Cloud Shell environment.

**Thank you for completing this tutorial!**
