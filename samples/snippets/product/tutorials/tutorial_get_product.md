# **Get Product Tutorial**

## Let's get started

If you need to make some detached changes in your product catalog, you may call the following Retail API methods:
 - create_product, 
 - get_product, 
 - update_product, 
 - delete_product.

In this tutorial you will call the **get_product()** method and check the service response.

You can find detailed information about managing catalog information in the [Retail API documentation](https://cloud.google.com/retail/docs/manage-catalog)

**Time to complete**: 
<walkthrough-tutorial-duration duration="2.0"></walkthrough-tutorial-duration>

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

## Get a product

To build GetProductRequest only ```name``` field is required. You should pass the **full resource name of Product**, which is:
```none
projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
```

You can find the GetProductRequest example in a **get_product.py**

When you run this code sample, a product will be created in a catalog, then you will get it using a prepared request.

Open terminal and run the command:

```bash
python product/get_product.py
```

The Retail API returns the requested **product with all product fields** despite the list od retrievable fields provided in a product.retrievable_fields - it defines which product fields should be displayed only in a SearchResponse.

## Error handling

If you send a request without the field **```name```** or if the field format is incorrect you will get an error message.

Let's now remove the product_id part from the **```name```**  value and send this request again. 

**The expected error message** should be like:

TODO
```[PUT THE ERROR MESSAGE HERE]```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to get a single product from the catalog using Retail API.
We encourage you to practice in getting products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
