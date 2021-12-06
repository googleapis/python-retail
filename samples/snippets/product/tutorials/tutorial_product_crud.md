# **Create-Get-Update-Delete Product Tutorial**

## Let's get started

In this tutorial you will learn how to use Retail API Product Service methods which are exposed to perform the following actions: 

 - create_product, 
 - get_product, 
 - update_product,
 - delete_product methods.

You will start with **creating a simple product**, then call **get product** method, next you will **update some product fields**, and finally **remove the product** from the catalog.

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

## Product object overview

The required product fields are:

 - **```name```** - Full resource name of the product, which is:
 ```none
 projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
 ```
 - **```id```** - Product identifier, which is the final component of product name.
 - **```type```** - The type of the product. Default to "PRIMARY"
 - **```primary_product_id```** - Variant group identifier, required for VARIANT products
 - **```categories[]```** - Names of categories the product belongs to, can represent different category hierarchies.
 - **```title```** - The product title which will be to a customer


## Generate simple product object

In this tutorial you will create a simple PRIMARY product, like this one, presented in JSON format:

```json
{
  "name": "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/default_branch/products/crud_product_id",
  "id": "crud_product_id",
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

Open **crud_product.py** code sample and check this product generation with the method ```generate_product()```.

## Create a product request

To create a product you should send a **CreateProductRequest** to Retail API with the following required fields specified:
 - **```product```** - the product object you want to create
 - **```product_id```** - product id 
 - **```parent```** - a branch name in a catalog where the product will be created

Check the ```CreateProductRequest``` along with the Retail API call in the code sample **```create_product()```** method.

The Retail API returns the created product as a response

## Get a product

To build GetProductRequest only ```name``` field is required. You should pass the **full resource name of Product**, which is:
```none
projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
```

You can find the GetProductRequest example in a **```get_product()```** method.

The Retail API returns the requested **product with all product fields** despite the list od retrievable fields provided in a product.retrievable_fields - it defines which product fields should be displayed only in a SearchResponse.

## Update a product request

To update a product you should send a **UpdateProductRequest** to Retail API with the following required fields specified:
 - **```product```** - the product object to be updated or created (depending on the  ```allow_missing``` value the product can be created if missing).
 - **```update_mask```** - indicates which fields in the provided product to update.
 - **```allow_missing```** - if set to true, and the Product is not found, a new Product will be created.


## Prepare data for Update Request

Let's assume you want to update each of its fields. You should set the product object you would like to see in a catalog ot the request field **```product```**

Take a look at the method **```generate_product_for_update()```** it returns the product object with updated fields except of fields ```name```, ```id```, ```type_``` - these fields are immutable.

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

Check the **UpdateProductRequest** example in a **```update_product()```** method.

In the Retail API response the updated product is returned.

## Delete a product

To build DeleteProductRequest, only **```name```** field is required. 

You should pass the **full resource name of Product**, such as:
```none
projects/<project_number>/locations/global/catalogs/<catalog_id>/branches/<branch_id>/products/<product_id>
```

You can find the DeleteProductRequest example in a **```delete_product()```** method

There is no return value for this method, so to check if the product was successfully removed we will try to get the product one more time.
The following error message is expected to appear:

```google.api_core.exceptions.NotFound: 404 Product with name "projects/<PROJECT_NUMBER>/locations/global/catalogs/default_catalog/branches/0/products/<PRODUCT_ID>" does not exist.```

## Run the CRUD code sample

When you run this code sample, the following actions will be made:

1. Call ```create_product()``` Retail API method, create a product with id 'crud_product_id'.
2. Call ```get_product()``` API method and receive the created product.
3. Call ```update_product()``` API method to update all the product fields except the immutable ones.
4. Call ```delete_product()``` API method to delete the created product from the catalog

Now, open terminal and run the command:

```bash
python product/crud_product.py
```

Check all the requests and the API responses in the console output. 

## Congratulations

<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You have completed the tutorial! Now you know how to manage a product in a catalog using Retail API. We encourage you to 
practice in creating, reading, updatig and deleting products right here, in Cloud Shell environment or in your oun Google Cloud Catalog.

**Thank you for completing this tutorial!**
