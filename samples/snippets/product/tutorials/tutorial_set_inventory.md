# **Set Inventory**

## Let's get started

Changes to a product inventory information may occur more frequently than changes to the catalog information..

You may decide to push inventory updates instead of updating the entire product.

In such cases, you can use the **```SetInventory```** method.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/inventory-updates#non-incremental-updates)


**Time to complete**: 
<walkthrough-tutorial-duration duration="3.0"></walkthrough-tutorial-duration>

## Before you begin

To run Python code samples from this tutorial, you need to set up your virtual environment.

To do that, run the following commands in a Terminal:

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

**Tip**: Click the copy button on the side of the code box to paste the command in the Cloud Shell Terminal and run it.

## Set the PROJECT_NUMBER environment variable

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable. It will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Set inventory 

To send the ```SetInventoryRequest```, you need to set the following fields:
 - ```inventory``` - the inventory information to update. The fields allowed for updating are: 
    * ```Product.price_info```
    * ```Product.availability``` 
    * ```Product.available_quantity``` 
    * ```Product.fulfillment_info```
 - ```set_mask``` - indicates what product inventory fields to update,
 - ```set_time``` - the time when the request is sent. It is used to prevent out-of-order updates on inventory fields that contain the last update time recorded value,
 - ```allow_missing``` - if set to true and the Product is not found, the fulfillment information will still be processed and retained for up to 24 hours, and then processed once you create the Product. 

Open **product/set_inventory.py** and check the ```SetInventoryRequest``` request.

To add the fulfillment places, open Terminal and run the following command:

```bash
python product/set_inventory.py
```

Check the responses in the Terminal. As you can see, the product was initially created with some **price_info** and **availability** information.
Next, to ensure that the product inventory information was updated successfully, check the ```get_product()``` response.

## Send out-of-order SetInventory request

The ```SetInventory``` method allows you to specify an update time when the request is sent.
he Retail API compares the update time you've specified with the latest recorded for the relevant inventory fields. The update happens only if the specified update time value is greater than the latest update time value.

For example, let's modify the product price field value.

Change the ```set_inventory_request``` request and set the ```request_time``` value to yesterday:
```
request_time = datetime.datetime.now() - datetime.timedelta(days=1)
```

Run the code once again:
```bash
python product/set_inventory.py
```

Check the product printed out in the Terminal. The inventory information was not updated.

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to update the product inventory information using the Retail API. We encourage you to 
practice in updating product inventory right here in the Cloud Shell environment.

**Thank you for completing this tutorial!**
