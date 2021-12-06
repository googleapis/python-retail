# **Delete Product Tutorial**

## Let's get started

If you need to make some detached changes in your product catalog, you may call the following Retail API methods:
 - create_product, 
 - get_product, 
 - update_product, 
 - delete_product.

In this tutorial you will call the **delete_product()** method.

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

## Delete a product

To build DeleteProductRequest, only **```name```** field is required. 

You should pass the **full resource name of Product**, such as:
```none
projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
```

You can find the DeleteProductRequest example in a **delete_product.py**

When you run this code sample, a product will be created in a catalog, then it will be removed using a prepared request.

Open terminal and run the command:

```bash
python product/delete_product.py
```

There is no return value for this method, so to check if the product was successfully removed let's try to delete this product one more time. As the product cannot be deleted twice, we expect the following error message:

```google.api_core.exceptions.NotFound: 404 Product with name "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/0/products/<PRODUCT_ID>" does not exist.```

Copy the product name from the output message ( it is printed in a terminal ) and assign it to the variable **```created_product_name```**.

Now, run the code again, you should receive the error message as above.

## Error handling

If you send a request without the field **```name```** or if the field format is incorrect you will get an error message.

Let's now remove the product_id part from the **```name```**  value and send this request again. 

**The expected error message** should be like:

```google.api_core.exceptions.InvalidArgument: 400 Request contains an invalid argument.```

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to remove a single product from the catalog using Retail API. 
We encourage you to practice in deleting products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
