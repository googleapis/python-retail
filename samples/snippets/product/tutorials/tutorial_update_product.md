# **Update Product Tutorial**

## Let's get started

To fill the catalog or to update a massive amount of products we recommend to use Import products method. 
However sometimes you may need to make some detached changes in your product catalog. For such cases the Retail API provides you such ability
exposing 
 - create_product, 
 - get_product, 
 - update_product,
 - delete_product methods.

In this tutorial you will **update product in a catalog**.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/manage-catalog)

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

As you are going to run the code samples in your own Cloud Project, you should specify the **project_id** as an environment variable, it will be used in every request to the Retail API.

You can find the ```project_number``` in the **Home/Dashboard/Project Info card**.

Set the environment variable with a following command:
```bash
export PROJECT_NUMBER=<YOUR_PROJECT_NUMBER>
```

## Update a product request

To update a product you should send a **UpdateProductRequest** to Retail API with the following required fields specified:
 - **```product```** - the product object to be updated or created (depending on the  ```allow_missing``` value the product can be created if missing).
 - **```update_mask```** - indicates which fields in the provided product to update.
 - **```allow_missing```** - if set to true, and the Product is not found, a new Product will be created.


## Prepare data for Update Request

When you run this code sample, first a product will be created in a catalog, then it will be updated using a prepared request.

The **originally created product** is the following:
```py
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/<PRODUCT_ID>",
  "id": "<PRODUCT_ID>",
  "type": "PRIMARY",
  "categories": [
    "Speakers and displays"
  ],
  "brands": [
    "Google"
  ],
  "title": "Nest Mini",
  "availability": "IN_STOCK",
  "price_info": {
    "price": 30.0,
    "original_price": 35.5,
    "currency_code": "USD"
  }
}
```

Let's assume you want to update each of its fields. You should set the product object you would like to see in a catalog ot the request field **```product```**

The **product object for update** is the following:
```py
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/<PRODUCT_ID>", #cannot be updated , should point to existent product
  "id": "<PRODUCT_ID>", #cannot be updated 
  "type": "PRIMARY", #cannot be updated
  "categories": [
    "Updated Speakers and displays"
  ],
  "brands": [
    "Updated Google"
  ], 
  "title": "Updated Nest Mini",
  "availability": "OUT_OF_STOCK",
  "price_info": {
    "price": 20.0,
    "original_price": 55.5,
    "currency_code": "EUR"
  }
}
```

You can find the update product request example in a **update_product.py**

Open terminal and run the command:
```bash
python product/update_product.py
```

**Check the response - the Retail API returns an updated product.**

## Update product using update mask

The **```update_mask```**, if specified in the UpdateProductRequest, indicates which fields in the provided Product to update. 

Note that the immutable and output only fields are not supported.

If not set, all supported fields are updated.

Let's assume that you want to update only some fields in the original product, you list them in a **```update mask```** like this:
```py
FieldMask(paths=['title', 'price_info', 'color_info'])
```

Modify the UpdateProductRequest in the **get_update_product_request()** method - add the following update_mask field:
```py
update_product_request.update_mask = FieldMask(paths=['title', 'price_info', 'color_info'])
```

Run the code sample again and check the response printed in Terminal.

As you can see **only the product fields listed in the  ```update_mask``` were updated**, the other fields were not changed even if provided in the product object in the UpdateProductRequest.

## Error handling

If you send a request without one of required fields or if the field format is incorrect you will get an error message.

Let's now remove the product field **```name```** and send this request again. 

**The expected error message** should be like:

TODO
```[PUT THE ERROR MESSAGE HERE]```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to update a product in a catalog using Retail API.
We encourage you to practice in updating products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
